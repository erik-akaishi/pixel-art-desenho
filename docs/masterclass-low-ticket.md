# Masterclass: Como Criar um Low Ticket de R$300K
### Anotações compiladas para estudo

---

## 1. O que é Low Ticket

- **Infoprodutos baratos**, usados como **estratégia de funil** (fazem o cliente "abrir a carteira" e entram no topo de uma esteira de ofertas maiores).
- **Consumo rápido**: geralmente ferramentas prontas — planilhas, manuais, guias, ebooks, bibliotecas de arquivos organizados.
- Resolvem **dores latentes/chatas** de forma fácil e imediata.

## 2. Por que "Low Ticket" faz sentido como modelo

| Vantagem | Descrição |
|---|---|
| Escalabilidade | Alta — não depende de atendimento 1:1 |
| Automação | Vende 24h/dia, 7 dias por semana |
| Custo | Sem custo de produto (é digital, réplica infinita) |
| Propriedade | Você é **dono**, não afiliado — a ideia é o ativo |
| Operação | Baixo estresse comparado a produtos de ticket alto |
| Contexto de mercado | É uma tendência atual de consumo |

---

## 3. Etapa 1 — O "Segredo": achar produtos que já validam

**Premissa:** você não precisa inventar do zero. Produtos low ticket lucrativos **já existem e já estão vendendo** — o trabalho é *achá-los*.

### Como achar
Toda plataforma de anúncios é obrigada a expor publicamente os anúncios ativos (transparência de propaganda):

- **Meta** → Biblioteca de Anúncios (Ad Library)
- **Google** → Google Ads Transparency Center
- **TikTok** → TikTok Ad Library

Existem serviços pagos (~R$497,90/mês) que só fazem uma coisa: pesquisar essas bibliotecas com as **keywords certas**. Ou seja, o valor está no *conjunto de palavras-chave*, não em tecnologia proprietária — algo replicável manualmente ou com um agente/skill de IA.

---

## 4. Validação da oferta (o filtro antes de modelar)

### 4.1 Três validações macro
1. O funil é de **low ticket + infoproduto**?
2. Está **vendendo de fato** (não é só um anúncio isolado sem tração)?
3. Como é a **oferta**?

### 4.2 Ao entrar no funil, identifique o formato
- Quiz
- Página de vendas
- VSL (Video Sales Letter)

### 4.3 Sinais de tração a analisar
- Quantidade de anúncios rodando simultaneamente
- Há quanto tempo os anúncios estão no ar
- Uso de extensões/ferramentas de espionagem (ex: AdSpyer, Ad Library Cloud) para checar histórico

### 4.4 A oferta entrega...
- Resolução de um problema **latente**?
- Resolução **rápida, tangível e empacotada**?
- Resolução **fácil**?

### ✅ Checklist final de validação
- [ ] É um funil de low ticket
- [ ] Roda anúncio há mais de 15–30 dias
- [ ] Roda mais de 20 anúncios simultâneos
- [ ] Resolve uma dor latente
- [ ] Resolve de forma fácil
- [ ] Resolve de forma rápida

> Se marcar todos → é um produto validado pelo mercado, seguro para servir de referência/modelagem.

---

## 5. Modelagem — a fase de execução com IA

### 5.1 Modelagem de Produto
- GPT/Claude com **prompts e skills específicas** fazem praticamente todo o trabalho de criação do material.
- Até o **cadastro do produto nas plataformas** de venda pode ser feito por extensões/agentes de IA (ex: extensão do Claude no navegador).

### 5.2 Modelagem de Funil
- Caminho mais simples: modelar a **página de vendas**.
- Fluxo sugerido:
  1. Prompt em Claude/Lovable/Codex (ou ferramenta similar de geração de site/app)
  2. Inspirar-se em páginas de concorrentes validados → print de tela como referência visual
  3. Stack técnica sugerida: **Supabase + GitHub + Vercel**

### 5.3 Modelagem de Criativos
- ChatGPT (geração de imagem) resolve praticamente tudo, desde que você tenha:
  - Referências visuais boas
  - Prompts corretos e específicos

---

## 6. Objeção de preço / garantia (usada na oferta da própria masterclass)

Argumento de venda: acesso a 100% do sistema + reembolso garantido em **7 dias**, amparado pelo **Código de Defesa do Consumidor**.

> *Nota para nós: isso é uma técnica de redução de risco percebido (garantia incondicional), útil como referência de copy — não é sobre o conteúdo do método em si.*

---

## 7. Exemplo de prompt de "entregável" (produto digital)

