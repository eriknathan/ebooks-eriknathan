# Guia de revisão DVA-C02

- `material.md`: fonte do conteúdo. Cobre as 13 tarefas do guia oficial do AWS Certified Developer - Associate (DVA-C02), versão 2.1. Os capítulos tratam de Lambda, API Gateway, DynamoDB, armazenamento e cache, mensageria e Step Functions, IAM/Cognito, KMS e segredos, SAM/CloudFormation/CDK, testes, CI/CD, observabilidade, otimização e desenvolvimento com IA. Cada capítulo tem tabelas de números, decisão rápida e pegadinhas; o fim do guia traz flashcards e questões de múltipla resposta. Limites e comportamentos foram conferidos na documentação oficial em setembro de 2026, incluindo as mudanças de 2024 a 2026 (payloads de 1 MB no Lambda assíncrono, SQS, SNS e EventBridge, X-Ray SDK em manutenção, CodeCommit de volta, ECS com blue/green nativo).
- **DVA-C03**: o DVA-C02 pode ser feito até 30/nov/2026; o DVA-C03 começa em 1º/dez/2026, e o guia oficial dele sai em 27/out/2026. A seção 14 resume o que foi anunciado. Quando o guia sair, revise o mapa de cobertura (seção 18) e a lista de serviços.
- `gerar_ebook.py`: converte o Markdown em `ebook.html`. Os títulos `##` viram capítulos, `###` viram seções numeradas no sumário (1.1, 1.2…) e `####` viram tópicos. Os callouts `> [!question]-` viram flashcards. Em relação aos outros guias, tem estilo para blocos de código (`buildspec.yml`, EMF, consultas do Logs Insights).
- `ebook.html`: e-book autônomo, com sumário, tabelas e flashcards expansíveis. É gerado pelo script: edite o Markdown ou o `gerar_ebook.py`, nunca este arquivo.
- `output/pdf/dva-c02-guia-de-revisao.pdf`: versão para impressão (A4).

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

O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md). Os scripts são cópias adaptadas dos do [`CLF-C02`](../CLF-C02/).
