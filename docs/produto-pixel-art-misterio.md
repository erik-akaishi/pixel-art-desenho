# Produto: Pixel Art Mistério
### Documentação de produto — AK Labs / projeto pessoal (Erik + esposa)

> Este documento continua a partir do estudo da Masterclass de Low Ticket (documento separado). Aqui entra tudo relativo à estruturação, produção e automação do primeiro produto: **Pixel Art Mistério**.

---

## 1. Visão geral do produto

- **Mecânica:** colorir por número/código — grade em branco numerada + legenda de cores. A imagem só se revela conforme a pessoa colore (diferente de pixel art "cópia direta", que já mostra o resultado ao lado).
- **Validação de mercado:** ver seção 14 do documento da masterclass — Educlub confirma legitimidade pedagógica, Etsy confirma demanda de escala internacional (+1.000 resultados, produtos com 60–1.100 avaliações).
- **Diferencial estratégico:** qualidade de design profissional + tema de Folclore Brasileiro combinado ao formato mistério (combinação ainda não vista em concorrentes mapeados).

## 2. Estrutura de linhas de produto (atualizado)

**Regra:** cada produto atende **um público e um nível de dificuldade só** — nada de misturar infantil e adulto, ou fácil e difícil, dentro do mesmo pacote.

| Linha | Público | Grade | Tema de lançamento |
|---|---|---|---|
| **Linha Infantil** | Crianças (pais/professores) | Grade simples (~20×25 células) | Tema genérico validado primeiro (ex: animais fofos) |
| **Linha Adulto** | Adultos (mindfulness/relaxamento) | Grade detalhada (~30×40 células) | Tema genérico validado primeiro |

Cada linha lança como **produto separado**, com sua própria coleção de 10 ilustrações, sua própria capa, sua própria copy. O Folclore Brasileiro entra como **segunda leva**, já dividido nas mesmas duas linhas (Folclore Infantil / Folclore Adulto), depois que o pipeline estiver validado com o tema genérico.

## 3. Estrutura da coleção (por produto)

- 10 ilustrações, todas do mesmo nível de dificuldade e público
- Mecânica de mistério/código consistente em toda a coleção

## 4. Arquivos do pacote (atualizado)

| Arquivo | Conteúdo | Observação |
|---|---|---|
| **PDF Principal** | Capa + instruções + 10 páginas (1 ilustração grande em grade mistério por página + legenda) | — |
| **PDF Mini** | As 10 ilustrações, **2 por folha** | Mudança: 2 por folha é o padrão para coleções de 10. Só migrar para 4 por folha se a coleção tiver 20 ilustrações. |
| **PDF Gabarito** | As 10 ilustrações já coloridas (resposta certa) | — |
| **JPG de capa/prévia** | Mockup das 10 ilustrações coloridas | Uso em anúncio/loja |
| **PNGs individuais** | Versão de cada ilustração (grade + gabarito) em PNG solto | Para quem colore digital (Procreate/GoodNotes/Adobe Fresco) |
| Entrega final | Tudo compactado em 1 ZIP | — |

## 5. Especificação técnica de arquivo

- Tamanho de imagem: ~2480×3508 px a 300dpi (equivalente A4, compatível com Carta/Letter)
- Margem de segurança para impressão doméstica
- Paleta de cor limitada por ilustração (facilita produção e leitura da legenda)

## 6. Divisão de responsabilidades (revisado — fluxo de ingestão de arte pronta)

**Mudança de abordagem:** em vez de eu gerar a ilustração-fonte via formas geométricas em código (qualidade limitada, muitas rodadas de ajuste fino), o fluxo passa a ser: **vocês produzem o gabarito colorido finalizado** (à mão, ou com a ferramenta de geração de imagem que tiverem) → eu ingiro essa imagem e cuido de toda a parte técnica a partir dali.