As anotações originais desse prompt vieram com bastante ruído de transcrição/OCR. Reconstruí abaixo a versão que parece ser a intenção original — vale revisar comigo antes de usar, porque fiz interpretação em alguns trechos:

> Atue como especialista no tema, designer editorial e ilustrador profissional. Crie um material digital premium chamado **"GUIA DA DIETA — 101 RECEITAS"**, no padrão de uma apostila educativa ilustrada, em páginas A4 verticais, prontas para impressão e posteriormente reunidas em PDF.
>
> Analise automaticamente o nicho do produto, o público-alvo, a finalidade, o nível de conhecimento e o estilo visual mais adequado. Adapte cores, linguagem e gráficos ao tema: use um visual colorido e acolhedor se o material for infantil, e um visual mais sóbrio e profissional quando for destinado a adultos.
>
> Crie uma capa chamativa, orientações de uso, e o sumário do conteúdo principal. Cada atividade, técnica, dinâmica ou receita deve ocupar uma página completa e conter: número, título, explicação curta, objetivo, materiais necessários, instruções em etapas, atividade prática, dica profissional, variação ou adaptação, e habilidades trabalhadas.
>
> Mantenha uma identidade visual consistente em todas as páginas: fundo claro, caixas coloridas, títulos destacados, ilustrações profissionais, boa hierarquia visual, margens seguras e textos fáceis de ler. Varie os formatos das atividades entre cartões, sequências, trilhas, tabuleiros, histórias, desafios, recorte e colagem, fichas e exercícios práticos — evitando páginas repetitivas.
>
> Todo o conteúdo deve ser original, realmente aplicável e esteticamente cuidado. Revise concordância, numeração, instruções e a relação entre imagens e palavras. Evite textos cortados, letras deformadas, imagens incoerentes, atividades duplicadas ou layouts amadores.
>
> Gere cada página como uma imagem final em alta resolução (não precisa ser editável). Comece criando somente a capa; depois gere o sumário; em seguida produza o conteúdo em blocos de 10 páginas, mantendo a identidade visual e a numeração consistentes.

**Estrutura genérica por trás do prompt** (útil pra reaplicar em outros nichos):
1. Papel/persona do especialista + estilo visual
2. Nome do produto + formato final (apostila → PDF)
3. Análise automática de nicho/público/tom
4. Estrutura fixa por página (o "molde" que se repete)
5. Regras de consistência visual
6. Regras de qualidade/anti-erro
7. Ordem de geração (capa → sumário → blocos de conteúdo)

---

## 8. Ferramenta citada: "Ads Keyword Miner"

- Descrita como uma **skill em Markdown**.
- Função: gerar e consultar **prompts/queries prontas** para encontrar anúncios de infoprodutos e low ticket na **Meta Ad Library**, nos mercados **PT / EN / ES**, organizadas em **clusters** (temas/nichos).
- Essencialmente automatiza a Etapa 1 (achar produtos validados) descrita acima.

---

## 9. Mapa geral do processo (resumo visual)

```
1. GARIMPAR    → Ad Libraries (Meta/Google/TikTok) + keywords certas
2. VALIDAR     → Checklist (tempo no ar, nº de anúncios, dor latente/fácil/rápida)
3. MODELAR     → Produto (IA) + Funil (página de vendas) + Criativos (IA)
4. PUBLICAR    → Cadastro nas plataformas (agente/extensão de IA)
5. VENDER      → Funil automatizado 24/7
```

---

## 10. Plataformas de venda (gateways de infoproduto)

Todas essas plataformas fazem basicamente o mesmo papel: hospedam o checkout, processam o pagamento (cartão/pix/boleto), entregam o produto ao comprador, cuidam de reembolso/chargeback, e (em graus diferentes) oferecem marketplace de afiliados. A diferença está em taxa, velocidade de saque, burocracia de cadastro e o quão pronta cada uma é pra low ticket especificamente.

> ⚠️ Taxas de gateway mudam com frequência e por faixa de faturamento — os números abaixo são a referência mais recente que encontrei, mas **confirme direto no site oficial de cada uma antes de decidir**, porque encontrei alguma divergência entre fontes (sinal de que elas mesmas promovem mudanças de tabela com frequência).

### Comparativo

