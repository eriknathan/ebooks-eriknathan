# Prompt padrão — material Markdown → e-book HTML + PDF

> Cole este prompt numa conversa com o Claude, no repositório, e preencha os campos em `<dados>` e `<conteudo>`.
> O visual é fixo: vem de `template/ebook-template.html`. O prompt serve só para garantir que todo e-book sai igual.

---

Transforme o material Markdown em `<conteudo>` num e-book de estudo, em HTML e PDF, usando o **template padrão do repositório**.

## Arquivos

Todo e-book é uma pasta na raiz com três arquivos editáveis. O HTML e o PDF são gerados pelos scripts de `ferramentas/`, que aplicam o visual de `template/ebook-template.html`. Não crie um novo design nem um script por pasta.

- **`<pasta>/material.md`:** o conteúdo. `##` vira capítulo, `###` seção e `####` tópico. Callouts `> [!question]- Pergunta` (com a resposta nas linhas `>` seguintes) viram flashcards. Parágrafos `Q01.` seguidos de uma lista viram questões de múltipla escolha. Blocos de código, tabelas e citações são convertidos sem ajuste.
- **`<pasta>/ebook.toml`:** capa, síntese, rodapé, nome do PDF e título da página. Copie o de um e-book parecido (com pesos na capa: `aws-saa-c03/ebook.toml`; com blocos numerados: `Docker/ebook.toml`) e troque os valores. Os campos de texto aceitam HTML inline; `{flashcards}` na síntese vira o total de perguntas.
- **`<pasta>/extra.css` (opcional):** só para ajustes de paginação deste e-book, como em `gh-200/extra.css`. Não redefina componentes.
- **Referência do padrão:** `template/DESIGN-SYSTEM.md` (cores, tipografia, componentes e regras de impressão).

Para gerar, a partir da raiz:

```bash
python3 ferramentas/gerar_ebook.py "<pasta>"   # material.md + ebook.toml → ebook.html
python3 ferramentas/gerar_pdf.py "<pasta>"     # ebook.html → <pasta>/output/pdf/<pdf>
python3 ferramentas/gerar_todos.py --apenas "<pasta>"   # os dois passos, com o PDF em PDF-Geral/
```

### Numeração

- `numeracao = "automatica"` (padrão): todo `##` vira `Capítulo 1`, `Capítulo 2`… Não escreva números nos títulos.
- `numeracao = "markdown"`: só os `##` que começam com `N. ` são numerados (`## 3. Redes`); os demais (ex.: `## Como usar este guia`) ficam sem número, e suas seções também.
- Seções e tópicos são sempre numerados pelo script (`N.M` e `N.M.K`). Não escreva esses números à mão.

## O que pode e o que não pode mudar

**Pode:**
- Escolher os campos da capa no `ebook.toml` (selo, nome completo e notas são opcionais) e de 1 a 6 destaques; com `destaques_com_peso = true`, a largura de cada barra segue o `peso`.
- Trocar as cores do bloco `TOKENS DO E-BOOK` **somente** se `<dados>` pedir outra cor de destaque: redefina as variáveis de `:root` no `extra.css`. Mantenha o contraste AA em `--accent-ink`.
- Definir o texto do `rodape`. A autoria que vem depois dele (`| Erik Nathan (eriknathan.me)`) é fixa e aparece em todas as páginas.

**Não pode:**
- Alterar o CSS do template, as fontes, os tamanhos, as regras de impressão ou a estrutura da capa e do sumário.
- Criar componentes novos. Se nenhum componente servir, use parágrafo, lista ou tabela.

## Estrutura gerada (nesta ordem)

1. **Capa** (`.cover`): categoria e data no topo, selo (opcional), `codigo` grande em mono, nome completo, título, subtítulo, autoria fixa e a grade de destaques.
2. **Sumário** (`.toc`): uma faixa `Capítulo N — Nome` por capítulo, seções `N.M` e tópicos `N.M.K` em duas colunas; capítulo sem seções vira link direto. No PDF, o número da página entra à direita de cada linha.
3. **Capítulos** (`section.chapter`): `chapter-head` com o kicker `Capítulo N`, seções com `sec-label` e tópicos com `topic-num`, com os mesmos números do sumário.
4. **Perguntas** no ponto em que aparecem no original, com `details.flashcard`.
5. **Síntese de revisão** (`.closing`) no final, a partir do `[sintese]` do `ebook.toml`.

