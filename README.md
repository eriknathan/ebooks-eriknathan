# E-books de estudo

Guias de revisão em HTML e PDF, todos com o mesmo padrão visual: capa, sumário por capítulo, flashcards e versão A4 para impressão.

| E-book | Pasta | PDF |
| --- | --- | --- |
| AWS Well-Architected Framework | [aws-well-architected/](aws-well-architected/) | [ebook-aws-well-architected.pdf](PDF-Geral/ebook-aws-well-architected.pdf) |
| AWS Certified Solutions Architect – Associate (SAA-C03) | [aws-saa-c03/](aws-saa-c03/) | [saa-c03-guia-de-revisao.pdf](PDF-Geral/saa-c03-guia-de-revisao.pdf) |
| AWS Certified Cloud Practitioner (CLF-C02) | [aws-clf-c02/](aws-clf-c02/) | [clf-c02-guia-de-revisao.pdf](PDF-Geral/clf-c02-guia-de-revisao.pdf) |
| AWS Certified AI Practitioner (AIF-C01) | [aws-aif-c01/](aws-aif-c01/) | [aif-c01-guia-de-revisao.pdf](PDF-Geral/aif-c01-guia-de-revisao.pdf) |
| AWS Certified Developer – Associate (DVA-C02) | [aws-dva-c02/](aws-dva-c02/) | [dva-c02-guia-de-revisao.pdf](PDF-Geral/dva-c02-guia-de-revisao.pdf) |
| Docker — do contêiner à produção | [docker/](docker/) | [docker-guia-de-estudo.pdf](PDF-Geral/docker-guia-de-estudo.pdf) |
| Kubernetes — do Pod à produção | [kubernetes/](kubernetes/) | [kubernetes-guia-de-estudo.pdf](PDF-Geral/kubernetes-guia-de-estudo.pdf) |
| GH-200 — GitHub Actions Certification | [gh-200/](gh-200/) | [gh-200-guia-de-estudo.pdf](PDF-Geral/gh-200-guia-de-estudo.pdf) |

Os PDFs versionados ficam só em [`PDF-Geral/`](PDF-Geral/). O `ferramentas/gerar_pdf.py` grava por padrão uma cópia local em `<pasta>/output/pdf/`, que é ignorada pelo git.

## Estrutura

Cada e-book é uma pasta com o conteúdo e os metadados; o código e o visual ficam num lugar só.

```text
.
├── ferramentas/
│   ├── gerar_ebook.py                     # material.md + ebook.toml + template → ebook.html
│   ├── gerar_pdf.py                       # ebook.html → PDF com o sumário numerado
│   ├── gerar_todos.py                     # HTML e PDF de todos os e-books, em PDF-Geral/
│   ├── verificar_links.py                 # links relativos dos .md (usado no CI)
│   └── comum.py                           # leitura do ebook.toml e descoberta dos e-books
├── template/
│   ├── ebook-template.html                # fonte única do CSS e da estrutura
│   ├── fontes/                            # IBM Plex (OFL), embutida nos HTML gerados
│   ├── DESIGN-SYSTEM.md                   # cores, tipografia, componentes e regras de impressão
│   ├── PROMPT.md                          # prompt para criar um e-book novo no padrão
│   └── legado/prompt-antigo.md            # prompt anterior (visual livre por e-book)
├── aws-aif-c01/
│   ├── material.md                        # conteúdo
│   ├── ebook.toml                         # capa, síntese, rodapé e nome do PDF
│   ├── ebook.html                         # gerado; não edite à mão
│   └── README.md
├── aws-clf-c02/                           # mesmo formato
├── aws-dva-c02/                           # idem
├── aws-saa-c03/                           # idem
├── docker/                                # idem
├── kubernetes/                            # idem
├── gh-200/                                # idem, mais extra.css (ajustes de paginação)
├── aws-well-architected/                  # ebook.html editado à mão; ebook.toml sem `fonte`
├── PDF-Geral/                             # PDFs de todos os e-books
├── .github/workflows/verificar.yml        # CI: HTML em sincronia com o Markdown e links
├── requirements.txt
└── PLANO-DE-MELHORIAS.md                  # plano de reorganização do repositório
```

## Requisitos

- Python 3.9+
- Google Chrome ou Chromium, para gerar o PDF. Se não for encontrado automaticamente, use `--chrome /caminho/para/chrome` ou a variável `CHROME_BIN`. Não precisa de rede: as fontes estão no repositório.
- Pacotes Python:

  ```bash
  python3 -m pip install -r requirements.txt
  ```

  `markdown-it-py` e `beautifulsoup4` geram o HTML; `pymupdf` numera as páginas do sumário no PDF; `tomli` lê o `ebook.toml` no Python 3.9 e 3.10.