| Plataforma | Taxa por venda | Ponto forte | Ponto fraco | Saque |
|---|---|---|---|---|
| **Hotmart** | ~9,9%–14,9% + R$1 | Maior marketplace de afiliados do Brasil, ecossistema mais completo (área de membros, integrações) | Taxa mais alta, plataforma mais "pesada"/complexa, suporte mais lento por ser gigante | Padrão do mercado, sem antecipação facilitada |
| **Kiwify** | ~8,99% + R$2,49 (varia por plano) | Simplicidade — sobe produto em <1h, checkout limpo, suporte mais ágil | Marketplace de afiliados menor que Hotmart | Um dos prazos de liberação mais rápidos (~15 dias) |
| **Ticto** | 6,99% + R$2,49 — e **0% de taxa em produtos até R$50** (programa "Turbo Low Ticket") | Isenção de taxa específica pra low ticket, checkout otimizado (Bolt), boa nota no Reclame Aqui | Marca menos conhecida (pode gerar desconfiança em quem não conhece), afiliação por convite (rede menor) | 14–30 dias, com opção de antecipação paga |
| **Cakto** | ~8,5% + R$0,50 (ou 0% no Pix, conforme forma de pagamento) | Cadastro simples (só CPF/CNPJ + conta bancária + 18 anos), sem limite de saque pra CPF, plataforma nova e ágil | Menos histórico de mercado, menos robustez de afiliados | Cartão até 15 dias, boleto 1 dia, Pix instantâneo |
| **Eduzz** | 4,9% + R$1 (venda direta) / 8,9% + R$1 (via afiliado) | Taxa direta mais baixa do grupo, ecossistema mais amplo (CRM, landing pages inclusos) | Interface considerada menos intuitiva que Kiwify/Cakto | Padrão do mercado |
| **Monetizze** | 7,99% + R$1,50 | Interface simples, bom programa de afiliados | Menos foco em recursos avançados de funil | Padrão do mercado |

### O que pesa mais pro seu caso específico (low ticket)

- **Ticto** se destaca por ter um programa desenhado exatamente pro seu modelo: **0% de taxa em produtos até R$50**. Se seu ticket de entrada for nessa faixa (o que é comum em low ticket), isso pode compensar a marca ser menos conhecida.
- **Cakto** compensa em burocracia mínima de entrada (CPF já basta, sem limite de saque) — bom pra validar rápido sem se preocupar com CNPJ logo de cara.
- **Hotmart** faz mais sentido se, no futuro, você quiser puxar tráfego via **rede de afiliados** (pessoas vendendo por você em troca de comissão) — é onde a rede é maior e mais madura.
- Nenhuma delas resolve a parte fiscal por você: mesmo a mais simples de cadastrar (ex: Cakto) espera que **você** emita a nota fiscal de cada venda — a plataforma só processa o pagamento, a responsabilidade tributária continua sendo sua (reforça o ponto que conversamos sobre CNPJ/regime).

### Sugestão de exploração prática
1. Abrir conta em **2 plataformas** pra comparar na prática (ex: Ticto pelo Turbo Low Ticket + Kiwify ou Cakto pela simplicidade) — nenhuma cobra mensalidade pra ter conta, só taxa por venda.
2. Rodar um produto de teste em ambas com o mesmo preço e comparar: taxa de conversão do checkout, tempo até o dinheiro cair, suporte quando precisar.
3. Decidir a definitiva só depois de ver conversão real — no low ticket, 1–2 pontos percentuais de taxa importam menos do que a taxa de conversão do checkout.

---

## 11. Direção escolhida: produtos low ticket com base em Design

Decisão tomada: em vez de nichos de conteúdo (dieta, finanças etc.), o produto nasce da **especialidade em design** (Erik + esposa/sócia), independente de o público-alvo final ser da área de design ou não.

### Confirmação de mercado
- Já existem lojas brasileiras rodando faturamento consistente só com papelaria digital pra GoodNotes/Notability/tablets (adesivos, capas de planner, cartelas temáticas).
- No mercado internacional (Etsy), planners digitais, templates Canva, printables e pacotes de prompts aparecem como categorias de **demanda consistente e forte em 2026**; planners são tratados como categoria "evergreen" (as pessoas reiniciam metas o ano todo).
- Nicho de **casamento/eventos** aparece com destaque especial — alta disposição a pagar por papelaria editável (convite, cardápio, rótulo).

### Ideias mapeadas