## Regras de conteúdo (prioridade máxima)

1. **Preserve o original:** todas as informações, perguntas, respostas, referências e links, na mesma ordem. Não resuma nem corte trechos. O trabalho é de diagramação.
2. **Ajustes editoriais mínimos:** corrija só erros evidentes de digitação e divida parágrafos longos sem mudar o sentido. Possível erro técnico ou ambiguidade: preserve e avise na resposta.
3. **Separe original de acréscimo:** perguntas criadas e a síntese só reorganizam o que está no material. Identifique-as como "Perguntas de revisão elaboradas a partir do material" e "Síntese de revisão". Nada de fatos novos.
4. **Português do Brasil**, mantendo os termos técnicos em inglês quando o original os usar.
5. **Não invente metadados.** Campo da capa sem base no material: apague o elemento.
6. **Gabarito:** não apresente como oficial o que o original não fornece. Resposta dedutível com segurança: marque como inferida. Sem fundamento: diga que o material não traz gabarito.

## Componente por tipo de conteúdo

Os componentes sem sintaxe própria no Markdown entram como HTML no próprio `material.md`, com as classes do template.

| Conteúdo no original | Componente do template |
| --- | --- |
| Definição-chave ou citação oficial | `blockquote` (`> texto` no Markdown) |
| Aviso, dica, "importante", "atenção" | `.callout` (rótulo em `.icon`: Dica, Atenção, Importante) |
| Itens paralelos com descrição | `.cards-grid > .card` |
| Sequência cronológica | `.timeline` |
| Colunas ou comparações | `.table-scroll > table` (com `caption.sr-only` e `th scope="col"`) |
| Termos soltos, siglas, nomes | `.chips` |
| Passo a passo | `ol.numbered-list` |
| Pergunta e resposta | `details.flashcard` (callout `> [!question]-`) |
| Código ou comandos | bloco cercado por três crases |
| Texto corrido | parágrafo (não transforme em card) |

## Conferência antes de entregar

1. Compare o material original com o `material.md` seção por seção: nada omitido ou alterado. O `gerar_ebook.py` confere sozinho que o HTML preserva todo o texto e os blocos de código do Markdown.
2. O `gerar_ebook.py` falha se houver `id` duplicado, link interno sem destino ou marcador `{{...}}` sobrando; corrija a causa no Markdown ou no `ebook.toml`.
3. Gere o PDF e confira capa, sumário, uma página com tabela, uma com perguntas e a última página: respostas visíveis, rodapé com número, sem páginas quase vazias.

Na resposta, informe os caminhos do HTML e do PDF e liste os possíveis erros ou ambiguidades encontrados no original.

---

<dados>
Pasta do projeto, em minúsculas e sem espaços: [ex.: aws-saa-c03]
Nome do PDF: [ex.: saa-c03-guia-de-revisao]
Categoria (topo esquerdo da capa): [ex.: Guia de estudo]
Data de atualização (topo direito): [ex.: setembro de 2026]
Selo de nível (opcional): [ex.: Nível Associate]
Título curto (destaque grande em mono): [ex.: SAA-C03]
Nome completo do assunto (abaixo do título curto): [ex.: AWS Certified Solutions Architect – Associate]
Título: [ex.: Guia de revisão]
Subtítulo: [uma frase descrevendo o material]
Rótulo e itens da grade de destaques: [ex.: Domínios do exame · pesos oficiais · 30% Design Secure Architectures (Arquiteturas seguras), 26% ...]
Rodapé do PDF: [ex.: SAA-C03  /  GUIA DE REVISÃO]
Cor de destaque (opcional): [padrão laranja #ff9900]
</dados>

<conteudo>
[COLE O MARKDOWN AQUI, OU INDIQUE O CAMINHO DO ARQUIVO]
</conteudo>
