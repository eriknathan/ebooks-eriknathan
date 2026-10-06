# Design system — e-books de estudo (HTML + PDF)

Referência do padrão visual dos e-books gerados a partir de Markdown (todos, exceto o Well-Architected, que ainda tem HTML próprio). A implementação está em [`ebook-template.html`](ebook-template.html): o [`ferramentas/gerar_ebook.py`](../ferramentas/gerar_ebook.py) lê dali o CSS e as fontes e monta capa, sumário, capítulos e síntese com a mesma estrutura dos moldes. Este documento explica **o que** cada peça é e **quando** usar. Se os dois divergirem, vale o template.

## Princípios

1. **Papel primeiro.** O e-book é pensado para A4 impresso. A tela imita a folha (papel branco sobre fundo cinza).
2. **Uma cor de destaque só.** O laranja marca estrutura (barra da capa, faixas do sumário, bordas de componentes), nunca texto corrido.
3. **Mono para estrutura, sans para leitura.** Rótulos, números, faixas e códigos usam IBM Plex Mono. O texto usa IBM Plex Sans.
4. **Conteúdo decide o componente.** Texto corrido fica como parágrafo. Componente só entra quando o formato do conteúdo pede (ver [Componentes](#componentes)).
5. **Economia de tinta na impressão.** Fundos escuros viram contorno no PDF.

---

## Cores

### Tokens editáveis (por e-book)

Só estes podem mudar, e só quando o e-book pedir outra cor de destaque.

| Token | Valor padrão | Uso | Contraste |
| --- | --- | --- | --- |
| `--accent` | `#ff9900` | Barra da capa, faixas do sumário, bordas de cards, callouts, flashcards, timeline | 2,1:1 — **só decorativo, nunca texto** |
| `--accent-ink` | `#8a4b00` | Texto em destaque: números do sumário, kicker, letras das alternativas, `+`/`−` | 6,8:1 sobre branco |
| `--accent-soft` | `#fff3de` | Fundo de callout, chip em destaque, marcador da lista numerada | — |
| `--accent-line` | `#e9b463` | Borda de callout e chip em destaque | — |
| `--ink` | `#1b2d3b` | Títulos, barras escuras, cabeçalho de tabela, rótulo de seção | 14,1:1 sobre branco |

Ao trocar o destaque, mantenha `--accent-ink` com pelo menos 4,5:1 sobre `#ffffff` e sobre `--accent-soft`.

### Tokens fixos

| Token | Valor | Uso | Contraste |
| --- | --- | --- | --- |
| `--paper` | `#ffffff` | Folha | — |
| `--canvas` | `#e7ecef` | Fundo da tela atrás da folha | — |
| `--text` | `#263643` | Texto corrido | 12,4:1 |
| `--muted` | `#52616d` | Subtítulos, descrições, tópicos do sumário, rodapé | 6,4:1 |
| `--line` | `#cbd5db` | Bordas finas, pontilhado do sumário, divisórias | — |
| `--surface` | `#f2f6f7` | Faixas do sumário, blockquote, resposta de flashcard, `code` | — |
| `--teal` | `#086b70` | Links na tela, site na linha de autoria, rótulo "Resposta" | 6,3:1 |

---

## Tipografia

| Família | Token | Pesos | Uso |
| --- | --- | --- | --- |
| IBM Plex Sans | `--sans` | 400, 500, 600, 700 | Corpo, títulos |
| IBM Plex Mono | `--mono` | 400, 500, 600, 700 | Código da capa, rótulos, números, faixas, chips, `code` |

As duas ficam em [`fontes/`](fontes/) (subconjuntos latin e latin-ext, licença OFL). O `gerar_ebook.py` embute no HTML, em base64, só as faces que o texto usa, então o e-book abre e o PDF sai igual sem rede. Caracteres que o Plex não tem (setas, `≥`, desenhos de caixa) usam as alternativas da pilha (`-apple-system`, `Segoe UI`, `Arial` / `Menlo`, `Consolas`), que variam por sistema operacional: por isso os PDFs são gerados sempre no mesmo sistema (hoje, macOS).

### Escala

| Elemento | Tela | PDF | Detalhe |
| --- | --- | --- | --- |
| Base (`body`) | 16px / 1,65 | 9,5pt / 1,48 | — |
| Selo de nível (`.cover-level`) | 0,78rem mono 700, maiúsculas | 8pt | Contorno de 2px `--ink` |
| Código da capa (`.cover-code`) | até 6rem, mono 700 | 64pt | `letter-spacing: -.085em`; hífen em `<span class="dash">` |
| Nome completo (`.cover-exam`) | 0,95rem mono 700, maiúsculas | 10,5pt | `--accent-ink` |
| Título da capa (`h1`) | até 3rem, 600 | 30pt | `letter-spacing: -.045em` |
| Subtítulo da capa | 1,14rem | 12pt | `--muted` |
| Autoria (`.cover-author`) | 1,05rem, nome em 600 | 11pt | No rodapé da capa; site em mono `--teal`, sem sublinhado no PDF |
| Título "Sumário" | 1,9rem | 18pt | Borda inferior de 3px `--ink` |
| Faixa de capítulo no sumário | 0,76rem mono 700, maiúsculas | 8pt | `letter-spacing: .06em` |
| Item do sumário | 0,88rem | 8,9pt | Número em mono 0,74rem / 7,8pt |
| Tópico do sumário | 0,82rem | 8,3pt | Recuado 14px, `--muted` |
| Título de capítulo (`h2`) | até 2,1rem, 600 | 20pt | — |
| Título de seção (`h3`) | 1,35rem, 600 | — | — |
| Tópico (`h4`) | 1,08rem | — | — |
| Kicker / rótulos mono | 0,75–0,78rem, 700, maiúsculas | — | `letter-spacing: .1–.14em` |
| Tabela | 0,88rem | 7,6pt | Cabeçalho 0,78rem |

Regras de leitura: parágrafos e itens com no máximo **75ch**, `orphans`/`widows` 3, hifenização automática no corpo e desligada em títulos e capa.

---

## Forma e espaçamento

| Recurso | Valores | Onde |
| --- | --- | --- |
| Barras grossas | lombada 16mm (capa), 16px (barra de pesos), 9px (destaques da capa), 6px (capítulo), 3px (sumário) | Estrutura de página |
| Borda de destaque lateral | 4px (faixa do sumário, blockquote, flashcard), 5px (callout) | Componentes com ênfase |
| Borda fina | 1px `--line` | Cards, tabelas, divisórias de seção |
| Raios | 3–6px em caixas, 8px em cards, 999px em chips, 50% em marcadores | — |
| Sombra | Só na folha em tela (`0 16px 55px`) | Nunca em componentes |
| Folha em tela | até 920px, margem lateral 70px (16px no celular) | `.book` |

---

## Estrutura da página

### Capa (`.cover`)

Direção editorial clara, com lombada. No PDF a capa ocupa a folha inteira, até a borda (`@page:first` sem margem, `height:297mm`), e não tem rodapé de página. A lombada à esquerda (16 mm no PDF, 60px na tela, 32px no celular) é a única área escura: o bloco de destaque no topo e o nome da coleção na vertical, na base.

```
┌──┬────────────────────────────────────────────────────────┐
│▓▓│ CATEGORIA                         ATUALIZADO EM MÊS/ANO │
│▓▓│                                                        │
│██│ ┌ NÍVEL ASSOCIATE ┐    ← selo opcional                 │
│██│ TÍTULO-CURTO           ← mono gigante (64pt no PDF)    │
│██│ NOME COMPLETO          ← mono, --accent-ink (opcional) │
│██│ ▬▬▬                    ← fio de destaque               │
│██│ Título                 ← sans 600                      │
│██│ Subtítulo em --muted                                   │
│██│ ══════════════════════════════════════════════════════ │
│██│ RÓTULO DOS DESTAQUES                                   │
│G │ ▬▬▬▬▬▬▬|████████|▬▬▬▬▬▬▬▬▬▬|█████|▬▬▬▬  ← barra com pesos│
│U │ ▬ 20%    █ 24%    ▬ 28%    █ 14%   ▬ 14%  ← legenda      │
│I │ ────────────────────────────────────────────────────── │
│A │ Erik Nathan  eriknathan.me                             │
└──┴────────────────────────────────────────────────────────┘
 ▓ bloco --accent   █ lombada --ink   GUIAS DE ESTUDO na vertical
```

Regras da capa:

- **Nada repete.** O topo direito traz a data de atualização; o nome completo do assunto fica só abaixo do código.
- **Pesos numa barra só.** Quando os destaques são pesos (domínios de exame), `.cover-bar` mostra a proporção com um segmento por destaque, e a legenda fica em colunas iguais (`.highlight-grid.weighted`), sem texto espremido nas colunas estreitas. Segmentos e marcadores da legenda alternam `--accent` e `--ink`, na mesma ordem. Destaques sem peso (blocos, pilares) usam colunas iguais, todos com a barra `--accent`.
- **Nota opcional.** `<span class="highlight-note">` traz a tradução ou um detalhe curto em `--muted`. O nome oficial em inglês leva `lang="en"`.
- **Autoria no rodapé da capa** (`.cover-foot`), separada por um fio fino, como num livro; o nome da coleção (`.cover-series`) vai para a lombada.
- **Selo em vez de cor.** O nível da certificação diferencia e-books da mesma família sem quebrar a regra de uma cor de destaque.
- **Hífen no código.** Em mono, o hífen ocupa uma célula inteira; envolva-o em `<span class="dash">-</span>`. Códigos muito longos (ex.: `Well-Architected`) precisam de fonte menor para caber em uma linha.
- **Sem `vw` no miolo impresso.** Com a capa sem margem, `vw` passa a medir a primeira página (210 mm) na impressão; tamanhos em `vw` precisam de valor fixo no `@media print`.

### Sumário (`.toc`)

- Uma **faixa por capítulo**: `Capítulo N — Nome`, mono maiúsculo, fundo `--surface`, borda esquerda de 4px `--accent`.
- **Seções** (h3) numeradas `N.M` em `--accent-ink`, duas colunas, pontilhado `--line` sob cada item.
- **Tópicos** (h4) numerados `N.M.K`, no mesmo estilo, recuados.
- **Tópicos** (h4) logo abaixo da seção, sem número, recuados e em `--muted`.
- Capítulo sem seções: a própria faixa vira link.
- Capítulo sem número no original ("Como usar este guia"): a faixa mantém o nome original.
- Na tela, as faixas abrem e fecham (`+`/`−`). Na impressão, tudo fica aberto.

### Capítulo (`.chapter`)

Sempre começa em folha nova no PDF.

```
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ (6px ink)
CAPÍTULO 1                  ← kicker, --accent-ink
Nome do capítulo            ← h2
───────────────────────────────────── (1px ink)
[1.1] Nome da seção         ← sec-label + h3
1.1.1 Nome do tópico        ← topic-num + h4 (opcional)
```

O número do `sec-label` é o mesmo do sumário, e o `id` da seção é o destino do link.

**Numeração hierárquica (regra do padrão):** capítulo `N`, seção `N.M`, tópico `N.M.K`, sempre reiniciando a contagem no nível acima. O mesmo número aparece no sumário e no título. O `ferramentas/gerar_ebook.py` calcula os números e os coloca em `sec-label` (h3) e `topic-num` (h4); não os escreva à mão. Com `numeracao = "markdown"` no `ebook.toml`, capítulos sem número no original (ex.: "Como usar este guia") ficam sem kicker e sem numeração nas seções.

### Rodapé do PDF

- Esquerda: `{{RODAPE}}  |  Erik Nathan (eriknathan.me)`, em mono 8pt `--muted`.
- Direita: número da página, em mono 9pt `--ink`.
- Não aparece na capa. O texto do rodapé não é clicável no PDF.

---

## Componentes

Use o componente pelo formato do conteúdo, não para variar o visual.

| Conteúdo | Componente | Aparência |
| --- | --- | --- |
| Definição-chave, citação oficial | `blockquote` | Fundo `--surface`, borda esquerda laranja, itálico |
| Aviso, dica, importante, atenção | `.callout` | Fundo `--accent-soft`, rótulo mono em maiúsculas à esquerda |
| Itens paralelos com descrição | `.cards-grid > .card` | Grade auto (mín. 190px), borda superior laranja |
| Termos soltos, siglas | `.chips > .chip` | Pílula mono; `.chip.accent` para o termo principal |
| Sequência cronológica | `.timeline > .timeline-item` | Linha vertical com pontos laranja, data em mono |
| Passo a passo | `ol.numbered-list` | Número em círculo `--accent-soft`, divisória entre passos |
| Colunas, comparações | `.table-scroll > table` | Cabeçalho `--ink`, linhas zebradas, rolagem horizontal na tela |
| Código, comandos | `.book-content pre` | Fundo `--surface`, borda esquerda `--teal`, mono 0,8rem (7,6pt no PDF, com quebra de linha) |
| Separador (`---`) | `.book-content hr` | Linha `--line` na tela; some no PDF |
| Pergunta aberta | `details.flashcard` | Borda esquerda laranja, resposta em `--surface` |
| Múltipla escolha | `details.flashcard` + `.flashcard-options` | Alternativas com letra mono, resposta abaixo |
| Síntese final | `.closing` | Bloco `--ink` com borda superior laranja |

### Snippets

```html
<blockquote><p>Definição</p></blockquote>

<div class="callout"><span class="icon">Atenção</span><div class="body"><p>Texto</p></div></div>

<div class="cards-grid">
  <div class="card"><h4>Item</h4><p>Descrição</p></div>
</div>

<div class="chips"><span class="chip accent">Principal</span><span class="chip">Termo</span></div>

<div class="timeline">
  <div class="timeline-item"><span class="when">2024</span><p>Evento</p></div>
</div>

<ol class="numbered-list"><li><span class="b">1</span><div>Passo</div></li></ol>

<div class="table-scroll" tabindex="0" role="region" aria-label="Descrição">
  <table>
    <caption class="sr-only">Descrição</caption>
    <thead><tr><th scope="col">Coluna</th></tr></thead>
    <tbody><tr><td>Valor</td></tr></tbody>
  </table>
</div>

<details class="flashcard">
  <summary>Enunciado</summary>
  <ul class="flashcard-options">
    <li><span class="letter">A</span><span>Alternativa</span></li>
  </ul>
  <div class="flashcard-answer">
    <p class="answer-label">Resposta: A</p>
    <p>Explicação curta</p>
  </div>
</details>
```

---

## Impressão (PDF)

| Regra | Valor |
| --- | --- |
| Papel | A4 |
| Margens | 19mm topo · 17mm laterais · 21mm base |
| Quebras de página | Depois da capa, depois do sumário, antes de cada capítulo |
| Evitar quebra dentro de | Cards, callouts, blockquotes, flashcards, itens da timeline, linhas de tabela |
| Evitar quebra logo após | Faixas do sumário, títulos de capítulo, seção e tópico |
| Tabelas | Cabeçalho repetido em cada página (`thead { display: table-header-group }`) |
| `details` | Todos abertos (CSS + script `beforeprint`/`afterprint`) |
| Tinta | `sec-label`, cabeçalho de tabela e `.closing` perdem o fundo escuro e viram contorno |
| Links | Sem sublinhado, na cor do texto |
| Cores | `print-color-adjust: exact` para manter faixas e bordas |

Gere sempre pelo Chrome headless (`ferramentas/gerar_pdf.py`), que respeita `@page` e as margens com rodapé e depois escreve o número da página de cada linha do sumário (por isso `.toc-list a` tem 24px de folga à direita no PDF). Não use captura de tela.

---

## Responsivo e acessibilidade

- **≤ 700px:** folha sem margem e sem sombra, gutter de 16px, sumário e destaques da capa em coluna única (a barra de cada destaque passa a ter `--w`% da largura), tabelas com rolagem horizontal.
- **Semântica:** `article.book` › `header.cover` › `nav.toc` › `main#conteudo` › `section.chapter` › `section.section` › `section.topic`. Os níveis de título seguem a ordem (h1 na capa, h2 no capítulo, h3 na seção, h4 no tópico).
- **Foco:** contorno de 3px `--accent-ink` em links, `summary` e tabelas roláveis.
- **Link de pular** para o conteúdo, no topo.
- **Tabelas:** `caption` oculta visualmente e `th scope="col"`.
- **Movimento:** rolagem suave desligada com `prefers-reduced-motion`.

---

## Não fazer

- Usar `--accent` (#ff9900) como cor de texto: não passa em contraste.
- Criar componentes, fontes ou cores novas fora dos tokens.
- Transformar parágrafos em cards só para enfeitar.
- Adicionar sombras a componentes.
- Mudar margens de `@page` ou tamanhos de impressão: o sumário e as quebras foram calibrados para eles.
