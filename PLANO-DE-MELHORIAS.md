# Plano de melhorias do repositório de e-books

Diagnóstico feito em 05/10/2026, sobre o commit `c06bf89`. O plano tem quatro fases, na ordem em que devem ser executadas. Cada fase termina com o repositório funcionando e pode virar um commit (ou uma série de commits) independente.

## Situação atual

| Item | Situação |
| --- | --- |
| E-books | 8: Well-Architected, SAA-C03, CLF-C02, AIF-C01, DVA-C02, Docker, Kubernetes e GH-200 |
| HTML gerado × Markdown | Os 7 `ebook.html` gerados a partir de Markdown estão em sincronia com seus geradores (conferido regenerando numa cópia) |
| `gerar_pdf.py` | 8 cópias; 7 são idênticas, exceto pelo nome do PDF e pela docstring. A do Well-Architected e a do `template/` não numeram o sumário |
| `gerar_ebook.py` | 6 cópias de cerca de 480 linhas (AIF, CLF, DVA, SAA, Docker, Kubernetes), com cerca de 200 linhas de CSS embutido, + 1 versão diferente no GH-200, que lê o CSS do template |
| CSS | O CSS embutido nas 6 cópias é uma versão anterior à do `template/ebook-template.html` (ex.: `.domain-grid` × `.highlight-grid`, tamanho de `.cover-code`, hifenização) |
| PDFs | Duas cópias de cada um: em `<pasta>/output/pdf/` e em `PDF-Geral/`. As das pastas estão desatualizadas em AIF, CLF, DVA e GH-200 |
| `.git` | 50 MB, com 44 versões de PDF em 5 commits; cada regeneração completa soma cerca de 30 MB |
| Local | O repositório está no iCloud Drive, origem dos arquivos `… 2.pdf` |

## Decisões a tomar antes de começar

| # | Decisão | Recomendação | Afeta |
| --- | --- | --- | --- |
| D1 | Onde ficam os PDFs | Fora do git, publicados em GitHub Releases. `PDF-Geral/` continua existindo localmente | Fases 1, 3 e 4 |
| D2 | Visual dos 6 e-books antigos | Migrar para o CSS atual do template, com revisão visual página a página | Fase 2 |
| D3 | Well-Architected entra no fluxo Markdown? | Sim, mas por último: o `material.md` dele não tem os callouts `[!question]` (os 48 flashcards estão só no HTML) | Fase 2 |
| D4 | Renomear pastas para slugs sem espaço | Sim, numa etapa isolada (quebra links e comandos documentados) | Fase 3 |
| D5 | Limpar PDFs do histórico do git | Opcional. Reescreve todos os commits e exige `push --force` | Fase 3 |
| D6 | Mover o repositório para fora do iCloud | Sim (ex.: `~/projetos/ebooks-eriknathan`) | Fase 3 |

---

## Fase 1 — Correções imediatas

> **Concluída em 05/10/2026.** Python 3.9 confirmado como versão mínima (o README do GH-200 foi corrigido). O `ebook.html` do Well-Architected ganhou `padding-right` nos links do sumário impresso, para os números de página não cobrirem títulos longos. Também foi criado um `.gitignore` parcial (item 3.1, sem as linhas de D1).

Mudanças pequenas e sem efeito no conteúdo dos e-books.

### 1.1 README da raiz

- [x] Corrigir os links da tabela para os nomes reais das pastas (`AWS - SAA-C03/`, `AWS - Well-Archeitect-Framework/`…), usando `<...>` nos caminhos com espaço, como já é feito na linha do GH-200.
- [x] Refazer a árvore da seção "Estrutura": incluir Docker, Kubernetes e GH-200 e corrigir os nomes das pastas.
- [x] Requisitos: incluir `pymupdf` (todo `gerar_pdf.py` importa `fitz`) e unificar a versão do Python. O código roda em 3.9+, mas o README do GH-200 diz 3.10+; confirmar com um ambiente 3.9 e corrigir o texto que estiver errado.
- [x] Corrigir os comandos da seção "Um e-book específico", que ainda usam `aws-well-architected-framework/`.