| Etapa | Responsável |
|---|---|
| Direção de arte, estilo visual, paleta-mestre da linha | Vocês (com meu apoio de referência/curadoria quando útil) |
| Produção da arte-fonte finalizada (gabarito colorido) | Vocês |
| Curadoria de temas/personagens de cada coleção | Compartilhado |
| **Ingestão da arte** (imagem → grade de células + paleta) | Eu (script `ingest.py`) |
| Geração da versão mistério (grade em branco + números) | Automação |
| Geração da legenda (Sugestão / Sua escolha) | Automação |
| Geração do gabarito formatado | Automação |
| Geração do PDF mini | Automação |
| Diagramação de capa, instruções, montagem final do PDF | Automação |
| Empacotamento final (ZIP) | Automação |
| Validação e aprovação final antes de publicar | Vocês |

**Requisito técnico único para a arte funcionar na ingestão automática:** manter sempre o contorno externo preto fechado (já é regra do guia de estilo, seção 11) — é isso que permite ao script distinguir fundo de desenho por conectividade, mesmo quando usam branco tanto no fundo quanto na pelagem.

## 7. Script de ingestão (`ingest.py`) — validado

Testado com sucesso via auto-teste (reingestão do próprio gabarito do panda): a partir de uma imagem colorida finalizada, o script:
1. Reduz a imagem para a resolução de grade alvo
2. Detecta o fundo automaticamente (via canal alpha, se houver, ou flood-fill a partir das bordas)
3. Quantiza as cores restantes em até N cores
4. Devolve o canvas + paleta prontos para o resto do pipeline (mistério, legenda, gabarito, PDF)

Resultado do teste: 8 cores detectadas corretamente, desenho reconstruído fielmente.



## 7. Tema de lançamento (decidido)

- **Estilo visual:** Kawaii Pixel — proporções fofas (cabeça grande, olhos grandes), contornos arredondados dentro da grade, paleta suave
- **Tema:** Animais mais conhecidos (tema genérico, valida o pipeline antes do Folclore Brasileiro)
- Aplica-se como teste inicial para as duas linhas (Infantil e Adulto), variando apenas a complexidade da grade

## 8. Coleta de referências

Vale a pena montar uma base de referência antes de gerar a arte-fonte — evita um "kawaii genérico" fora do padrão que o público desse nicho já reconhece. Já iniciei essa base:

- Pesquisa de estilo geral: referências de pixel art kawaii para colorir, proporções e traço
- Pesquisa de paleta: referências de paleta de cor típica do gênero (inclusive cruzando com o universo de padrões perler/pixel, que usa convenções de cor parecidas)

O que ajuda vindo de vocês, se quiserem contribuir:
- Exemplos de kawaii/pixel art que já agradam ao olhar de vocês (prints, links, prints de Pinterest)
- Preferência de paleta (mais pastel/suave vs. mais saturado/vibrante)
- Qualquer restrição de estilo (ex: sempre olhos grandes, nunca boca aberta, etc.)

Não é obrigatório — sigo com o que já levantei se preferirem que eu decida sozinho.

## 9. Scripts, skills e processos a construir (atualizado)

Lista do que precisamos montar para deixar o pipeline automático e padronizado — agora incluindo a etapa de idealização/curadoria, não só a técnica:

1. **Processo de idealização de tema e lista de personagens**
   Curadoria dos 10 personagens/motivos de cada coleção — critérios de popularidade, apelo visual, ausência de risco autoral (ver seção de domínio público do documento da masterclass) e diversidade dentro do tema.

2. **Script de geração/definição da arte-fonte**
   Processo pra transformar o conceito de cada personagem em uma ilustração-fonte já pensada em grade (proporção, paleta, nível de detalhe conforme a linha Infantil/Adulto).

3. **Script de conversão arte → grade numerada**
   Quantiza as cores conforme a paleta definida, mapeia cada bloco em uma célula, gera a grade numerada + legenda de cores.

4. **Gerador do PDF Principal**
   Monta capa, instruções, e as 10 páginas de grade mistério, no tamanho técnico definido (seção 5).

5. **Gerador do PDF Mini**
   Reaproveita as grades já geradas e diagrama em 2 por folha (ou 4, quando a coleção tiver 20 ilustrações).

