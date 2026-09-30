#!/usr/bin/env python3
"""Gera o ebook GH-200 com o conteúdo integral do material e o template do projeto."""

from __future__ import annotations

import html
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag
from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "material.md"
OUTPUT = ROOT / "ebook.html"
TEMPLATE = ROOT.parent / "template" / "ebook-template.html"
MARKDOWN = MarkdownIt("commonmark", {"html": True}).enable("table")


@dataclass
class Heading:
    title: str
    anchor: str
    number: str
    level: int
    children: list[Heading] = field(default_factory=list)


def slug(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    plain = "".join(c for c in normalized if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")


def content_text(root: Tag | BeautifulSoup) -> str:
    """Normaliza só espaços; usado para assegurar a preservação do texto."""
    return re.sub(r"\s+", " ", root.get_text(" ", strip=True)).strip()


def organize_content(rendered: str) -> tuple[Tag, list[Heading]]:
    soup = BeautifulSoup(rendered, "html.parser")
    expected_text = content_text(soup)
    expected_code = [node.get_text() for node in soup.select("pre code")]
    container = soup.new_tag("main", attrs={"id": "conteudo", "class": "book-content"})
    chapters: list[Heading] = []
    used: set[str] = set()
    chapter = subsection = topic = None
    section_count = topic_count = 0
    preamble: list[Tag] = []

    for node in list(soup.contents):
        if isinstance(node, NavigableString) or not isinstance(node, Tag):
            continue
        if node.name == "h1":
            node.name = "p"
            bold = soup.new_tag("strong")
            for child in list(node.contents):
                bold.append(child.extract())
            node.append(bold)
        if node.name in ("h2", "h3", "h4"):
            level = int(node.name[1])
            title = node.get_text(" ", strip=True)
            base = slug(title)
            anchor = base
            suffix = 2
            while anchor in used:
                anchor = f"{base}-{suffix}"
                suffix += 1
            used.add(anchor)
            node["id"] = anchor
            if level == 2:
                section_count = topic_count = 0
                number = str(len(chapters) + 1)
                heading = Heading(title, anchor, number, level)
                chapters.append(heading)
                chapter = soup.new_tag("section", attrs={"class": "chapter", "aria-labelledby": anchor})
                header = soup.new_tag("div", attrs={"class": "chapter-head"})
                kicker = soup.new_tag("span", attrs={"class": "kicker", "data-generated": "true"})
                kicker.string = f"Capítulo {number}"
                header.extend([kicker, node.extract()])
                chapter.append(header)
                container.append(chapter)
                subsection = topic = None
                if preamble:
                    # Mantém o prefácio antes do primeiro título, na ordem da fonte.
                    pref = soup.new_tag("div", attrs={"class": "callout"})
                    body = soup.new_tag("div", attrs={"class": "body"})
                    for item in preamble:
                        body.append(item.extract())
                    pref.append(body)
                    container.insert(0, pref)
                    preamble.clear()
            elif level == 3:
                if chapter is None:
                    raise ValueError(f"Seção sem capítulo: {title}")
                section_count += 1
                topic_count = 0
                number = f"{len(chapters)}.{section_count}"
                subsection = soup.new_tag("section", attrs={"class": "section", "aria-labelledby": anchor})
                header = soup.new_tag("div", attrs={"class": "section-head"})
                label = soup.new_tag("span", attrs={"class": "sec-label", "data-generated": "true"})
                label.string = number
                header.extend([label, node.extract()])
                subsection.append(header)
                chapter.append(subsection)
                topic = None
                chapters[-1].children.append(Heading(title, anchor, number, level))
            else:
                if subsection is None:
                    raise ValueError(f"Tópico sem seção: {title}")
                topic_count += 1
                number = f"{len(chapters)}.{section_count}.{topic_count}"
                topic = soup.new_tag("section", attrs={"class": "topic", "aria-labelledby": anchor})
                label = soup.new_tag("span", attrs={"class": "topic-num", "data-generated": "true"})
                label.string = number + " "
                node.insert(0, label)
                topic.append(node.extract())
                subsection.append(topic)
                chapters[-1].children.append(Heading(title, anchor, number, level))
            continue
        destination = topic or subsection or chapter
        if destination is None:
            preamble.append(node)
        else:
            destination.append(node.extract())

    for table in container.find_all("table"):
        heading = table.find_previous(["h4", "h3", "h2"])
        description = heading.get_text(" ", strip=True) if heading else "Tabela de estudo"
        caption = soup.new_tag("caption", attrs={"class": "sr-only", "data-generated": "true"})
        caption.string = description
        table.insert(0, caption)
        for cell in table.select("th"):
            cell["scope"] = "col"
        table.wrap(soup.new_tag("div", attrs={"class": "table-scroll", "tabindex": "0", "role": "region", "aria-label": description}))

    # O gabarito continua no ponto original, após todas as perguntas.
    for paragraph in list(container.find_all("p")):
        if not re.match(r"^Q\d{2}\.", paragraph.get_text(strip=True)):
            continue
        options = paragraph.find_next_sibling()
        if options is None or options.name != "ul":
            raise ValueError("Questão sem alternativas")
        question = soup.new_tag("details", attrs={"class": "flashcard", "open": ""})
        paragraph.insert_before(question)
        paragraph.name = "summary"
        question.append(paragraph.extract())
        options["class"] = "flashcard-options"
        for option in options.find_all("li", recursive=False):
            body = soup.new_tag("span")
            for child in list(option.contents):
                body.append(child.extract())
            option.append(body)
        question.append(options.extract())

    verification = BeautifulSoup(str(container), "html.parser")
    for generated in verification.select("[data-generated]"):
        generated.decompose()
    if content_text(verification) != expected_text:
        raise ValueError("A organização alterou o conteúdo textual do Markdown")
    if [node.get_text() for node in container.select("pre code")] != expected_code:
        raise ValueError("Um bloco de código foi alterado durante a conversão")
    return container, chapters


def build_toc(chapters: list[Heading]) -> str:
    groups = []
    for chapter in chapters:
        label = html.escape(f"Capítulo {chapter.number} — {chapter.title}")
        if not chapter.children:
            groups.append(f'<div class="toc-group"><a class="toc-group-title" href="#{chapter.anchor}">{label}</a></div>')
            continue
        items = []
        for child in chapter.children:
            css = ' class="toc-topic"' if child.level == 4 else ""
            items.append(f'<li{css}><a href="#{child.anchor}"><span class="n">{child.number}</span> {html.escape(child.title)}</a></li>')
        groups.append(f'<details class="toc-group"><summary class="toc-group-title">{label}</summary><ul class="toc-list">{"".join(items)}</ul></details>')
    return "\n".join(groups)


def build_html(content: Tag, chapters: list[Heading]) -> str:
    template = BeautifulSoup(TEMPLATE.read_text(encoding="utf-8"), "html.parser")
    css = template.style.string.replace("{{RODAPE}}", "GH-200 / GUIA DE ESTUDO")
    # Blocos de código seguem o tratamento usado no ebook Docker.
    # Blocos extensos podem continuar na folha seguinte, preservando o YAML.
    css += r'''
  .book-content pre{margin:16px 0 22px;padding:13px 16px;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--teal);border-radius:0 4px 4px 0;overflow-x:auto;font:.8rem/1.55 var(--mono);color:var(--ink);hyphens:none}
  .book-content pre code{background:none;padding:0;font-size:inherit;overflow-wrap:normal;hyphens:none}
  .book-content hr{border:0;border-top:1px solid var(--line);margin:30px 0}
  @media print{
    .toc-list a{padding-right:24px}
    .book-content> .callout:first-child{margin-top:0}
    .book-content> .callout:first-child+.chapter{break-before:auto}
    .section{margin-top:14px;padding-top:10px}
    .section-head{margin-bottom:10px}
    .section-head,.chapter-head,.topic>h4{break-inside:avoid;break-after:avoid}
    .table-scroll{margin:14px 0 18px}
    thead{break-after:avoid}
    tbody tr:first-child{break-before:avoid}
    .chapter[aria-labelledby="dominio-4-gerenciar-o-github-actions-para-a-organizacao"] th,
    .chapter[aria-labelledby="dominio-4-gerenciar-o-github-actions-para-a-organizacao"] td{padding-top:4px;padding-bottom:4px}
    .section:has(#versionamento-releases-e-imutabilidade){break-inside:avoid}
    .book-content pre{margin:12px 0 16px;white-space:pre-wrap;overflow:visible;overflow-wrap:anywhere;break-inside:auto;font-size:7.6pt;line-height:1.4;box-decoration-break:clone}
    .book-content pre code{overflow-wrap:anywhere}
    .book-content hr{display:none}
    .closing{margin-top:18px;padding:18px 22px}
  }
'''
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Guia GH-200 de GitHub Actions: cinco domínios, exemplos YAML, cinco laboratórios e simulado autoral com 25 questões comentadas.">
<title>GH-200 — GitHub Actions Certification — Guia de estudo</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
<article class="book">
  <header class="cover">
    <div class="cover-top"><span>Guia de estudo</span><span>Atualizado em setembro de 2026</span></div>
    <div class="cover-main">
      <span class="cover-code">GH<span class="dash">-</span>200</span>
      <span class="cover-exam">GitHub Actions Certification</span>
      <h1>Automação, segurança e entrega contínua</h1>
      <p class="cover-subtitle">Preparação para os cinco domínios do exame, com exemplos de workflows, laboratórios guiados, consulta rápida e simulado comentado.</p>
      <p class="cover-author"><strong>Erik Nathan</strong><a href="https://eriknathan.me/">eriknathan.me</a></p>
    </div>
    <div class="cover-bottom">
      <p class="cover-bottom-label">Estudo, prática e revisão</p>
      <div class="highlight-grid">
        <div class="highlight"><strong>05</strong><span>Domínios do exame</span></div>
        <div class="highlight"><strong>05</strong><span>Laboratórios guiados</span></div>
        <div class="highlight"><strong>25</strong><span>Questões comentadas</span></div>
      </div>
    </div>
  </header>
  <nav class="toc" id="sumario" aria-label="Sumário">
    <h2>Sumário</h2>
    <p class="toc-intro">Abra um capítulo para ir diretamente ao tópico que deseja revisar.</p>
    {build_toc(chapters)}
    <p class="toc-ending"><a href="#sintese-de-revisao">Ir para a síntese de revisão</a></p>
  </nav>
  {content}
  <section class="closing" id="sintese-de-revisao" aria-labelledby="sintese-title">
    <h2 id="sintese-title">Síntese de revisão</h2>
    <p>Reorganização dos pontos centrais do material para a última revisão.</p>
    <ul>
      <li>Leia eventos, filtros, dependências e condições antes de prever a execução.</li>
      <li>Escolha outputs para pequenos valores, artefatos para arquivos e cache para reaproveitar trabalho.</li>
      <li>Distinga templates, workflows reutilizáveis e ações compostas pelo que cada um encapsula.</li>
      <li>Administre runners, variáveis, segredos e políticas conforme o acesso necessário.</li>
      <li>Revise permissões, entradas não confiáveis, OIDC e proveniência antes de conceder acesso à implantação.</li>
      <li>Use os laboratórios e o simulado para identificar lacunas e explicar cada correção.</li>
    </ul>
  </section>
</article>
<script>
  (() => {{
    let opened = [];
    window.addEventListener('beforeprint', () => {{
      opened = [...document.querySelectorAll('details:not([open])')];
      opened.forEach(item => item.open = true);
    }});
    window.addEventListener('afterprint', () => {{
      opened.forEach(item => item.open = false);
      opened = [];
    }});
  }})();
</script>
</body>
</html>
'''


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    content, chapters = organize_content(MARKDOWN.render(source))
    output = build_html(content, chapters)
    soup = BeautifulSoup(output, "html.parser")
    ids = [node["id"] for node in soup.select("[id]")]
    if len(ids) != len(set(ids)):
        raise ValueError("IDs duplicados no HTML")
    for link in soup.select('a[href^="#"]'):
        if link["href"][1:] not in ids:
            raise ValueError(f"Link interno sem destino: {link['href']}")
    if re.search(r"\{\{[A-Z_]+\}\}", output):
        raise ValueError("Marcador de template não preenchido")
    OUTPUT.write_text(output, encoding="utf-8")
    print(f"Gerado {OUTPUT}: {len(chapters)} capítulos, {len(soup.select('details.flashcard'))} questões e {len(soup.select('pre'))} blocos de código")


if __name__ == "__main__":
    main()
