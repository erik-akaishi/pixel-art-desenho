# Pixel Art Mistério

Produto pessoal (AK Labs / Erik + esposa) — coleção de pixel art "colorir por código" (mystery/color-by-number), estilo kawaii.

## Estrutura do projeto

```
docs/       → documentação de produto e da pesquisa de mercado (Markdown)
editor/     → editor visual (HTML/JS, roda no navegador, sem backend)
pipeline/   → scripts Python (vetorização, ingestão, geração de PDF)
```

## docs/

- `masterclass-low-ticket.md` — estudo da masterclass de low ticket, garimpo de nicho, validação de mercado
- `produto-pixel-art-misterio.md` — especificação completa do produto, guia de estilo, prompts calibrados, histórico de calibração técnica

## editor/

`index.html` — editor de grade pixel art. Abre direto no navegador (sem instalação). Funcionalidades:
- Detecção automática a partir de uma imagem de referência
- Pintura manual célula a célula (conta-gotas, desfazer, fusão de cor por hex)
- Exportação em PNG (pronto pra impressão) ou JSON (grade + paleta, pra reprocessar)

**Hospedagem:** é um arquivo estático puro, sem backend — pode subir em GitHub Pages, Vercel ou Netlify sem nenhuma configuração especial.

## pipeline/

Scripts Python que fazem a parte pesada: vetorização, ingestão (imagem → grade numerada), geração das versões mistério/gabarito/legenda, e montagem dos PDFs finais.

- `pixelkit.py` — núcleo: canvas de desenho, renderização (colorida, mistério, legenda), montagem de página/PDF
- `ingest.py` — ingestão de imagem (`image_to_canvas`), vetorização (`vectorize_source`), leitura do JSON do editor (`canvas_from_json`)

**Dependências:**
```
pip install pillow vtracer cairosvg
```

**Padrão de calibração atual** (ver `docs/produto-pixel-art-misterio.md`, seções 17–21):
- Grade: variável por ilustração (medido de produto real: ~29×36 até ~42×55)
- Pré-achatamento: 64 cores
- Tamanho de exportação: 2362×3189px (200×270mm — A4/Carta)

## Fluxo de produção

```
1. IA gera a ilustração (prompt calibrado em docs/produto-pixel-art-misterio.md §15)
2. editor/index.html — correção manual, exporta PNG limpo
3. pipeline/ingest.py — vetorização (se necessário) + ingestão
4. pipeline/pixelkit.py — geração dos PDFs finais
```
