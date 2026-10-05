# Guia de revisão DVA-C02

- `material.md`: fonte do conteúdo. Cobre as 13 tarefas do guia oficial do AWS Certified Developer - Associate (DVA-C02), versão 2.1. Os capítulos tratam de Lambda, API Gateway, DynamoDB, armazenamento e cache, mensageria e Step Functions, IAM/Cognito, KMS e segredos, SAM/CloudFormation/CDK, testes, CI/CD, observabilidade, otimização e desenvolvimento com IA. Cada capítulo tem tabelas de números, decisão rápida e pegadinhas; o fim do guia traz flashcards e questões de múltipla resposta. Limites e comportamentos foram conferidos na documentação oficial em setembro de 2026, incluindo as mudanças de 2024 a 2026 (payloads de 1 MB no Lambda assíncrono, SQS, SNS e EventBridge, X-Ray SDK em manutenção, CodeCommit de volta, ECS com blue/green nativo).
- **DVA-C03**: o DVA-C02 pode ser feito até 30/nov/2026; o DVA-C03 começa em 1º/dez/2026, e o guia oficial dele sai em 27/out/2026. A seção 14 resume o que foi anunciado. Quando o guia sair, revise o mapa de cobertura (seção 18) e a lista de serviços.
- `ebook.toml`: capa, síntese, rodapé e nome do PDF.
- `ebook.html`: gerado por [`ferramentas/gerar_ebook.py`](../ferramentas/gerar_ebook.py); edite o Markdown ou o `ebook.toml`, nunca este arquivo.
- [`PDF-Geral/dva-c02-guia-de-revisao.pdf`](../PDF-Geral/dva-c02-guia-de-revisao.pdf): versão para impressão (A4).

Para regenerar o HTML e o PDF, a partir da raiz: `python3 ferramentas/gerar_todos.py --apenas dva`. Os outros comandos estão no [README da raiz](../README.md#gerar-os-e-books). O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md).
