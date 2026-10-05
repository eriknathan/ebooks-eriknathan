# Guia de estudo Docker

- `material.md`: fonte do conteúdo. São 16 capítulos: fundamentos e arquitetura, ciclo de vida de contêineres, imagens e registries, Dockerfile, BuildKit/Buildx/Bake, redes, armazenamento, Compose, segurança, recursos e troubleshooting, Swarm e Kubernetes, produção e CI/CD, preparação para o DCA, pegadinhas, referência de comandos e flashcards. Cada capítulo de conteúdo termina com uma tabela de decisão rápida. Versões e limites foram conferidos na documentação oficial em setembro de 2026 (Docker Engine 29.8, Compose 5.5, limites de pull do Docker Hub, GitHub Actions do Docker), incluindo as mudanças recentes: containerd image store como padrão no Engine 29, Compose v5 com builds via Bake, Docker Hardened Images gratuitas e Docker Content Trust aposentado.
- `ebook.toml`: capa, síntese, rodapé e nome do PDF.
- `ebook.html`: gerado por [`ferramentas/gerar_ebook.py`](../ferramentas/gerar_ebook.py); edite o Markdown ou o `ebook.toml`, nunca este arquivo.
- [`PDF-Geral/docker-guia-de-estudo.pdf`](../PDF-Geral/docker-guia-de-estudo.pdf): versão para impressão (A4).

Diferente dos guias de certificação AWS, este não é organizado pelos domínios de um exame, mas cobre o roteiro do **Docker Certified Associate (DCA)**: o capítulo 13 liga cada objetivo da prova ao ponto do guia que o cobre e explica os tópicos legados que ela ainda cobra (UCP/DTR, Docker Content Trust, devicemapper) e o Kubernetes pedido. A capa mostra os cinco blocos do guia no lugar dos pesos de domínio, e não tem selo de nível.

Para regenerar o HTML e o PDF, a partir da raiz: `python3 ferramentas/gerar_todos.py --apenas docker`. Os outros comandos estão no [README da raiz](../README.md#gerar-os-e-books). O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md).
