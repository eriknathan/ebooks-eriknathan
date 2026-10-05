# GH-200 — GitHub Actions Certification

O [material.md](material.md) é a fonte de conteúdo deste guia, desenvolvido a partir do roteiro fornecido e das referências oficiais consultadas em 30/09/2026.

O material contém:

- Mapa dos cinco domínios e método de estudo.
- Explicações de workflows, eventos, contextos, matrizes, contêineres, outputs, cache e artefatos.
- Reutilização, diagnóstico, autoria de ações e administração organizacional.
- Segurança, OIDC, ambientes, proveniência e otimização.
- Cinco laboratórios guiados, incluindo um pipeline completo com falha controlada.
- Consulta rápida, simulado autoral de 25 questões com gabarito comentado, acompanhamento de erros e checklist final.

Os exemplos têm como referência o GitHub.com. Caminhos apresentados no texto indicam onde criar os arquivos em um repositório de laboratório; eles não instalam workflows neste repositório de ebooks. Os simulados externos mencionados no roteiro original não foram fornecidos e não são apresentados como arquivos existentes.

## Arquivos e geração

- [material.md](material.md): fonte editável.
- [ebook.toml](ebook.toml): capa, síntese, rodapé e nome do PDF.
- [extra.css](extra.css): ajustes de paginação só deste e-book (blocos longos de YAML continuam na folha seguinte, seções compactadas).
- [ebook.html](ebook.html): versão para leitura no navegador, com sumário e questões expansíveis. Gerado por [`ferramentas/gerar_ebook.py`](../ferramentas/gerar_ebook.py); não edite à mão.
- [PDF A4](../PDF-Geral/gh-200-guia-de-estudo.pdf): versão para impressão, com sumário numerado e links.

Edite o `material.md`. Os títulos `##` definem capítulos, os `###` definem seções e os `####` definem tópicos. O gerador acrescenta a numeração automaticamente, transforma os parágrafos `Q01.` seguidos de alternativas em questões, preserva o conteúdo e os blocos de código e verifica os links internos. O visual segue o [design system](../template/DESIGN-SYSTEM.md) e o [template do projeto](../template/ebook-template.html).

Para regenerar o HTML e o PDF, a partir da raiz:

```bash
python3 ferramentas/gerar_todos.py --apenas GH-200
```

Os requisitos e os demais comandos estão no [README da raiz](../README.md#requisitos).

## Verificação dos exemplos

Os 22 blocos YAML foram analisados, e os sete workflows completos passaram no `actionlint`. A lógica dos exemplos JavaScript e composto foi executada localmente com entradas válidas e inválidas. O Markdown e os links locais também foram conferidos. Os workflows não foram executados no GitHub; os laboratórios indicam os pré-requisitos e resultados esperados para essa etapa.

## Manutenção

O material inclui links oficiais junto às regras e um índice de fontes. Ao atualizar o guia, confira o [programa GH-200](https://learn.microsoft.com/pt-br/credentials/certifications/resources/study-guides/gh-200), revise exemplos e gabaritos afetados e registre a nova data de consulta.
