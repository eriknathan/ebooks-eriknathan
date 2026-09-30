# Guia de revisão AIF-C01

- `material.md`: fonte do conteúdo. Cobre as 14 tarefas do guia oficial do AWS Certified AI Practitioner (AIF-C01), versão 1.1 (abril de 2026), com IA agêntica, MCP, Bedrock AgentCore, Strands Agents, Kiro e Amazon Quick. Tem tabelas de decisão rápida por capítulo, padrões recorrentes, mapa de domínios, flashcards e questões de múltipla resposta, ordenação e correspondência. Serviços e disponibilidade foram conferidos na documentação oficial em setembro de 2026, incluindo a entrada em modo de manutenção, em 30/jul/2026, do Bedrock Agents Classic, do Kendra, do Q Business e de recursos do SageMaker AI (Clarify, Model Monitor, Ground Truth, A2I).
- `gerar_ebook.py`: converte o Markdown em `ebook.html`. Os títulos `##` viram capítulos, `###` viram seções numeradas no sumário (1.1, 1.2…) e `####` viram tópicos. Os callouts `> [!question]-` viram flashcards.
- `ebook.html`: e-book autônomo, com sumário, tabelas e flashcards expansíveis. É gerado pelo script: edite o Markdown ou o `gerar_ebook.py`, nunca este arquivo.
- `output/pdf/aif-c01-guia-de-revisao.pdf`: versão para impressão (A4).

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

O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md). Os scripts são cópias adaptadas dos do [`CLF-C02`](../CLF-C02/): muda o texto da capa, a grade de domínios (cinco colunas em vez de quatro), o rodapé e a síntese final.
