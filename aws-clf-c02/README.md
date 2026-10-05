# Guia de revisão CLF-C02

- `material.md`: fonte do conteúdo. Cobre as 19 tarefas do guia oficial do AWS Certified Cloud Practitioner (CLF-C02), com tabelas de decisão rápida por capítulo, padrões recorrentes, mapa de domínios, flashcards e questões de múltipla resposta. Preços, planos de suporte (Business Support+, Enterprise, Unified Operations) e Free Tier foram conferidos na documentação oficial em setembro de 2026.
- `ebook.toml`: capa, síntese, rodapé e nome do PDF.
- `ebook.html`: gerado por [`ferramentas/gerar_ebook.py`](../ferramentas/gerar_ebook.py); edite o Markdown ou o `ebook.toml`, nunca este arquivo.
- [`PDF-Geral/clf-c02-guia-de-revisao.pdf`](../PDF-Geral/clf-c02-guia-de-revisao.pdf): versão para impressão (A4).

Para regenerar o HTML e o PDF, a partir da raiz: `python3 ferramentas/gerar_todos.py --apenas clf`. Os outros comandos estão no [README da raiz](../README.md#gerar-os-e-books). O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md).
