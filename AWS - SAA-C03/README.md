# Guia de revisão SAA-C03

- `material-original.md`: fonte do conteúdo. É o material revisado, com o mapa das 14 tarefas oficiais, o método para cenários, as correções de disponibilidade de serviços em 2026 e as questões de múltipla resposta. O nome foi mantido para preservar o fluxo de geração.
- `gerar_ebook.py`: converte o Markdown em `ebook.html`. Os títulos `##` viram capítulos, `###` viram seções numeradas no sumário (1.1, 1.2…) e `####` viram tópicos. Os callouts `> [!question]-` viram flashcards.
- `ebook.html`: e-book autônomo, com sumário, tabelas e flashcards expansíveis. É gerado pelo script: edite o Markdown ou o `gerar_ebook.py`, nunca este arquivo.
- `output/pdf/saa-c03-guia-de-revisao.pdf`: versão para impressão (A4).

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

O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md).

Os links no formato `[[nota do Obsidian]]` foram mantidos como texto porque os arquivos das notas não vieram com o material.