| Ideia | Formato | Por que combina com vocês |
|---|---|---|
| Papelaria digital para planner (adesivos, capas, cartelas) | PNG/PDF cortável | Ilustração/UI decorativo, produção rápida em lote, mercado BR já validado |
| Templates de planner (semanal, hábitos, financeiro, metas) | PDF preenchível/digital | Cruza design editorial com UX de fluxo — hierarquia de informação |
| Kits de social media (templates Canva feed/stories/destaques) | Canva template | Mesmo raciocínio de sistema visual já aplicado a clientes B2B, embalado pra pessoa física |
| Pacotes de prompts visuais (curadoria por estética) | PDF/planilha | Cruza vivência com IA generativa + curadoria estética |
| Templates de landing page (Framer/Notion por segmento) | Template clonável | O ofício mais técnico de vocês (UX/UI + DEX) — maior ticket dentro do low ticket |
| Desenhos para colorir (adulto/infantil, por tema) | PDF printable | Produção escalável com IA + revisão de design, nicho evergreen |
| Mini kits de identidade visual "faça você mesmo" | Canva/Figma template | Aproveita a especialidade em branding, para autônomos/pequenos negócios |
| Papelaria para eventos (convite, cardápio, rótulo editável) | Canva/PDF editável | Nicho "wedding/eventos" com forte disposição a pagar |
| Ícones/ilustrações em pacotes (professores, criadores de conteúdo) | PNG/SVG bundle | "Matéria-prima de design" — baixa complexidade, alta reutilização |

**Vantagem identificada:** os produtos validados nesse recorte são 100% estético/de sistema visual, não de conteúdo educacional — parte que a maioria dos infoprodutores de outros nichos precisa terceirizar, e que pra vocês é a parte fácil.

### Keywords de garimpo (pra rodar na Meta Ad Library agora)

Use estas como ponto de partida — testar em PT (Brasil) e, se quiser referência internacional de precificação/formato, também em EN:

**Papelaria digital / planner**
- planner digital
- adesivos digitais planner
- papelaria digital GoodNotes
- cartela de adesivos digital

**Templates sociais e identidade**
- template canva feed
- kit identidade visual pronto
- template stories canva
- logo editável canva

**Landing page / templates de site**
- template landing page notion
- template site framer
- landing page pronta para vender

**Colorir / printables**
- desenho para colorir pdf
- livro de colorir digital
- printable para imprimir

**Eventos**
- convite digital editável
- papelaria casamento editável
- convite chá de bebê canva

**Prompts visuais**
- pacote de prompts imagens
- prompts para IA design

> Próximo passo: pegar 3–5 dessas keywords, rodar na Ad Library, e aplicar o checklist da seção 4 em cima do que aparecer (tempo no ar, nº de anúncios, dor latente/fácil/rápida).

---

## 12. Garimpo — Rodada 1 (resultados reais)

### Convites digitais editáveis
- Busca "convites digitais editáveis" no Ad Library (Brasil) retornou **60+ anúncios ativos** → nicho saturado, confirmado oceano vermelho pra venda direta de template.
- Modelos de negócio identificados dentro do nicho:
  - Venda direta de template ao consumidor final (noiva/mãe) — ex: Fer Lopes (R$67, ~5 ads), Canva Para Noivas (6 convites por R$47)
  - Megapack pra revenda (B2B2C) — ex: Infinity Express Digital (800+ opções), DesignerClube (220 convites por R$9,90)
  - Minicurso "aprenda a vender convites" — ex: Seu Convite Criativo (+3.000 alunas), Canva Para Noivas — aqui o produto é educação, não design puro
- **Achado relevante:** Joana Cabral ("Arquivos que Encantam") empacota revistinha de colorir + convites editáveis no mesmo Kit Lembrancinhas — sinal de que bundling entre categorias de papelaria/design já é praticado no mercado.
- Conclusão: deprioritizar convites como produto carro-chefe. Guardar a ideia de bundle (colorir + papelaria de festa) pra uma fase 2.

### Pixel art / desenho para colorir
- O único concorrente encontrado antes (365 Pixel Art) tinha ~7 anúncios rodando por até 1 mês — sinal real de teste, mas os anúncios sumiram na nova checagem (ambíguo: pode ser fim de orçamento, baixo desempenho ou pausa).
- Busca por "pixel art" não retornou concorrentes diretos — mas busca por "desenho para colorir" retorna majoritariamente estilo convencional (não pixel art), com sinais de potencial segundo leitura de campo.
- Conclusão: manter a categoria "desenho para colorir" no radar de forma mais ampla (não apostar tudo no recorte "pixel art" especificamente); precisa de mais garimpo pra achar um ângulo de diferenciação claro.

### Atividades pedagógicas / educação infantil
- Pesquisa de mercado (fora do Ad Library) confirma nicho **maduro e validado**, com players brasileiros ativos há anos: apostilas por nível/faixa etária com entrega automática por e-mail (800+ famílias atendidas), coleções de 100 apostilas alinhadas à BNCC (currículo oficial — forte sinal de confiança), apostilas com 530+ atividades (coordenação motora, letras, números, formas).
- Boa parte do material existente tem qualidade de design amadora — hierarquia visual fraca, layout inconsistente — brecha clara pra entrada com padrão profissional.
- Ainda falta rodar o garimpo direto no Ad Library pra aplicar o checklist completo (nº de anúncios ativos, tempo no ar).

