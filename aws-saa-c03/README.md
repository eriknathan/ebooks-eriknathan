# Guia de revisão SAA-C03

- `material.md`: fonte do conteúdo. É o material revisado, com o mapa das 14 tarefas oficiais, o método para cenários, as correções de disponibilidade de serviços em 2026 e as questões de múltipla resposta.
- `ebook.toml`: capa, síntese, rodapé e nome do PDF.
- `ebook.html`: gerado por [`ferramentas/gerar_ebook.py`](../ferramentas/gerar_ebook.py); edite o Markdown ou o `ebook.toml`, nunca este arquivo.
- [`PDF-Geral/saa-c03-guia-de-revisao.pdf`](../PDF-Geral/saa-c03-guia-de-revisao.pdf): versão para impressão (A4).

Os links no formato `[[nota do Obsidian]]` foram mantidos como texto porque os arquivos das notas não vieram com o material.

Para regenerar o HTML e o PDF, a partir da raiz: `python3 ferramentas/gerar_todos.py --apenas saa`. Os outros comandos estão no [README da raiz](../README.md#gerar-os-e-books). O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md).
