# Design system — e-books de estudo (HTML + PDF)

Referência do padrão visual usado nos PDFs (SAA-C03, Well-Architected). A implementação está em [`ebook-template.html`](ebook-template.html); este documento explica **o que** cada peça é e **quando** usar. Se os dois divergirem, vale o template.

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
| `--teal` | `#086b70` | Links na tela, linha de autoria, rótulo "Resposta" | 6,3:1 |

---

## Tipografia

| Família | Token | Pesos | Uso |
| --- | --- | --- | --- |
| IBM Plex Sans | `--sans` | 400, 500, 600, 700 | Corpo, títulos |
| IBM Plex Mono | `--mono` | 400, 500, 600, 700 | Código da capa, rótulos, números, faixas, chips, `code` |

As duas vêm do Google Fonts, com alternativas locais (`-apple-system`, `Segoe UI`, `Arial` / `Menlo`, `Consolas`) para abrir sem rede.

### Escala

| Elemento | Tela | PDF | Detalhe |
| --- | --- | --- | --- |
| Base (`body`) | 16px / 1,65 | 9,5pt / 1,48 | — |
| Código da capa (`.cover-code`) | até 6rem, mono 700 | 56pt | `letter-spacing: -.085em` |
| Título da capa (`h1`) | até 3rem, 600 | 30pt | `letter-spacing: -.045em` |
| Subtítulo da capa | 1,14rem | 12pt | `--muted` |
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
| Barras grossas | 10px (capa), 6px (capítulo), 3px (sumário), 4px (destaques da capa) | Estrutura de página |
| Borda de destaque lateral | 4px (faixa do sumário, blockquote, flashcard), 5px (callout) | Componentes com ênfase |
| Borda fina | 1px `--line` | Cards, tabelas, divisórias de seção |
| Raios | 3–6px em caixas, 8px em cards, 999px em chips, 50% em marcadores | — |
| Sombra | Só na folha em tela (`0 16px 55px`) | Nunca em componentes |
| Folha em tela | até 920px, margem lateral 70px (16px no celular) | `.book` |

---

## Estrutura da página

### Capa (`.cover`)

Ocupa a primeira folha inteira, sem rodapé.

```
┌ barra ▬▬▬(laranja 92px)▬▬▬▬▬▬▬▬▬▬▬▬(ink)▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ┐
  CATEGORIA                           NOME COMPLETO DO ASSUNTO

  TÍTULO-CURTO            ← mono gigante
  Título                  ← sans 600
  Subtítulo em --muted
  Por Erik Nathan · eriknathan.me

  ───────────────────────────────────────────────────────────
  RÓTULO DOS DESTAQUES
  ▬▬▬▬▬   ▬▬▬▬▬   ▬▬▬▬▬   ▬▬▬▬▬    ← 3 a 6 destaques
  30%     26%     24%     20%        (número em mono + legenda)
```

### Sumário (`.toc`)

- Uma **faixa por capítulo**: `Capítulo N — Nome`, mono maiúsculo, fundo `--surface`, borda esquerda de 4px `--accent`.
- **Seções** (h3) numeradas `N.M` em `--accent-ink`, duas colunas, pontilhado `--line` sob cada item.
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
```

O número do `sec-label` é o mesmo do sumário, e o `id` da seção é o destino do link.

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

Gere sempre pelo Chrome headless (`template/gerar_pdf.py`), que respeita `@page` e as margens com rodapé. Não use captura de tela.

---

## Responsivo e acessibilidade

- **≤ 700px:** folha sem margem e sem sombra, gutter de 16px, sumário e destaques da capa em coluna única ou dupla, tabelas com rolagem horizontal.
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
