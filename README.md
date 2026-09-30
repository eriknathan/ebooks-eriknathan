# E-books de estudo AWS

Guias de revisão em HTML e PDF, todos com o mesmo padrão visual: capa, sumário por capítulo, flashcards e versão A4 para impressão.

| E-book | Pasta | PDF |
| --- | --- | --- |
| AWS Well-Architected Framework | [`aws-well-architected-framework/`](aws-well-architected-framework/) | [`pdf/ebook-aws-well-architected.pdf`](aws-well-architected-framework/pdf/ebook-aws-well-architected.pdf) |
| AWS Certified Solutions Architect – Associate (SAA-C03) | [`SAA-C03/`](SAA-C03/) | [`output/pdf/saa-c03-guia-de-revisao.pdf`](SAA-C03/output/pdf/saa-c03-guia-de-revisao.pdf) |
| AWS Certified Cloud Practitioner (CLF-C02) | [`CLF-C02/`](CLF-C02/) | [`output/pdf/clf-c02-guia-de-revisao.pdf`](CLF-C02/output/pdf/clf-c02-guia-de-revisao.pdf) |
| AWS Certified AI Practitioner (AIF-C01) | [`AIF-C01/`](AIF-C01/) | [`output/pdf/aif-c01-guia-de-revisao.pdf`](AIF-C01/output/pdf/aif-c01-guia-de-revisao.pdf) |
| AWS Certified Developer – Associate (DVA-C02) | [`DVA-C02/`](DVA-C02/) | [`output/pdf/dva-c02-guia-de-revisao.pdf`](DVA-C02/output/pdf/dva-c02-guia-de-revisao.pdf) |

## Estrutura

```text
.
├── template/                        # padrão para novos e-books
│   ├── ebook-template.html          # HTML-base com todo o CSS e os componentes
│   ├── DESIGN-SYSTEM.md             # cores, tipografia, componentes e regras de impressão
│   ├── PROMPT.md                    # prompt para gerar um e-book novo no padrão
│   └── gerar_pdf.py                 # gera o PDF de qualquer HTML
├── aws-well-architected-framework/
│   ├── ebook.html                   # e-book (editado diretamente)
│   ├── gerar_pdf.py
│   └── pdf/
├── SAA-C03/
│   ├── material-original.md         # fonte do conteúdo
│   ├── gerar_ebook.py               # Markdown → ebook.html
│   ├── ebook.html                   # gerado; não edite à mão
│   ├── gerar_pdf.py
│   └── output/pdf/
├── CLF-C02/                         # mesmo fluxo do SAA-C03
│   ├── material.md                  # fonte do conteúdo
│   ├── gerar_ebook.py               # Markdown → ebook.html
│   ├── ebook.html                   # gerado; não edite à mão
│   ├── gerar_pdf.py
│   └── output/pdf/
├── AIF-C01/                         # mesmo fluxo do SAA-C03
│   ├── material.md                  # fonte do conteúdo
│   ├── gerar_ebook.py               # Markdown → ebook.html
│   ├── ebook.html                   # gerado; não edite à mão
│   ├── gerar_pdf.py
│   └── output/pdf/
├── DVA-C02/                         # mesmo fluxo do SAA-C03
│   ├── material.md                  # fonte do conteúdo
│   ├── gerar_ebook.py               # Markdown → ebook.html
│   ├── ebook.html                   # gerado; não edite à mão
│   ├── gerar_pdf.py
│   └── output/pdf/
└── prompt.md                        # prompt antigo (visual livre por e-book)
```

## Requisitos

- Python 3.9+
- Google Chrome ou Chromium, para gerar o PDF. Se não for encontrado automaticamente, use `--chrome /caminho/para/chrome` ou a variável `CHROME_BIN`.
- Só para o SAA-C03, o CLF-C02, o AIF-C01 e o DVA-C02: `python3 -m pip install markdown-it-py beautifulsoup4`

## Gerar os PDFs

Rode a partir da raiz do repositório.

**Well-Architected**: o conteúdo fica direto no `ebook.html`.

```bash
python3 aws-well-architected-framework/gerar_pdf.py \
  --output aws-well-architected-framework/pdf/ebook-aws-well-architected.pdf
```

Sem `--output`, o script grava em `aws-well-architected-framework/output/pdf/`, e não na pasta `pdf/` onde fica o PDF versionado.

**SAA-C03**: edite o `material-original.md` e gere o HTML antes do PDF.

```bash
cd SAA-C03
python3 gerar_ebook.py
python3 gerar_pdf.py
```

Os detalhes do SAA-C03 estão em [`SAA-C03/README.md`](SAA-C03/README.md).

**CLF-C02**, **AIF-C01** e **DVA-C02**: mesmo fluxo, com o conteúdo em `material.md`.

```bash
cd CLF-C02   # ou AIF-C01, DVA-C02
python3 gerar_ebook.py
python3 gerar_pdf.py
```

Os detalhes estão em [`CLF-C02/README.md`](CLF-C02/README.md), [`AIF-C01/README.md`](AIF-C01/README.md) e [`DVA-C02/README.md`](DVA-C02/README.md).

## Criar um e-book novo

1. Abra [`template/PROMPT.md`](template/PROMPT.md), preencha o bloco `<dados>` (pasta, título, capa, rodapé) e cole o material em `<conteudo>`.
2. Envie o prompt ao Claude neste repositório. Ele copia o [`ebook-template.html`](template/ebook-template.html) para a nova pasta e preenche o conteúdo sem alterar o visual.
3. Gere o PDF:

   ```bash
   python3 template/gerar_pdf.py nova-pasta/ebook.html
   ```

   O PDF sai em `nova-pasta/output/pdf/ebook.pdf`. Para outro nome, passe o caminho como segundo argumento.

O padrão visual está documentado em [`template/DESIGN-SYSTEM.md`](template/DESIGN-SYSTEM.md). Todos os PDFs levam no rodapé de cada página o nome do e-book e `Erik Nathan (eriknathan.me)`.

> O [`prompt.md`](prompt.md) da raiz é a versão anterior: ele pede um visual diferente para cada e-book. Para seguir o padrão, use `template/PROMPT.md`.

## Autor

Erik Nathan · [eriknathan.me](https://eriknathan.me/)
