"""
Pixel Art Mistério — toolkit de geração
Núcleo do pipeline: canvas de desenho por células, renderização colorida (gabarito),
renderização em grade-mistério (código + legenda), e exportação para PDF.
"""
from PIL import Image, ImageDraw, ImageFont
import math

BG = "."  # célula vazia / fora do desenho

class PixelCanvas:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.grid = [[BG for _ in range(width)] for _ in range(height)]

    def set_cell(self, x, y, code):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.grid[y][x] = code

    def fill_rect(self, x0, y0, x1, y1, code):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.set_cell(x, y, code)

    def fill_ellipse(self, cx, cy, rx, ry, code, overwrite=True):
        for y in range(self.h):
            for x in range(self.w):
                dx = (x - cx) / rx
                dy = (y - cy) / ry
                if dx * dx + dy * dy <= 1.0:
                    if overwrite or self.grid[y][x] == BG:
                        self.set_cell(x, y, code)

    def mirror_left_right(self):
        """Espelha a metade esquerda (assumindo simetria vertical central)."""
        for y in range(self.h):
            for x in range(self.w // 2):
                self.grid[y][self.w - 1 - x] = self.grid[y][x]


def _font(size):
    try:
        return ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size
        )
    except Exception:
        return ImageFont.load_default()


def render_colored(canvas, palette, cell_px=24, outline=(210, 210, 210)):
    """Gabarito: imagem totalmente colorida (resposta certa)."""
    img = Image.new("RGB", (canvas.w * cell_px, canvas.h * cell_px), "white")
    d = ImageDraw.Draw(img)
    for y in range(canvas.h):
        for x in range(canvas.w):
            code = canvas.grid[y][x]
            if code == BG:
                continue
            color = palette[code]["rgb"]
            x0, y0 = x * cell_px, y * cell_px
            x1, y1 = x0 + cell_px, y0 + cell_px
            d.rectangle([x0, y0, x1, y1], fill=color, outline=outline)
    return img


def render_mystery(canvas, palette, cell_px=24, grid_color=(140, 140, 140), number_color=(195, 195, 195)):
    """Grade mistério: células em branco com o NÚMERO da cor (sutil, mais claro que a grade)."""
    img = Image.new("RGB", (canvas.w * cell_px, canvas.h * cell_px), "white")
    d = ImageDraw.Draw(img)
    font_size = max(8, int(cell_px * 0.42))
    font = _font(font_size)
    for y in range(canvas.h):
        for x in range(canvas.w):
            code = canvas.grid[y][x]
            x0, y0 = x * cell_px, y * cell_px
            x1, y1 = x0 + cell_px, y0 + cell_px
            d.rectangle([x0, y0, x1, y1], outline=grid_color)
            if code == BG:
                continue
            label = str(palette[code]["num"])
            bbox = d.textbbox((0, 0), label, font=font)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            d.text(
                (x0 + (cell_px - tw) / 2, y0 + (cell_px - th) / 2 - bbox[1]),
                label,
                fill=number_color,
                font=font,
            )
    return img


def _luminance(rgb):
    r, g, b = rgb
    return 0.299 * r + 0.587 * g + 0.114 * b


