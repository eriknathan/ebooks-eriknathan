# Guia de estudo Docker

- `material.md`: fonte do conteúdo. São 16 capítulos: fundamentos e arquitetura, ciclo de vida de contêineres, imagens e registries, Dockerfile, BuildKit/Buildx/Bake, redes, armazenamento, Compose, segurança, recursos e troubleshooting, Swarm e Kubernetes, produção e CI/CD, preparação para o DCA, pegadinhas, referência de comandos e flashcards. Cada capítulo de conteúdo termina com uma tabela de decisão rápida. Versões e limites foram conferidos na documentação oficial em setembro de 2026 (Docker Engine 29.8, Compose 5.5, limites de pull do Docker Hub, GitHub Actions do Docker), incluindo as mudanças recentes: containerd image store como padrão no Engine 29, Compose v5 com builds via Bake, Docker Hardened Images gratuitas e Docker Content Trust aposentado.
- `gerar_ebook.py`: converte o Markdown em `ebook.html`. Os títulos `##` viram capítulos, `###` viram seções (1.1, 1.2…) e `####` viram tópicos (1.1.1, 1.1.2…). A numeração é gerada pelo script, no corpo e no sumário; não escreva números nos títulos `###` e `####` do Markdown. Capítulos sem número (como "Como usar este guia") ficam sem numeração nas seções. Os callouts `> [!question]-` viram flashcards. Tem estilo para blocos de código (Dockerfile, Compose, comandos).
- `ebook.html`: e-book autônomo, com sumário, tabelas e flashcards expansíveis. É gerado pelo script: edite o Markdown ou o `gerar_ebook.py`, nunca este arquivo.
- `output/pdf/docker-guia-de-estudo.pdf`: versão para impressão (A4).

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

Diferente dos guias de certificação AWS, este não é organizado pelos domínios de um exame, mas cobre o roteiro do **Docker Certified Associate (DCA)**: o capítulo 13 liga cada objetivo da prova ao ponto do guia que o cobre e explica os tópicos legados que ela ainda cobra (UCP/DTR, Docker Content Trust, devicemapper) e o Kubernetes pedido. A capa mostra os cinco blocos do guia no lugar dos pesos de domínio, e não tem selo de nível.

O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md). Os scripts são cópias adaptadas dos do DVA-C02.