### Checklist atualizado

| Critério | Convites | Colorir (geral) | Atividades pedagógicas |
|---|---|---|---|
| Funil low ticket + infoproduto | ✅ | ✅ | ✅ (confirmar formato de venda) |
| 20+ anúncios ativos | ✅ **60+** (saturado) | A confirmar | A confirmar no Ad Library |
| Dor latente | Alta (evento com prazo) | Média-alta | Alta (dupla: professor + pai) |
| Fácil/rápido de entregar | ✅ | ✅ | ✅ |
| Concorrência | Alta — saturado | Média | Média — mercado maduro, mas brecha de qualidade |

## 13. Priorização atualizada

1. 🥇 **Atividades pedagógicas / educação infantil** — demanda dupla validada, brecha clara de qualidade de design frente aos concorrentes atuais
2. 🥈 **Desenho para colorir (geral)** — potencial real, precisa de ângulo de diferenciação melhor definido
3. 🥉 **Convites digitais** — deprioritizado como carro-chefe (saturado); ideia de bundle guardada pra fase 2

### Próximas keywords de garimpo (atividades pedagógicas)
- atividades educação infantil
- apostila alfabetização
- material pedagógico professora
- atividades coordenação motora
- cruzadinha infantil
- ligar pontos atividade
- apostila BNCC
- kit atividades sala de aula
- roteiro de aula pronto

---

## 14. Garimpo — Rodada 2: Pixel Art (reavaliação)

### Educlub — validação pedagógica
O portal Educlub (biblioteca de atividades educativas por série/matéria) cataloga pixel art oficialmente como atividade pedagógica, ligando a técnica a: coordenação motora fina, percepção espacial, **conceitos matemáticos** (contagem, sequência, padrões) e introdução a conceitos de imagem digital/design gráfico. Isso conecta diretamente a frente "colorir" com a frente "atividades pedagógicas" — não são duas ideias separadas, pixel art pode ser o produto de entrada dentro da frente pedagógica.

### Etsy — validação de escala internacional
- Busca "pixel art pdf" retorna **mais de 1.000 resultados relevantes**.
- Produtos com **60 a 1.100 avaliações** cada — sinal de venda recorrente real, não anúncio de teste isolado.
- Formato vencedor identificado: **"pixel art mistério" / colorir por número-código** (a imagem só se revela enquanto a pessoa pinta) — usado tanto em versão infantil quanto com framing de "alívio de estresse" pra adultos, confirmando apelo duplo de público.
- Faixa de preço: pacotes de colorir entre €2,46–€7,41 (com âncora de desconto 20–70%); ferramentas pra criador (pincéis Procreate) até €26,94.
- ⚠️ **Risco de direito autoral:** vários dos mais vendidos usam personagens licenciados (Pokémon, animes). Caminho seguro: usar o mecanismo de mistério/código com temas 100% originais.
- **Canal alternativo identificado:** Etsy funciona via busca orgânica internacional, sem depender de anúncio pra começar — um segundo canal de teste em paralelo ao funil brasileiro via Meta Ads.

## 15. Priorização final (atualizada)

1. 🥇 **Pixel art / colorir por código-mistério** — validação dupla (pedagógica + comercial em escala), maior potencial do lote
2. 🥈 **Atividades pedagógicas (mais amplo)** — pixel art pode nascer como primeiro produto dentro dessa frente
3. 🥉 **Convites digitais** — deprioritizado, ideia de bundle guardada pra fase 2

---

## Pontos para discutirmos juntos

- O método inteiro depende de **clonar/modelar ofertas validadas** — vale a pena mapear onde fica a linha entre "modelagem" (inspiração estrutural) e cópia direta de conteúdo/copy de terceiros, inclusive por segurança jurídica.
- A "Ads Keyword Miner" parece ser a peça mais replicável rapidamente — dá pra prototipar como skill própria.
- O prompt do "Guia da Dieta" é essencialmente um **template de produto editorial em lote** — o mesmo esqueleto serve pra qualquer nicho (dieta, organização financeira, produtividade, etc.), trocando só o tema.
- Vale pensar se isso é algo pra rodar como projeto pessoal separado do Akaishi, ou se há alguma aplicação como **produto de entrada (lead magnet pago)** para o próprio estúdio.