def render_legend_strip(palette, codes_in_order, mode, swatch_px=70, label=None):
    """
    Legenda em faixa horizontal, no modelo 'color by number':
    cada número tem um quadrado (vazio ou colorido) com o número dentro.
    mode: "vazio" (contorno + número escuro, sem preencher) ou "sugestao" (preenchido).
    """
    n = len(codes_in_order)
    gap = 14
    label_w = 210 if label else 0
    width = label_w + n * (swatch_px + gap) + gap
    height = swatch_px + 30
    img = Image.new("RGB", (width, height), "white")
    d = ImageDraw.Draw(img)
    font = _font(int(swatch_px * 0.4))
    label_font = _font(26)

    if label:
        d.text((10, height / 2 - 14), label, fill=(60, 60, 60), font=label_font)

    x = label_w + gap
    y = 15
    for code in codes_in_order:
        info = palette[code]
        num = str(info["num"])
        if mode == "sugestao":
            fill = info["rgb"]
            d.rectangle([x, y, x + swatch_px, y + swatch_px], fill=fill, outline=(120, 120, 120), width=2)
            txt_color = (255, 255, 255) if _luminance(fill) < 140 else (40, 40, 40)
        else:  # vazio
            d.rectangle([x, y, x + swatch_px, y + swatch_px], fill="white", outline=(150, 150, 150), width=2)
            txt_color = (90, 90, 90)
        bbox = d.textbbox((0, 0), num, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        d.text((x + (swatch_px - tw) / 2, y + (swatch_px - th) / 2 - bbox[1]), num, fill=txt_color, font=font)
        x += swatch_px + gap
    return img


def render_legend(palette, used_codes, width_px, cell_px=24):
    """Tabela de legenda: código -> cor -> nome."""
    used = [c for c in palette if c in used_codes]
    row_h = cell_px
    img = Image.new("RGB", (width_px, row_h * len(used) + 20), "white")
    d = ImageDraw.Draw(img)
    font = _font(max(10, cell_px // 2))
    y = 10
    for code in used:
        info = palette[code]
        d.rectangle([10, y, 10 + row_h, y + row_h], fill=info["rgb"], outline=(120, 120, 120))
        d.text((10 + row_h + 12, y + row_h / 2 - 8), f"{info['code']}  —  {info['name']}", fill="black", font=font)
        y += row_h
    return img


def used_codes(canvas):
    s = set()
    for row in canvas.grid:
        for c in row:
            if c != BG:
                s.add(c)
    return s


def add_silhouette_outline(canvas, outline_code="K"):
    """Adiciona contorno de 1 célula ao redor de toda a silhueta (regiao nao-BG)."""
    to_set = []
    for y in range(canvas.h):
        for x in range(canvas.w):
            if canvas.grid[y][x] != BG:
                continue
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < canvas.w and 0 <= ny < canvas.h and canvas.grid[ny][nx] != BG:
                    to_set.append((x, y))
                    break
    for x, y in to_set:
        canvas.grid[y][x] = outline_code


# ---------------------------------------------------------------
# Montagem de páginas / PDFs
# ---------------------------------------------------------------
PAGE_W, PAGE_H = 2480, 3508  # A4 a 300dpi


def _paste_centered(page, img, top_y):
    x = (page.width - img.width) // 2
    page.paste(img, (x, top_y))
    return top_y + img.height


def build_page(illustration_img, legend_imgs, title, subtitle=None, page_size=(PAGE_W, PAGE_H),
                gap_between_legends=6, gap_before_grid=90):
    """legend_imgs: lista de imagens de legenda, na ordem em que aparecem de cima para baixo
    (a última da lista fica mais próxima da grade, respeitando gap_before_grid)."""
    page = Image.new("RGB", page_size, "white")
    d = ImageDraw.Draw(page)
    title_font = _font(70)
    sub_font = _font(40)
    y = 80
    bbox = d.textbbox((0, 0), title, font=title_font)
    d.text(((page_size[0] - (bbox[2] - bbox[0])) / 2, y), title, fill="black", font=title_font)
    y += (bbox[3] - bbox[1]) + 30
    if subtitle:
        bbox = d.textbbox((0, 0), subtitle, font=sub_font)
        d.text(((page_size[0] - (bbox[2] - bbox[0])) / 2, y), subtitle, fill=(100, 100, 100), font=sub_font)
        y += (bbox[3] - bbox[1]) + 40
    else:
        y += 20

    # legendas (gap pequeno entre elas)
    for i, legend_img in enumerate(legend_imgs):
        y = _paste_centered(page, legend_img, y)
        if i < len(legend_imgs) - 1:
            y += gap_between_legends

    # gap maior antes da grade
    y += gap_before_grid

    max_w = page_size[0] - 240
    max_h = page_size[1] - y - 120
    scale = min(max_w / illustration_img.width, max_h / illustration_img.height)
    illo = illustration_img.resize(
        (int(illustration_img.width * scale), int(illustration_img.height * scale)), Image.NEAREST
    )
    _paste_centered(page, illo, y)
    return page


def build_cover(title, subtitle, page_size=(PAGE_W, PAGE_H)):
    page = Image.new("RGB", page_size, (250, 248, 240))
    d = ImageDraw.Draw(page)
    title_font = _font(130)
    sub_font = _font(55)
    bbox = d.textbbox((0, 0), title, font=title_font)
    d.text(((page_size[0] - (bbox[2] - bbox[0])) / 2, page_size[1] // 2 - 200), title, fill="black", font=title_font)
    bbox2 = d.textbbox((0, 0), subtitle, font=sub_font)
    d.text(((page_size[0] - (bbox2[2] - bbox2[0])) / 2, page_size[1] // 2 - 40), subtitle, fill=(90, 90, 90), font=sub_font)
    return page


def build_instructions(page_size=(PAGE_W, PAGE_H)):
    page = Image.new("RGB", page_size, "white")
    d = ImageDraw.Draw(page)
    title_font = _font(80)
    body_font = _font(46)
    d.text((120, 100), "Como colorir por código", fill="black", font=title_font)
    lines = [
        "1. Escolha uma ilustração da coleção.",
        "2. Veja a legenda, cada código (1, 2, ...) corresponderá a uma",
        "    cor, sugerida ou da sua escolha.",
        "3. Pinte cada quadrado com a cor escolhida pro código.",
        "4. A imagem surpresa vai aparecer aos poucos — não espie o",
        "    gabarito!",
        "5. Terminou? Confira sua obra na página de gabarito no fim",
        "    do arquivo.",
    ]
    y = 260
    for line in lines:
        d.text((120, y), line, fill=(40, 40, 40), font=body_font)
        y += 90
    return page


def build_mini_page(pairs, page_size=(PAGE_W, PAGE_H)):
    """pairs: lista de até 2 tuplas (mystery_img, title) para uma folha (2 por folha)."""
    page = Image.new("RGB", page_size, "white")
    d = ImageDraw.Draw(page)
    title_font = _font(50)
    slot_h = page_size[1] // 2
    for i, (img, title) in enumerate(pairs):
        top = i * slot_h
        bbox = d.textbbox((0, 0), title, font=title_font)
        d.text(((page_size[0] - (bbox[2] - bbox[0])) / 2, top + 60), title, fill="black", font=title_font)
        max_w = page_size[0] - 300
        max_h = slot_h - 300
        scale = min(max_w / img.width, max_h / img.height)
        mini = img.resize((int(img.width * scale), int(img.height * scale)), Image.NEAREST)
        x = (page_size[0] - mini.width) // 2
        page.paste(mini, (x, top + 180))
        if i == 0:
            d.line([(150, slot_h), (page_size[0] - 150, slot_h)], fill=(200, 200, 200), width=3)
    return page


def save_pdf(pages, path):
    pages[0].save(path, save_all=True, append_images=pages[1:])