6. **Gerador do Gabarito**
   Monta o PDF com as versões coloridas de referência.

7. **Exportador de PNGs individuais**
   Gera arquivos soltos por ilustração (grade + gabarito) para uso em apps de desenho.

8. **Empacotador final**
   Reúne todos os arquivos gerados em um único ZIP, nomeado e organizado por padrão consistente entre produtos.

9. **Skill dedicada (Claude Code)**
   Uma skill própria (seguindo o mesmo padrão da `akaishi-widget-craft`) que orquestra as etapas 1–8 de ponta a ponta, garantindo que todo produto novo da linha "Pixel Art Mistério" siga exatamente o mesmo processo e padrão de qualidade.

## 11. Guia de estilo visual (a partir das referências coletadas)

### Execução gráfica
- **Contorno preto/escuro grosso e definido**, blocos de cor sólidos — evitar sombreamento em gradiente com muitos tons próximos (dificulta manter a legenda de cores enxuta e prejudica a experiência de "mistério")
- Paleta limitada por ilustração (idealmente entre 4–8 cores), cada cor com seu próprio código na legenda
- Estética kawaii clássica: proporções fofas, traços arredondados dentro da grade

### Regra de composição (obrigatória)
**Nunca desenhar o elemento isolado.** Todo personagem precisa estar em uma cena mínima ou executando uma ação — segurando um objeto, brincando, comendo algo, interagindo com o ambiente. Exemplos de referência: coala abraçado a um galho (não só o coala), ursinho segurando um morango, capivara com uma xícara de café.

### Convenção de legenda
Adotar o mesmo princípio dos padrões de bead-art/ponto de cruz usados como referência: cada célula da grade recebe um **código alfanumérico curto**, mapeado numa tabela de legenda logo abaixo (código → cor). Essa convenção já é reconhecida pelo público do nicho de "colorir por código".

## 12. Lista de personagens — Coleção-teste "Animais Mais Conhecidos" (revisada)

1. **Arara-azul** bicando uma castanha
2. **Leão** espreguiçando e bocejando ao sol
3. **Foca** equilibrando uma bola no nariz
4. **Panda** mordendo um talo de bambu
5. **Coelho** mordendo uma cenoura
6. **Pinguim** escorregando de barriga no gelo
7. **Gato** enrolado dormindo num novelo de lã
8. **Cachorro** brincando com uma bolinha
9. **Elefante** se refrescando com a própria tromba
10. **Coruja** pousada num galho à noite, com estrelas ao fundo

## 13. Próximos passos

- [x] Definir tema genérico de lançamento (Kawaii Pixel — Animais Mais Conhecidos)
- [x] Fechar coleta de referências (estilo + paleta)
- [x] Validar a lista dos 10 personagens/animais da coleção-teste
- [x] Construir o script de conversão arte → grade numerada (`pixelkit.py`)
- [x] Construir os geradores de PDF (principal, mini, gabarito)
- [ ] Montar a skill dedicada no Claude Code (empacotar o pipeline atual numa skill reutilizável)
- [x] Produzir a primeira ilustração-teste de ponta a ponta pelo pipeline (Panda mordendo bambu — item 4 da lista)
- [ ] Produzir as 9 ilustrações restantes da coleção-teste
- [ ] Revisão de qualidade artística com Erik + esposa antes da versão final

## 14. Pipeline técnico — primeira execução (validado)

Construí e testei o pipeline completo de ponta a ponta com a primeira ilustração da coleção (Panda mordendo bambu):

- **`pixelkit.py`** — toolkit núcleo: canvas de desenho por células (formas via elipse/retângulo), contorno automático de silhueta, renderização em 3 modos (colorida/gabarito, grade-mistério com código, legenda), e montagem de páginas/PDF (capa, instruções, página individual, mini 2-por-folha)
- **`panda.py`** — script da ilustração-teste, usando o toolkit
- **`build_pack.py`** — monta os 3 PDFs finais (Principal, Mini, Gabarito) a partir das ilustrações

