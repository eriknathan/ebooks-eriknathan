# Prompt padrão — material Markdown → e-book HTML + PDF

> Cole este prompt numa conversa com o Claude, no repositório, e preencha os campos em `<dados>` e `<conteudo>`.
> O visual é fixo: vem de `template/ebook-template.html`. O prompt serve só para garantir que todo e-book sai igual.

---

Transforme o material Markdown em `<conteudo>` num e-book de estudo, em HTML e PDF, usando o **template padrão do repositório**.

## Arquivos

- **Base visual obrigatória:** `template/ebook-template.html`. Copie esse arquivo para `<pasta>/ebook.html` e preencha. Não crie um novo design.
- **Referência do padrão:** `template/DESIGN-SYSTEM.md` (cores, tipografia, componentes e regras de impressão). Consulte antes de decidir qual componente usar.
- **PDF:** `python3 template/gerar_pdf.py <pasta>/ebook.html <pasta>/output/pdf/<nome-do-pdf>.pdf`
- Se o material for longo ou tiver que ser regerado várias vezes, escreva um `<pasta>/gerar_ebook.py` que converta o Markdown e injete o resultado no template, como em `SAA-C03/gerar_ebook.py`. Assim a formatação continua igual quando o material mudar.

## O que pode e o que não pode mudar no template

**Pode:**
- Preencher todos os marcadores `{{...}}` e apagar os moldes que não forem usados.
- Repetir os blocos marcados com `REPETIR`.
- Trocar as cores do bloco `TOKENS DO E-BOOK` **somente** se `<dados>` pedir outra cor de destaque. Mantenha o contraste AA em `--accent-ink`.
- Trocar o texto do rodapé em `@page` (`{{RODAPE}}`). A autoria que vem depois dele (`| Erik Nathan (eriknathan.me)`) é fixa e aparece em todas as páginas.

**Não pode:**
- Alterar o resto do CSS, as fontes, os tamanhos, as regras de impressão ou a estrutura da capa e do sumário.
- Criar componentes novos. Se nenhum componente servir, use parágrafo, lista ou tabela.

## Estrutura (nesta ordem)

1. **Capa** (`.cover`): categoria e data de atualização no topo, selo de nível (opcional), `TITULO_CURTO` grande em mono (hífen em `<span class="dash">`), nome completo, título, subtítulo, linha de autoria (já preenchida) e uma grade de 3 a 6 destaques (módulos, pilares, pesos, números-chave do material). Se os destaques forem pesos, a largura de cada barra segue o peso (ver comentário no template).
2. **Sumário** (`.toc`), no padrão:
   - uma faixa por capítulo: `Capítulo N — Nome` (mono, maiúsculas, fundo cinza, borda de destaque à esquerda);
   - seções (h3) numeradas como `N.M`, em duas colunas, com linha pontilhada;
   - tópicos (h4), se houver, logo abaixo da seção, recuados e sem número;
   - capítulo sem seções: a faixa vira um link direto (`div.toc-group > a.toc-group-title`);
   - capítulos sem número no original (introdução, "como usar") ficam com o nome original, sem `Capítulo N`.
3. **Capítulos** (`section.chapter`): `chapter-head` com o kicker `Capítulo N` e o título. Cada seção usa `sec-label` com o mesmo número `N.M` do sumário e o mesmo `id` do link.
4. **Perguntas** no ponto em que aparecem no original, com `details.flashcard` (aberta ou múltipla escolha).
5. **Síntese de revisão** (`.closing`) no final.

## Regras de conteúdo (prioridade máxima)

1. **Preserve o original:** todas as informações, perguntas, respostas, referências e links, na mesma ordem. Não resuma nem corte trechos. O trabalho é de diagramação.
2. **Ajustes editoriais mínimos:** corrija só erros evidentes de digitação e divida parágrafos longos sem mudar o sentido. Possível erro técnico ou ambiguidade: preserve e avise na resposta.
3. **Separe original de acréscimo:** perguntas criadas e a síntese só reorganizam o que está no material. Identifique-as como "Perguntas de revisão elaboradas a partir do material" e "Síntese de revisão". Nada de fatos novos.
4. **Português do Brasil**, mantendo os termos técnicos em inglês quando o original os usar.
5. **Não invente metadados.** Campo da capa sem base no material: apague o elemento.
6. **Gabarito:** não apresente como oficial o que o original não fornece. Resposta dedutível com segurança: marque como inferida. Sem fundamento: diga que o material não traz gabarito.

## Componente por tipo de conteúdo

| Conteúdo no original | Componente do template |
| --- | --- |
| Definição-chave ou citação oficial | `blockquote` |
| Aviso, dica, "importante", "atenção" | `.callout` (rótulo em `.icon`: Dica, Atenção, Importante) |
| Itens paralelos com descrição | `.cards-grid > .card` |
| Sequência cronológica | `.timeline` |
| Colunas ou comparações | `.table-scroll > table` (com `caption.sr-only` e `th scope="col"`) |
| Termos soltos, siglas, nomes | `.chips` |
| Passo a passo | `ol.numbered-list` |
| Pergunta e resposta | `details.flashcard` |
| Texto corrido | parágrafo (não transforme em card) |

## Conferência antes de entregar

1. Compare Markdown e HTML seção por seção: nada omitido ou alterado.
2. Todos os links do sumário apontam para `id`s existentes; nenhum `id` duplicado; numeração do sumário igual à dos `sec-label`.
3. Nenhum `{{...}}` sobrando no HTML (`grep -n "{{" <pasta>/ebook.html` deve voltar vazio).
4. Gere o PDF e confira capa, sumário, uma página com tabela, uma com perguntas e a última página: respostas visíveis, rodapé com número, sem páginas quase vazias.

Na resposta, informe os caminhos do HTML e do PDF e liste os possíveis erros ou ambiguidades encontrados no original.

---

<dados>
Pasta do projeto: [ex.: SAA-C03]
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
