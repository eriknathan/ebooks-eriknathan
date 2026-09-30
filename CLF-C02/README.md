# Guia de revisão CLF-C02

- `material.md`: fonte do conteúdo. Cobre as 19 tarefas do guia oficial do AWS Certified Cloud Practitioner (CLF-C02), com tabelas de decisão rápida por capítulo, padrões recorrentes, mapa de domínios, flashcards e questões de múltipla resposta. Preços, planos de suporte (Business Support+, Enterprise, Unified Operations) e Free Tier foram conferidos na documentação oficial em setembro de 2026.
- `gerar_ebook.py`: converte o Markdown em `ebook.html`. Os títulos `##` viram capítulos, `###` viram seções numeradas no sumário (1.1, 1.2…) e `####` viram tópicos. Os callouts `> [!question]-` viram flashcards.
- `ebook.html`: e-book autônomo, com sumário, tabelas e flashcards expansíveis. É gerado pelo script: edite o Markdown ou o `gerar_ebook.py`, nunca este arquivo.
- `output/pdf/clf-c02-guia-de-revisao.pdf`: versão para impressão (A4).

Para atualizar o HTML depois de editar o Markdown:

```bash
python3 -m pip install markdown-it-py beautifulsoup4
python3 gerar_ebook.py
```

Para regenerar o PDF:

```bash
python3 gerar_pdf.py
```

O script usa o Google Chrome/Chromium em modo headless e PyMuPDF para inserir no sumário os números das páginas calculados no próprio PDF. Instale com `python3 -m pip install pymupdf`. Opções: `--input`, `--output` e `--chrome /caminho/do/executável` (ou a variável `CHROME_BIN`).

O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md). Os scripts são cópias adaptadas dos do [`SAA-C03`](../SAA-C03/): muda só o texto da capa, os domínios, o rodapé e a síntese final.