Resultado: os 3 PDFs foram gerados corretamente, com a mecânica de código funcionando (grade em branco com códigos tipo `W1`, `K1`, `P1` mapeados numa legenda). Validei visualmente cada etapa antes de fechar.

**Observação de qualidade:** essa primeira ilustração é um protótipo de validação do *mecanismo*, não a arte final — o nível de acabamento (curvas mais suaves, proporções mais refinadas) ainda vai passar por iteração antes de ir para produção real. O pipeline técnico já está sólido; o próximo ganho de qualidade vem de refinar o processo de ilustração-fonte.

## 14. Pipeline técnico — refinamentos (rodada 2)

Ajustes aplicados após a primeira revisão:

- **Resolução/detalhe:** ilustração refeita em grade maior (41×50, antes 24×29), com paleta ampliada de 5 para 9 cores — incluindo tons de sombra/profundidade (cinza claro no corpo, verde e bege em dois tons), brilho no olho e almofadinhas de pata. Mais fiel ao nível de detalhe desejado.
- **Legenda dentro da grade:** trocada de código alfanumérico (`W1`, `K1`...) para **numeral simples** (`1`, `2`, `3`...), na cor mais clara/sutil que as linhas da grade — a grade fica mais visível que o número.
- **Legenda em faixa (modelo color-by-number):** implementada no formato de referência trazido — quadrados numerados em fileira horizontal. Duas variações:
  - **"Sua escolha"** — quadrado vazio (só contorno) com o número dentro
  - **"Sugestão"** — quadrado preenchido com a cor sugerida
  - Na página de grade-mistério, as duas fileiras aparecem juntas, **acima da grade**. No gabarito, aparece só a fileira "Sugestão".
- **Instruções:** itens 2 e 3 reescritos conforme solicitado.
- **Título da página:** trocado de "04 — Panda mordendo bambu" para **"Desenho 4"**.

## 15. Diretrizes de geração de imagem (padrão fixo do processo)

**Princípio:** em vez de adaptar a ingestão a cada imagem, a arte deve ser gerada já seguindo regras que garantam uma ingestão limpa. Abaixo, o padrão a manter sempre.

### Prompt-base FINAL (validado — funciona em 25×30)

Versão de Erik, com 3 correções sobre a minha proposta anterior: removi a instrução de "não desenhar dedinhos" (desnecessária — o modelo já simplifica bem só com o "target grid size"), adicionei rosa nas patas explicitamente em Proportions (estava faltando), e deixei o bambu livre em vez de prescrever "segmentos grossos" (estava distorcendo o resultado).

```
Kawaii pixel art illustration of [SUBJECT + ACTION/SCENE], sitting pose,
front-facing.

Style: flat solid color blocks only — no gradients, no soft shading, no
anti-aliasing. Clean hard pixel edges, like a perler bead / cross-stitch
pattern. Bold thick black outline around the entire silhouette.

Target grid size: design this illustration to read clearly when reduced
to a LOW-RESOLUTION grid of approximately 25 columns × 30 rows. This
means: use large, simple, clearly separated color regions.

Symmetry: some illustration details must be perfectly symmetric —
matching ears, matching eye patches, matching cheek blush size and
shape, matching paws and others.

Color limit: use a small flat color palette (around 6-7 distinct solid
colors total, including black and white). Avoid near-duplicate shades of
the same color — reuse the same exact color consistently for the same
material across the whole illustration.

Proportions: rounded kawaii chibi proportions — big round head, small
body, large black eye patches with a tiny white eye highlight, soft pink
blush on the cheeks and paws.

Background: plain solid white, no texture, no shadow, no vignette,
nothing else in the scene besides the subject.

Format: vector-flat digital illustration / pixel art style. NOT
photorealistic, NOT 3D render, NOT painterly.

Use the reference images as inspiration, don't copy.
```