### 1.2 Arquivos que sobraram

- [x] Remover do git `AWS - Well-Archeitect-Framework/pdf/ebook-aws-well-architected 2.pdf` e `Kubernetes/output/pdf/kubernetes-guia-de-estudo 2.pdf` (cópias de conflito do iCloud).
- [x] Apagar as pastas temporárias `Kubernetes/output/pdf/ebook-pdf-bvlp4roz/` e `GH-200 - GitHub Actions Certification/output/pdf/ebook-pdf-6wznicpm/`.
- [x] Mover `prompt.md` (o prompt antigo, com visual livre) para `template/legado/prompt-antigo.md` ou removê-lo, e ajustar a menção no README.

### 1.3 PDFs desatualizados

Com D1 aceita:

- [x] Remover do git os PDFs de `<pasta>/output/pdf/` e de `AWS - Well-Archeitect-Framework/pdf/`. `PDF-Geral/` passa a ser a única cópia até a Fase 3.
- [x] Apontar os links de PDF do README da raiz e dos READMEs das pastas para `PDF-Geral/`.
- [x] Regenerar tudo com `python3 gerar-all-pdfs.py` para garantir que `PDF-Geral/` está atual.

### 1.4 Well-Architected

- [x] Renomear a pasta `AWS - Well-Archeitect-Framework` para `AWS - Well-Architected-Framework` (corrige o erro de digitação). Nenhum script referencia o nome; só os READMEs.
- [x] Portar `add_toc_page_numbers` para o `gerar_pdf.py` dele. O HTML já tem `nav#sumario` com 242 links no formato que a função espera.
- [x] Criar o `README.md` da pasta, no mesmo formato dos outros, dizendo que o `ebook.html` é a fonte e o `material.md` é derivado (até a Fase 2).

**Verificação:** `python3 gerar-all-pdfs.py --listar` lista os 8 e-books; os 8 PDFs são gerados sem erro; o PDF do Well-Architected sai com páginas no sumário; nenhum link relativo dos READMEs aponta para um arquivo inexistente (conferir com um script simples ou `lychee --offline`).

---

## Fase 2 — Eliminar a duplicação dos geradores

Objetivo: cada pasta de e-book guarda só conteúdo e metadados; o código e o CSS ficam num lugar só.

> **Concluída em 05/10/2026, exceto o item 2.6 (Well-Architected), que ficou pendente de decisão.** Mudanças em relação ao planejado:
>
> - **Etapa A sem comparação byte a byte.** Os 6 geradores antigos não diferiam do GH-200 só no CSS, mas na marcação (`section.subchapter` + `span.sec-num`, número do capítulo dentro do `h2`). Reproduzir o HTML antigo exigiria um modo legado no gerador, a ser apagado logo depois. No lugar disso, cada HTML novo foi comparado com o anterior: texto do conteúdo, títulos e âncoras, sumário (links, números e textos), capa, síntese, rodapé, título, descrição, blocos de código e número de perguntas. Os 7 ficaram equivalentes. As âncoras antigas foram mantidas, e os links já publicados continuam válidos.
> - **Etapa B feita direto no template, sem `legado.css`.** A revisão das páginas encontrou dois defeitos do template na impressão, corrigidos nele: o marcador das listas numeradas cortado (recuo de `ol` maior) e a grade da capa quebrando 5 destaques em 4+1 (o gerador agora fixa as colunas). O template também ganhou os estilos de bloco de código e separador (`pre`, `hr`), usados por 4 e-books, e a folga para o número de página no sumário. As mudanças visuais esperadas: rótulo de seção em caixa, kicker "Capítulo N", citação em itálico com borda laranja, código da capa em 56pt. Os PDFs ganharam de 0 a 3 páginas (sumário um pouco mais espaçado).
> - **`ebook.toml` com formato um pouco diferente do exemplo abaixo**: `[pagina]` com `titulo` e `descricao`, `destaques_com_peso` e `idioma` por destaque, e `numeracao` (`"automatica"` ou `"markdown"`). Ver `AWS - AIF-C01/ebook.toml`.
> - **`requirements.txt` criado nesta fase** (item 3.1), porque o `tomli` passou a ser necessário no Python 3.9 e 3.10. Testado com Python 3.9.