## Gerar os e-books

Os comandos funcionam a partir de qualquer pasta. Os e-books são identificados pelo caminho da pasta ou por um trecho do nome (`docker`, `saa`, `gh-200`).

### Todos de uma vez

```bash
python3 ferramentas/gerar_todos.py
```

Encontra sozinho toda pasta que tem um `ebook.toml` (um e-book novo entra automaticamente), regenera o `ebook.html` quando o `ebook.toml` indica a `fonte` em Markdown e salva todos os PDFs em [`PDF-Geral/`](PDF-Geral/). Opções:

| Opção | Efeito |
| --- | --- |
| `--listar` | Mostra os e-books encontrados e o nome de cada PDF, sem gerar nada |
| `--apenas TEXTO` | Gera só as pastas cujo nome contém o texto (pode repetir: `--apenas docker --apenas dva`) |
| `--sem-html` | Não regenera o `ebook.html`; só gera o PDF a partir do HTML atual |
| `--destino PASTA` | Salva em outra pasta no lugar de `PDF-Geral/` |
| `--chrome CAMINHO` | Caminho do Chrome/Chromium |

Um erro em um e-book não interrompe os outros; no fim, o script lista os que falharam e sai com código 1.

### Passo a passo

```bash
python3 ferramentas/gerar_ebook.py docker      # só o HTML (sem argumento: todos)
python3 ferramentas/gerar_pdf.py docker        # só o PDF, em docker/output/pdf/
python3 ferramentas/gerar_pdf.py docker --output /tmp/docker.pdf
```

O `gerar_ebook.py` falha, sem gravar nada, se o HTML perder algum texto ou bloco de código do Markdown, se houver `id` duplicado ou link interno sem destino.

No **Well-Architected**, o conteúdo fica direto no `ebook.html`; só o passo do PDF se aplica (`python3 ferramentas/gerar_pdf.py well-architected`).

Os detalhes de cada e-book estão no `README.md` da pasta.

### Ao atualizar um e-book

1. Edite o `material.md` e, se a revisão mudou o conteúdo, a data em `[capa] atualizado` do `ebook.toml` (ex.: `"outubro de 2026"`). Ela aparece no topo da capa; nada a atualiza sozinho.
2. Rode `python3 ferramentas/gerar_todos.py --apenas <pasta>` e commite o `material.md`, o `ebook.toml`, o `ebook.html` e o PDF juntos.

O CI ([`.github/workflows/verificar.yml`](.github/workflows/verificar.yml)) roda a cada push e pull request: regenera os HTML com Python 3.9 e com a versão mais recente e falha se algum `ebook.html` commitado estiver diferente do gerado, ou se um `.md` tiver link relativo quebrado. Os PDFs não são gerados no CI: no Linux, os caracteres que caem em fonte de reserva (setas, `≥`) mudam a largura e, em alguns e-books, a paginação. Gere os PDFs sempre no macOS.

## Criar um e-book novo

1. Abra [`template/PROMPT.md`](template/PROMPT.md), preencha o bloco `<dados>` (pasta, título, capa, rodapé) e cole o material em `<conteudo>`.
2. Envie o prompt ao Claude neste repositório. Ele cria a pasta com o `material.md` e o `ebook.toml`, sem script próprio e sem alterar o visual.
3. Gere o HTML e o PDF:

   ```bash
   python3 ferramentas/gerar_todos.py --apenas "nova-pasta"
   ```

O padrão visual está documentado em [`template/DESIGN-SYSTEM.md`](template/DESIGN-SYSTEM.md). A numeração é hierárquica em todos os e-books: capítulo (`1`), seção (`1.1`) e tópico (`1.1.1`), igual no sumário e no corpo. O `gerar_ebook.py` cria os números sozinho; não os escreva à mão nos títulos do Markdown (a exceção é o `## N. Título` dos capítulos quando o `ebook.toml` usa `numeracao = "markdown"`). Todos os PDFs levam no rodapé de cada página o nome do e-book e `Erik Nathan (eriknathan.me)`.

> O [`template/legado/prompt-antigo.md`](template/legado/prompt-antigo.md) é a versão anterior do prompt: ele pede um visual diferente para cada e-book. Para seguir o padrão, use `template/PROMPT.md`.

## Autor

Erik Nathan · [eriknathan.me](https://eriknathan.me/)