**Resultado do teste (Desenho 4 — panda, versão final):** legível e reconhecível em 25×30 — orelhas, olhos, bochechas, patas com toque de rosa, bambu como linha diagonal simples. 5 cores limpas. Este é o padrão oficial a partir de agora.

### Histórico de calibração (para referência futura)
| Tentativa | Resultado | Grade praticável |
|---|---|---|
| V1 (sem pedido de detalhe) | Simples demais, formas vagas | — |
| V2 (com "high detail level") | Bonito, mas denso (dedinhos individuais, segmentos finos) | ~60×60 — impraticável |
| V3 (calibrado pra 25×30, 1ª versão) | Sem rosa na pata, olho estranho, bambu distorcido | — |
| **V4 (calibrado + correções de Erik)** | **Legível e fiel em 25×30** ✅ | **25×30 — padrão oficial** |

### Referências de imagem — obrigatório incluir no prompt

**Regra fixa do processo:** toda geração deve incluir imagens de referência anexadas ao prompt (não só texto). Isso é responsabilidade de quem gera a imagem (Erik/esposa) — registrado aqui para manter o padrão entre gerações futuras.

Referências validadas (usadas na geração do Desenho 4 — panda):
- Referência de traço/contorno em grade (estilo grid-art preto e branco)
- Referência de paleta/proporção kawaii (fundo rosa, contorno preto grosso, blush nas bochechas)

### Checklist antes de aceitar uma ilustração pra ingestão
- [ ] Fundo branco liso, sem textura
- [ ] Contorno preto único e fechado ao redor de toda a silhueta
- [ ] No máximo 7 cores distintas — sem tons quase-duplicados
- [ ] Sem gradiente/sombreado suave (blocos de cor sólidos)
- [ ] Cena/ação presente (nunca elemento isolado — regra da seção 11)
- [ ] Referências de estilo anexadas no prompt de geração

## 16. Ingestão — correção do algoritmo de fusão de cores

**Problema identificado:** a primeira versão do `ingest.py` tratava tons quase-idênticos (ex: 3 variações de cinza-escuro, ou rosa claro vs. bege) como cores separadas, gerando mais códigos do que o necessário.

**Causa:** o agrupamento por frequência sozinho não diferencia "ruído de antialiasing perto do contorno" de "cor genuinamente diferente".

**Correção aplicada:** o algoritmo agora separa cores **neutras** (preto/cinza/branco) de cores **cromáticas** (rosa, verde, bege...) antes de decidir o que mesclar:
- Duas cores neutras próximas → mesclam entre si (correto: normalmente é ruído de borda)
- Duas cores cromáticas próximas → só mesclam se muito parecidas (limiar mais rígido)
- Uma neutra e uma cromática → **nunca mesclam entre si** (evita rosa virar bege, por exemplo)

**Resultado no teste:** o panda foi de 10 cores detectadas (com duplicatas) para exatamente **7 cores limpas**, todas visualmente distintas — preto, branco, rosa, bege, e 3 tons de verde do bambu (esses 3 são intencionais na arte original, não duplicata).

**Parâmetro ajustável:** `max_colors=7` agora é o padrão de `image_to_canvas()`, alinhado ao limite definido no prompt.

---

## 17. Calibração final — resolução e algoritmo de ingestão

### Resolução oficial: 42×55 células (medição direta de produto real)
Erik comprou um produto real no Etsy ("Pixel Cats Color Pages") para servir de gabarito de calibração. Medi a grade programaticamente a partir do PDF entregue (detecção de linhas de grade por análise de pixel, não estimativa visual): **42 colunas × 55 linhas** (~2.310 células), confirmado por dois métodos independentes (espaçamento de linha detectado e largura total da moldura dividida pelo espaçamento). Isso substitui a estimativa anterior de 36×44.

**Cores:** variam por ilustração dentro do mesmo produto — observei de 5 a 12 cores dependendo da complexidade de cada desenho, não é um número fixo. Ajustar `max_colors` caso a caso, não travar num valor único.