### 2.1 Estrutura-alvo

```text
.
├── ferramentas/
│   ├── gerar_ebook.py        # Markdown + ebook.toml + template → ebook.html
│   ├── gerar_pdf.py          # ebook.html → PDF com sumário numerado
│   └── gerar_todos.py        # substitui o gerar-all-pdfs.py
├── template/
│   ├── ebook-template.html   # fonte única do CSS e da estrutura
│   ├── DESIGN-SYSTEM.md
│   └── PROMPT.md
├── AWS - AIF-C01/
│   ├── material.md           # conteúdo
│   ├── ebook.toml            # metadados: capa, rodapé, síntese, nome do PDF
│   ├── extra.css             # opcional: ajustes de impressão só deste e-book
│   ├── ebook.html            # gerado
│   └── README.md
└── ...
```

### 2.2 Formato do `ebook.toml`

Tudo o que hoje varia entre as cópias de `gerar_ebook.py` vira dado:

```toml
fonte = "material.md"                 # SAA-C03 usa "material-original.md"
pdf = "aif-c01-guia-de-revisao.pdf"
rodape = "AIF-C01  /  GUIA DE REVISÃO"
descricao = "Guia de revisão AIF-C01 com fundamentos de IA, ..."
titulo_pagina = "AIF-C01 — Guia de revisão"

[capa]
categoria = "Guia de estudo"
atualizado = "setembro de 2026"
selo = "Nível Foundational"           # opcional
codigo = "AIF-C01"                    # o hífen vira <span class="dash">
exame = "AWS Certified AI Practitioner"
titulo = "Guia de revisão"
subtitulo = "Fundamentos de IA e ML, IA generativa, ..."
rotulo_destaques = "Domínios do exame · pesos oficiais"
destaques_proporcionais = true        # largura das barras segue o peso

[[capa.destaques]]
valor = "20%"
texto = "Fundamentals of AI and ML"
texto_en = true
nota = "Fundamentos de IA e ML"
peso = 20

[sintese]
introducao = "Este guia organiza a revisão pelos quatro domínios do exame ..."
itens = [
  "Os pesos oficiais são 20% para ...",
  "O autoteste ... oferecem {flashcards} perguntas para revisão ativa.",
]
```

Usar `tomllib` (biblioteca padrão a partir do Python 3.11) ou `tomli` no 3.9/3.10. Se preferir não depender disso, o mesmo conteúdo cabe em front matter YAML no topo do `material.md`.

### 2.3 Gerador único (`ferramentas/gerar_ebook.py`)

- [x] Partir do `Docker/gerar_ebook.py`, que o `template/PROMPT.md` aponta como referência.
- [x] Incorporar o que só o GH-200 tem: a checagem de que o texto do Markdown foi preservado (`content_text`) e a verificação dos links internos.
- [x] Ler o CSS de `template/ebook-template.html` (como o GH-200 já faz) e acrescentar o `extra.css` da pasta, se existir.
- [x] Montar capa e síntese a partir do `ebook.toml`, sem HTML fixo no Python.
- [x] Uso: `python3 ferramentas/gerar_ebook.py "AWS - AIF-C01"` (ou sem argumento, para todas as pastas).
- [x] Manter as validações atuais: número de flashcards e de capítulos esperado; erro se algo divergir.

### 2.4 PDF único (`ferramentas/gerar_pdf.py`)

