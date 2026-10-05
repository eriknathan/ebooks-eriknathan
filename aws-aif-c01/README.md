# Guia de revisão AIF-C01

- `material.md`: fonte do conteúdo. Cobre as 14 tarefas do guia oficial do AWS Certified AI Practitioner (AIF-C01), versão 1.1 (abril de 2026), com IA agêntica, MCP, Bedrock AgentCore, Strands Agents, Kiro e Amazon Quick. Tem tabelas de decisão rápida por capítulo, padrões recorrentes, mapa de domínios, flashcards e questões de múltipla resposta, ordenação e correspondência. Serviços e disponibilidade foram conferidos na documentação oficial em setembro de 2026, incluindo a entrada em modo de manutenção, em 30/jul/2026, do Bedrock Agents Classic, do Kendra, do Q Business e de recursos do SageMaker AI (Clarify, Model Monitor, Ground Truth, A2I).
- `ebook.toml`: capa, síntese, rodapé e nome do PDF.
- `ebook.html`: gerado por [`ferramentas/gerar_ebook.py`](../ferramentas/gerar_ebook.py); edite o Markdown ou o `ebook.toml`, nunca este arquivo.
- [`PDF-Geral/aif-c01-guia-de-revisao.pdf`](../PDF-Geral/aif-c01-guia-de-revisao.pdf): versão para impressão (A4).

Para regenerar o HTML e o PDF, a partir da raiz: `python3 ferramentas/gerar_todos.py --apenas aif`. Os outros comandos estão no [README da raiz](../README.md#gerar-os-e-books). O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md).