### Causa raiz do problema de definição (resolvida)
O algoritmo de ingestão amostrava a **moda de toda a área** de cada célula — isso borra detalhes pequenos (ex: cada dedinho da pata, que ocupa só 1-2 pixels na grade final). Comparação direta contra um downscale nearest-neighbor puro (sem processamento de cor) confirmou que o "rabinho" estranho na orelha é fiel à arte original (não é bug), mas que a definição das patas estava sendo perdida pelo método de amostragem.

**Correção 1:** trocado para amostragem do **pixel central** de cada célula (nearest-neighbor clássico) em vez de moda de área.

**Bug encontrado na correção 1:** pixel único central é vulnerável a *aliasing* — quando a grade de amostragem coincide com um padrão repetitivo no fundo da imagem de referência (ex: linhas finas de papel quadriculado em imagens de estilo/inspiração), uma linha inteira da grade final "trava" na cor da linha, criando uma faixa sólida falsa que não existe na arte original. Confirmado comparando input real vs. output.

**Correção 2 (atual):** amostragem de **9 pontos espalhados por célula** (grade 3×3 esparsa), pegando a moda entre eles — resistente a ruído de linha isolada, sem voltar a borrar detalhe fino. Validado nos dois sentidos: manteve definição de pata no panda, eliminou a faixa sólida no teste com imagem de fundo quadriculado.

### Padrão oficial a partir de agora
- Grade: **42×55** (medido de produto real, não estimado)
- Cores: variável, 5 a 12 conforme a ilustração
- Amostragem: moda de 9 pontos espalhados por célula (grade 3×3)
- Tamanho de exportação: 2362×3189px (200×270mm) — confirmado como padrão em todos os produtos de referência

### Editor (`editor.html`) — melhorias adicionadas
- **Conta-gotas** (grade ou imagem de referência) — clique pra pegar cor exata
- **Fusão automática por hex duplicado** — editar uma cor pro mesmo hex de outra já existente funde as duas
- **Desfazer (Ctrl+Z)** — histórico de estados antes de qualquer ação destrutiva
- Sincronizado com a mesma correção de amostragem (9 pontos) do `ingest.py`
- Grade padrão atualizada para 42×55, até 10 cores

## 18. Grade variável, não fixa (correção importante)
Medição de mais duas páginas do produto real revelou que a grade **não é fixa** — uma ficou em ~41×51 (perto do que já tínhamos), outra em ~29×36 (bem menor). Ou seja, cada ilustração tem sua própria resolução, provavelmente proporcional à complexidade dela. Deixamos de mirar "o número certo" único — a resolução deve se adaptar por ilustração.

## 19. Achado principal: a causa raiz é o tipo de imagem-fonte, não (só) grade/algoritmo
Erik notou que subir de 36×44 para 42×55 não melhorou o panda de forma clara — em alguns detalhes até piorou. Isso levantou a pergunta certa: talvez o teto de qualidade não esteja na grade nem no algoritmo de ingestão, e sim na **imagem de entrada**.

**Confirmado com medição direta:** analisando os valores de pixel numa transição de borda da arte gerada por IA (branco → preto), existe um pixel intermediário com valor 101 (cinza) entre os dois extremos — prova de **antialiasing real** (gradiente suave de 1-2 pixels). Produtos profissionais como o comprado no Etsy têm acabamento perfeitamente limpo, sem esse pixel de transição — característica de **arte vetorial** (Illustrator/Procreate, formas fechadas com contorno matematicamente exato) ou **pixel art nativa** (desenhada célula por célula direto num editor tipo Aseprite), não de imagem raster gerada por IA.

**Implicação:** nenhum ajuste de grade ou algoritmo de amostragem remove um teto de qualidade que já está na origem — mais células só significam mais chances de amostrar um pixel de transição ambíguo.

### Correção aplicada: pré-achatamento antes da amostragem
A imagem inteira agora é **pré-achatada para poucas cores em alta resolução antes** de ser dividida em células — isso colapsa os pixels de transição antialiasada para o lado mais próximo (a cor sólida real), resolvendo o problema na origem, não só na amostragem.