- [x] Uma só cópia, com `add_toc_page_numbers`, recebendo a pasta do e-book e lendo o nome do PDF do `ebook.toml`.
- [x] Apagar os 8 `gerar_pdf.py` das pastas e o `template/gerar_pdf.py`.
- [x] `ferramentas/gerar_todos.py` passa a descobrir os e-books pelo `ebook.toml`, não mais por regex no `DEFAULT_OUTPUT`.

### 2.5 Migração, em duas etapas

**Etapa A — mesmo resultado, código novo.** Para provar que o gerador único não muda nada:

1. Copiar temporariamente o CSS antigo (o das 6 cópias) para `template/legado.css` e as linhas extras de `pre` do Docker, do Kubernetes e do DVA para o `extra.css` de cada um.
2. Migrar um e-book por vez (AIF → CLF → DVA → SAA → Docker → Kubernetes).
3. Para cada um, o `ebook.html` gerado deve ser **byte a byte igual** ao atual. Se não for, corrigir o gerador, não o arquivo.
4. GH-200 por último: o HTML dele pode mudar na marcação do sumário. Comparar com `diff` e aceitar só diferenças de marcação, sem perda de texto (a checagem `content_text` garante isso).

**Etapa B — convergência visual (D2).**

1. Gerar os PDFs de todos os e-books com o CSS antigo e guardar fora do repositório (ex.: `/tmp/antes/`).
2. Trocar `legado.css` pelo CSS do template; reduzir cada `extra.css` ao mínimo.
3. Renderizar as páginas dos PDFs de antes e depois em PNG com PyMuPDF e comparar (diferença de pixels por página + revisão manual das páginas que mudarem). Atenção especial à capa (`.domain-grid` → `.highlight-grid`) e ao sumário.
4. Apagar `template/legado.css`.

### 2.6 Well-Architected no fluxo Markdown (D3) — pendente

> **Não feito.** O `ebook.html` usa componentes ricos que o fluxo Markdown não gera sozinho: 71 cards, 59 blocos de pilar, 16 itens de linha do tempo, 38 quizzes com a alternativa correta destacada e passos com setas. O `material.md` tem 98% das palavras do HTML, mas sem essa estrutura (os componentes viram texto corrido, com negrito quebrado como `****…**:**`). Uma conversão mecânica faria o e-book perder esses componentes. Opções: (a) manter o HTML editado à mão, como está hoje, já integrado às ferramentas por um `ebook.toml` sem `fonte`; (b) reescrever o `material.md` com os componentes em HTML embutido e conferir página a página, o que é um trabalho editorial à parte.

- [ ] Converter os 48 flashcards do `ebook.html` para callouts `> [!question]-` no `material.md`.
- [ ] Remover do `material.md` o sumário manual (o gerador cria o sumário).
- [ ] Criar o `ebook.toml` dele e gerar o HTML; comparar o texto com o `ebook.html` atual (mesma checagem de preservação). Revisar visualmente.

### 2.7 Documentação

- [x] Atualizar `template/PROMPT.md` e `template/DESIGN-SYSTEM.md`: um e-book novo passa a ser "pasta + `material.md` + `ebook.toml`".
- [x] Simplificar os READMEs das pastas: só o que é específico do e-book (fontes, data de conferência, observações). Os comandos ficam no README da raiz.

**Verificação:** nenhum `gerar_ebook.py` ou `gerar_pdf.py` dentro das pastas de e-book; `python3 ferramentas/gerar_todos.py` gera os 8 HTML e os 8 PDFs; a Etapa A reproduziu os HTML byte a byte; a Etapa B teve todas as páginas alteradas revisadas.

---

## Fase 3 — Organização do repositório

> **Concluída em 05/10/2026 conforme as decisões de 05/10:** D1 = manter os PDFs no git (sem Release nem LFS); D5 = não reescrever o histórico; D6 = não mover o repositório para fora do iCloud. Por isso os itens 3.2, 3.3 e 3.4 não foram executados, e o `.gitignore` não ignora `PDF-Geral/`. Os itens 3.1 e 3.5 foram feitos. As mudanças foram commitadas localmente, sem push.

