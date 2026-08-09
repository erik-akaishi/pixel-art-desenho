"""
Ingestão de arte pronta -> canvas de grade
Fluxo: Erik/esposa produzem o gabarito colorido (pixel art já em blocos definidos,
com fundo transparente OU fundo bem distinto da arte) -> este script lê a imagem,
reduz para a resolução de grade alvo, identifica as células de fundo, quantiza
a paleta de cores, e devolve um PixelCanvas + palette prontos para o resto do
pipeline (render_mystery, render_legend_strip, build_page, etc).
"""
from PIL import Image
from collections import deque
from pixelkit import PixelCanvas, BG


def _flood_fill_background(pixels, w, h, bg_test):
    """Detecta a região de fundo (conectada às bordas) via flood fill a partir dos 4 cantos."""
    is_bg = [[False] * w for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    q = deque()
    for x in range(w):
        q.append((x, 0)); q.append((x, h - 1))
    for y in range(h):
        q.append((0, y)); q.append((w - 1, y))
    while q:
        x, y = q.popleft()
        if x < 0 or x >= w or y < 0 or y >= h or visited[y][x]:
            continue
        visited[y][x] = True
        if not bg_test(pixels[y][x]):
            continue
        is_bg[y][x] = True
        q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return is_bg


def image_to_canvas(path, cols, rows, max_colors=10, merge_distance=45, neutral_merge_distance=90, white_threshold=245, preflatten_colors=64):
    """
    Lê uma imagem (gabarito colorido) e converte para PixelCanvas + palette.

    - cols, rows: resolução de grade alvo (deve bater com a grade em que a arte foi desenhada)
    - Se a imagem tiver canal alpha, transparência = fundo (BG)
    - Caso contrário, faz flood-fill a partir das bordas sobre pixels quase-brancos
      para detectar o fundo automaticamente (assume fundo claro/branco)
    - Usa amostragem por MODA de múltiplos pontos por célula, não média/pixel único
    - PRÉ-ACHATA a imagem inteira pra poucas cores em alta resolução ANTES de dividir em
      células — remove pixels de transição/antialiasing na origem (arte gerada por IA tem
      bordas com gradiente suave; achatar primeiro resolve isso na raiz, não só na amostragem)
    """
    img = Image.open(path).convert("RGBA")
    has_alpha = img.split()[-1].getextrema() != (255, 255)
    W, H = img.size

    # pre-achatamento: quantiza a imagem INTEIRA (em alta resolucao) para poucas cores,
    # isso colapsa os pixels de transicao antialiasada pro lado mais proximo, antes de
    # qualquer amostragem por celula
    rgb_img = img.convert("RGB")
    flat = rgb_img.quantize(colors=preflatten_colors, method=Image.MEDIANCUT).convert("RGB")
    flat_rgba = Image.new("RGBA", img.size)
    flat_rgba.paste(flat, (0, 0))
    flat_rgba.putalpha(img.split()[-1])
    img = flat_rgba
    px = img.load()

    def cell_bounds(c, r):
        x0 = int(c * W / cols)
        x1 = max(x0 + 1, int((c + 1) * W / cols))
        y0 = int(r * H / rows)
        y1 = max(y0 + 1, int((r + 1) * H / rows))
        return x0, x1, y0, y1

    def multipoint_color(x0, x1, y0, y1):
        # amostra uma grade esparsa de pontos (nao a area inteira) e pega a MODA.
        # single-pixel central e' fragil contra aliasing (ex: linhas finas de papel
        # quadriculado numa referencia); moda de area inteira borra detalhe fino
        # (ex: almofadinha de pata). Multiplos pontos espalhados e' o meio-termo.
        w, h = x1 - x0, y1 - y0
        n = 3  # grade 3x3 de pontos por celula
        counts = {}
        for iy in range(n):
            for ix in range(n):
                px_x = x0 + int((ix + 0.5) * w / n)
                px_y = y0 + int((iy + 0.5) * h / n)
                px_x = min(px_x, x1 - 1)
                px_y = min(px_y, y1 - 1)
                r, g, b, a = px[px_x, px_y]
                key = (r // 12 * 12, g // 12 * 12, b // 12 * 12)
                counts[key] = counts.get(key, 0) + 1
        return max(counts, key=counts.get)

    pixels_rgb = [[None] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            x0, x1, y0, y1 = cell_bounds(c, r)
            pixels_rgb[r][c] = multipoint_color(x0, x1, y0, y1)

    if has_alpha:
        alpha_avg = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                x0, x1, y0, y1 = cell_bounds(c, r)
                tot = 0
                n = 0
                for y in range(y0, y1):
                    for x in range(x0, x1):
                        tot += px[x, y][3]
                        n += 1
                alpha_avg[r][c] = tot / n
        is_bg = [[alpha_avg[r][c] < 128 for c in range(cols)] for r in range(rows)]
    else:
        def bg_test(rgb):
            r, g, b = rgb
            return r >= white_threshold and g >= white_threshold and b >= white_threshold
        is_bg = _flood_fill_background(pixels_rgb, cols, rows, bg_test)

    # consolida as cores dominantes em no maximo max_colors: agrupa por frequencia,
    # mas MESCLA cores proximas entre si (evita ter, por ex, 3 tons quase iguais de
    # cinza escuro como "cores" separadas so porque cada um apareceu muitas vezes)
    freq = {}
    for r in range(rows):
        for c in range(cols):
            if is_bg[r][c]:
                continue
            freq[pixels_rgb[r][c]] = freq.get(pixels_rgb[r][c], 0) + 1

    def dist(a, b):
        return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

    def is_neutral(c, thresh=22):
        return max(c) - min(c) <= thresh

    def should_merge(a, b):
        # cores neutras (preto/cinza/branco) só mesclam com outras neutras — evita que
        # ruído de antialiasing (ex: cinza-escuro perto do contorno preto) vire uma cor
        # "oficial" à parte. Cores cromáticas (rosa, verde, bege...) usam um limiar mais
        # rígido entre si, e NUNCA mesclam com neutras (senão rosa claro vira bege).
        if is_neutral(a) and is_neutral(b):
            return dist(a, b) < neutral_merge_distance
        if is_neutral(a) != is_neutral(b):
            return False
        return dist(a, b) < merge_distance

    ordered = sorted(freq, key=freq.get, reverse=True)
    canonical = []
    for color in ordered:
        if not any(should_merge(color, k) for k in canonical):
            canonical.append(color)
        if len(canonical) >= max_colors:
            break

    def nearest_canonical(color):
        candidates = [k for k in canonical if is_neutral(k) == is_neutral(color)] or canonical
        return min(candidates, key=lambda k: dist(k, color))

    qmap = {color: nearest_canonical(color) for color in freq}

    canvas = PixelCanvas(cols, rows)
    palette = {}
    color_to_code = {}
    next_num = 1

    for r in range(rows):
        for c in range(cols):
            if is_bg[r][c]:
                continue
            color = qmap[pixels_rgb[r][c]]
            if color not in color_to_code:
                code = f"C{next_num}"
                palette[code] = {"rgb": color, "num": next_num, "name": f"Cor {next_num}"}
                color_to_code[color] = code
                next_num += 1
            canvas.set_cell(c, r, color_to_code[color])

    codes_order = list(palette.keys())
    return canvas, palette, codes_order


if __name__ == "__main__":
    # auto-teste: reingere nosso próprio gabarito do panda pra validar o mecanismo
    canvas, palette, order = image_to_canvas(
        "/home/claude/pixelart/panda_gabarito.png", cols=46, rows=50, max_colors=10
    )
    from pixelkit import render_colored, render_mystery, render_legend_strip

    render_colored(canvas, palette, cell_px=16).save("/home/claude/pixelart/reingest_gabarito.png")
    render_mystery(canvas, palette, cell_px=16).save("/home/claude/pixelart/reingest_misterio.png")
    render_legend_strip(palette, order, "sugestao", label="Sugestão").save(
        "/home/claude/pixelart/reingest_legenda.png"
    )
    print("Cores detectadas:", len(palette))


def canvas_from_json(path):
    """
    Lê o arquivo grade.json exportado pelo editor.html (correção manual) e monta
    PixelCanvas + palette no mesmo formato usado pelo resto do pipeline.
    Esta é a via RECOMENDADA quando a detecção automática (image_to_canvas) não
    for confiável o suficiente — usa exatamente o que foi pintado manualmente.
    """
    import json
    with open(path) as f:
        data = json.load(f)

    cols, rows = data["cols"], data["rows"]
    canvas = PixelCanvas(cols, rows)
    palette = {}
    num_to_code = {}

    for p in data["palette"]:
        code = f"C{p['num']}"
        rgb = tuple(int(p["hex"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        palette[code] = {"rgb": rgb, "num": p["num"], "name": f"Cor {p['num']}"}
        num_to_code[p["num"]] = code

    for r in range(rows):
        for c in range(cols):
            num = data["grid"][r][c]
            if num is not None:
                canvas.set_cell(c, r, num_to_code[num])

    codes_order = [num_to_code[p["num"]] for p in data["palette"]]
    return canvas, palette, codes_order


def vectorize_source(input_path, output_path, resolution=1254, **vtracer_kwargs):
    """
    Etapa recomendada ANTES de image_to_canvas(): vetoriza a arte gerada por IA
    (raster, com antialiasing) e renderiza de volta em alta resolução como PNG
    de cores 100% sólidas — elimina o antialiasing na origem, em vez de só
    compensar por ele na amostragem/pré-achatamento.

    Requer: pip install vtracer cairosvg --break-system-packages

    Uso:
        vectorize_source("panda_ia.png", "panda_vetorizado.png")
        canvas, palette, order = image_to_canvas("panda_vetorizado.png", cols=42, rows=55)
    """
    import vtracer
    import cairosvg

    svg_path = output_path.rsplit(".", 1)[0] + ".svg"
    defaults = dict(
        colormode="color",
        hierarchical="stacked",
        mode="spline",
        filter_speckle=4,
        color_precision=6,
        layer_difference=16,
        corner_threshold=60,
        length_threshold=4.0,
        max_iterations=10,
        splice_threshold=45,
        path_precision=3,
    )
    defaults.update(vtracer_kwargs)
    vtracer.convert_image_to_svg_py(input_path, svg_path, **defaults)
    cairosvg.svg2png(url=svg_path, write_to=output_path, output_width=resolution, output_height=resolution)
    return output_path
