# Guia de revisão AWS Well-Architected Framework

- `ebook.html`: fonte do conteúdo. Diferente dos outros e-books, este HTML é editado diretamente: tem capa, sumário dos 10 módulos do treinamento AWS Well-Architected (o último é o questionário) e 48 perguntas expansíveis.
- `material.md`: versão do conteúdo em Markdown, exportada do HTML sem os componentes visuais (cards, pilares, linha do tempo, passos e quizzes viram texto corrido). **Não** alimenta o `ebook.html`; uma mudança feita só aqui não aparece no e-book. Os motivos para não migrar este e-book para o fluxo Markdown estão no item 2.6 do [plano de melhorias](../PLANO-DE-MELHORIAS.md).
- `ebook.toml`: só o nome do PDF. Sem o campo `fonte`, as ferramentas tratam o `ebook.html` como editado à mão e geram apenas o PDF.
- [`PDF-Geral/ebook-aws-well-architected.pdf`](../PDF-Geral/ebook-aws-well-architected.pdf): versão para impressão (A4).

Para regenerar o PDF depois de editar o `ebook.html`, a partir da raiz: `python3 ferramentas/gerar_todos.py --apenas well-architected` (grava em `PDF-Geral/`). Os outros comandos estão no [README da raiz](../README.md#gerar-os-e-books).

O visual segue a estrutura do padrão do repositório (capa, sumário por módulo, rodapé), mas com CSS e tipografia próprios (Fraunces e Source Sans 3) no `<head>` do HTML; ele não usa o [`template/ebook-template.html`](../template/ebook-template.html).