### 3.1 Arquivos de apoio (pode ser feito antes da Fase 2)

- [x] `.gitignore`: (sem `PDF-Geral/`, pela decisão D1 de manter os PDFs no git)

  ```gitignore
  .DS_Store
  __pycache__/
  *.pyc
  ebook-pdf-*/
  * 2.*
  output/
  PDF-Geral/
  ```

  (As duas últimas linhas só com D1 aceita.)

- [x] `requirements.txt`: `markdown-it-py`, `beautifulsoup4`, `pymupdf` e `tomli; python_version < "3.11"`, com versões mínimas testadas.

### 3.2 PDFs fora do git (D1)

- [ ] `git rm --cached -r PDF-Geral/` e conferir que nenhum outro PDF continua versionado.
- [ ] Publicar os PDFs numa Release (`gh release create v2026.10 PDF-Geral/*.pdf`) e trocar os links do README pelo link da Release mais recente (`https://github.com/<usuário>/<repo>/releases/latest`).
- [ ] Alternativa, se os PDFs precisarem continuar no repositório: Git LFS para `*.pdf`.

### 3.3 Histórico (D5, opcional)

- [ ] Fazer um backup (`git clone --mirror`).
- [ ] `git filter-repo --path-glob '*.pdf' --invert-paths`.
- [ ] `git push --force` e reclonar onde houver cópias. Resultado esperado: `.git` de 50 MB para poucos MB.

### 3.4 Sair do iCloud (D6)

- [ ] Commitar e dar push de tudo.
- [ ] Clonar em `~/projetos/ebooks-eriknathan` (fora do iCloud) e conferir que o build funciona lá.
- [ ] Apagar a cópia do iCloud só depois disso.

### 3.5 Nomes de pasta (D4)

> **Feito em 05/10/2026** (`git mv` em duas etapas, por causa das pastas que só mudam de maiúscula para minúscula num disco que não diferencia as duas).

Etapa isolada, num commit só, com `git mv` para preservar o histórico:

| Atual | Novo |
| --- | --- |
| `AWS - AIF-C01` | `aws-aif-c01` |
| `AWS - CLF-C02` | `aws-clf-c02` |
| `AWS - DVA-C02` | `aws-dva-c02` |
| `AWS - SAA-C03` | `aws-saa-c03` |
| `AWS - Well-Architected-Framework` | `aws-well-architected` |
| `Docker` | `docker` |
| `Kubernetes` | `kubernetes` |
| `GH-200 - GitHub Actions Certification` | `gh-200` |

- [x] Renomear também `material-original.md` do SAA-C03 para `material.md` e ajustar o `ebook.toml`.
- [x] Atualizar READMEs, `template/PROMPT.md` e links internos; procurar o nome antigo com `grep` antes do commit.

**Verificação:** `git status` limpo depois de um build completo (nada gerado aparece como modificado); `git ls-files '*.pdf'` vazio (com D1); build funcionando fora do iCloud.

---

## Fase 4 — Automação