- Testado com 16, 32, 48 e 64 cores de pré-achatamento — **64 foi o ponto certo**: poucas o bastante pra eliminar a ambiguidade de borda, muitas o bastante pra não perder nuance real (rosa das bochechas, os dois tons de verde do bambu).
- Com 16, o algoritmo perdeu o rosa inteiro e confundiu a cor do bambu — "achatar mais" não é sempre melhor.
- Resultado final: bochechas rosa de volta, bambu com verde limpo, patas com contorno arredondado nítido — melhor resultado da calibração até agora.

**Padrão atualizado:** `preflatten_colors=64` como default em `image_to_canvas()`, aplicado também no `editor.html`.

### Questão em aberto para produção futura
Se o teto real de qualidade está no tipo de fonte (raster com antialiasing vs. vetorial/pixel nativo), vale considerar, além de seguir otimizando a ingestão: (a) pedir explicitamente output sem antialiasing na geração, se o modelo permitir; ou (b) usar o editor manual com a arte de IA só como camada de referência visual, pintando por cima — o que dá acabamento perfeito por construção, já que célula pintada manualmente nunca tem ambiguidade de borda.

## 20. Vetorização como etapa oficial do pipeline (implementada)

Testamos a resposta direta pra causa raiz da seção 19: em vez de só compensar o antialiasing (pré-achatamento), **eliminá-lo de vez** convertendo a arte em vetor antes de qualquer processamento.

### Como funciona
1. PNG gerado pela IA (raster, com antialiasing) → vetorizado com `vtracer` (formas fechadas, cores 100% sólidas, contorno matematicamente exato)
2. Vetor renderizado de volta em PNG de alta resolução com `cairosvg`
3. Esse PNG "limpo" segue pro pipeline normal (`image_to_canvas`)

### Resultado
Qualidade no mesmo patamar do pré-achatamento (ou levemente superior) — patas com dedinhos nítidos, cores sólidas, contornos limpos. A diferença é que aqui a limpeza é **por construção**, não por aproximação estatística.

### Implementação
Nova função `vectorize_source()` em `ingest.py`:
```python
from ingest import vectorize_source, image_to_canvas

vectorize_source("panda_ia.png", "panda_vetorizado.png")
canvas, palette, order = image_to_canvas("panda_vetorizado.png", cols=42, rows=55)
```
Requer `pip install vtracer cairosvg` (ambos instalados e testados no ambiente).

### Bônus não previsto
Como o resultado intermediário é um SVG de verdade (não só um PNG mais limpo), isso abre a possibilidade de usar **vetor no material de impressão final** em vez de raster — evita qualquer serrilhado em tamanhos de impressão maiores. Vale explorar mais pra frente, não é prioridade agora.

### Recomendação de processo
Vetorização entra como **etapa padrão** entre "arte gerada pela IA" e "ingestão" — não substitui o pré-achatamento (que continua como camada de proteção), mas ataca o problema antes dele precisar existir.

## 21. Fluxo oficial de produção (consolidado)

```
1. IA gera a ilustração (ChatGPT/Magnific, prompt calibrado — seção 15)
2. Editor (editor.html): detecção automática + correção manual célula a célula
   → exporta PNG já 100% limpo (sem antialiasing, por construção — fillRect)
3. Vetorização (vectorize_source) — CONDICIONAL:
   - Pular se a arte já veio do editor (já está limpa)
   - Rodar se for ingerir direto o PNG cru da IA, sem passar pelo editor antes
4. Ingestão (image_to_canvas) — grade + paleta + pré-achatamento como camada extra de segurança
5. Geração de mistério, legenda, gabarito, PDFs (pixelkit.py)
```

Validado de ponta a ponta com o Desenho 4 (panda) por esse caminho exato: IA → editor (correção manual) → PNG exportado → ingestão direta → PDFs. Resultado com mais nuance capturada até agora (9 cores, incluindo os aneizinhos dos nós do bambu e o tom de destaque nas folhas).

---

## Pontos para discutirmos juntos