> **Concluída em 05/10/2026, com a 4.3 encerrada pelo critério do próprio plano** (os PDFs do Linux não saem iguais aos do macOS). Resultados:
>
> - **4.1:** IBM Plex em `template/fontes/` (latin e latin-ext; o Plex Sans normal é variável, um arquivo para 400–700). O `gerar_ebook.py` embute em base64 só as faces que o texto usa (cerca de 135 KB por HTML; hoje só o subconjunto latin). O Well-Architected, editado à mão, ganhou `aws-well-architected/fontes/` com as fontes dele, carregadas por caminho relativo. Com e sem rede, os 8 PDFs ficaram idênticos pixel a pixel aos anteriores; antes, sem rede, o Well-Architected mudava inteiro (140 páginas em vez de 137). Como os PDFs não mudaram, `PDF-Geral/` não foi regenerado.
> - **4.2:** `.github/workflows/verificar.yml` (Python 3.9 e 3.x) e `ferramentas/verificar_links.py`. Simulado em contêineres Linux: passa com o repositório atual e falha quando só o `material.md` é editado. Ainda não rodou no GitHub (sem push).
> - **4.3:** no Linux (Chromium em contêiner), todas as páginas têm pequenas diferenças de rasterização, e o CLF-C02 e o SAA-C03 mudam de paginação (95→96 e 157→159), porque os caracteres sem glifo no Plex (`→`, `≥`, `└`) caem em fontes de reserva diferentes. O `publicar.yml` não foi criado; os PDFs continuam gerados no macOS (coerente com D1). O `gerar_pdf.py` passou a usar `--no-sandbox` quando roda como root ou com `CI=true`, condição necessária para o Chromium em contêiner.
> - **4.4:** documentado no README da raiz ("Ao atualizar um e-book").

### 4.1 Fontes locais

- [x] Baixar IBM Plex Sans e IBM Plex Mono (licença OFL) para `template/fontes/` e trocar o `<link>` do Google Fonts por `@font-face`. O `ebook.html` precisa continuar autônomo: embutir as fontes em base64 no HTML gerado ou referenciá-las por caminho relativo e copiá-las junto.
- [x] Objetivo: o PDF sai igual com ou sem rede.

### 4.2 CI de verificação (a cada push e pull request)

Workflow `.github/workflows/verificar.yml`:

- [x] Instalar Python e `requirements.txt`.
- [x] Rodar `ferramentas/gerar_ebook.py` para todas as pastas e falhar se `git diff --exit-code -- '*/ebook.html'` mostrar diferença (HTML fora de sincronia com o Markdown).
- [x] Rodar a checagem de links relativos dos READMEs.

### 4.3 Publicação dos PDFs (manual ou por tag)

Workflow `.github/workflows/publicar.yml`, disparado por `workflow_dispatch` ou por uma tag `v*`:

- [ ] ~~Instalar Chrome (`browser-actions/setup-chrome`) e as dependências.~~ (não feito: ver 4.3)
- [ ] ~~`python3 ferramentas/gerar_todos.py --destino dist/`.~~ (não feito: ver 4.3)
- [ ] ~~Criar ou atualizar a Release com os 8 PDFs (`gh release upload`).~~ (não feito: ver 4.3)
- [x] Conferir se os PDFs gerados no Linux saem iguais aos do macOS (fontes e quebras de página); se não saírem, manter a geração local e usar o CI só para a verificação da 4.2.

### 4.4 Data de atualização

- [x] Hoje "Atualizado em setembro de 2026" está fixo em cada gerador. Com a Fase 2 ela vai para o `ebook.toml`; documentar no README que ela deve ser atualizada junto com o conteúdo.

**Verificação:** um PR que altere só o `material.md`, sem regenerar o HTML, falha no CI; uma tag gera uma Release com os 8 PDFs.

---

## Ordem de execução resumida

1. Fase 1 inteira.
2. Fase 3.1 (`.gitignore` e `requirements.txt`).
3. Fase 2 (Etapa A, depois Etapa B, depois Well-Architected).
4. Fase 3.2 a 3.5.
5. Fase 4.

## Riscos

| Risco | Mitigação |
| --- | --- |
| O gerador único muda o HTML sem ninguém perceber | Etapa A exige HTML byte a byte igual antes de qualquer mudança visual |
| A troca de CSS quebra a paginação do PDF | Comparação página a página na Etapa B; `extra.css` por e-book para ajustes pontuais |
| Perda de PDFs ao tirá-los do git | Publicar a Release antes de remover; backup `--mirror` antes de reescrever o histórico |
| Links quebrados depois de renomear pastas | Renomeação isolada num commit, com busca pelo nome antigo e checagem de links |
| Conflitos do iCloud durante o trabalho | Fazer a Fase 3.4 cedo, se possível antes da Fase 2 |
