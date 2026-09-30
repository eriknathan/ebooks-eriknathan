#!/usr/bin/env python3
"""Converte o material Markdown do AIF-C01 em um e-book HTML autônomo."""

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
MARKDOWN = MarkdownIt("commonmark", {"html": True}).enable("table")


@dataclass
class Heading:
    title: str
    anchor: str
    level: int


@dataclass
class Chapter:
    heading: Heading
    children: list[Heading] = field(default_factory=list)


def slug(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(char for char in normalized if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")


def convert_flashcards(source: str) -> tuple[str, int]:
    """Troca callouts Obsidian por details sem alterar perguntas ou respostas."""
    lines = source.splitlines()
    result: list[str] = []
    count = 0
    index = 0
    while index < len(lines):
        match = re.match(r"^> \[!question\]-\s*(.*)$", lines[index])
        if not match:
            result.append(lines[index])
            index += 1
            continue
        question = match.group(1)
        index += 1
        answer_lines: list[str] = []
        while index < len(lines) and lines[index].startswith(">"):
            answer_lines.append(re.sub(r"^> ?", "", lines[index]))
            index += 1
        answer = "\n".join(answer_lines).strip()
        if not answer:
            raise ValueError(f"Flashcard sem resposta: {question}")
        result.extend(
            [
                "",
                '<details class="flashcard">',
                f"<summary>{MARKDOWN.renderInline(question)}</summary>",
                '<div class="flashcard-answer">',
                '<p class="answer-label">Resposta</p>',
                MARKDOWN.render(answer).strip(),
                "</div>",
                "</details>",
                "",
            ]
        )
        count += 1
    return "\n".join(result) + "\n", count


def organize_content(rendered: str) -> tuple[str, list[Chapter]]:
    soup = BeautifulSoup(rendered, "html.parser")
    container = soup.new_tag("main", attrs={"id": "conteudo", "class": "book-content"})
    chapters: list[Chapter] = []
    used: set[str] = set()
    current_chapter: Tag | None = None
    current_subchapter: Tag | None = None
    current_topic: Tag | None = None

    for node in list(soup.contents):
        if isinstance(node, NavigableString) and not node.strip():
            continue
        if not isinstance(node, Tag):
            continue
        if node.name in ("h2", "h3", "h4"):
            level = int(node.name[1])
            title = node.get_text(" ", strip=True)
            base = slug(title) or f"secao-{len(used) + 1}"
            anchor = base
            suffix = 2
            while anchor in used:
                anchor = f"{base}-{suffix}"
                suffix += 1
            used.add(anchor)
            node["id"] = anchor
            heading = Heading(title, anchor, level)

            if level == 2:
                current_chapter = soup.new_tag("section", attrs={"class": "chapter", "aria-labelledby": anchor})
                current_chapter.append(node.extract())
                container.append(current_chapter)
                current_subchapter = None
                current_topic = None
                chapters.append(Chapter(heading))
            elif level == 3:
                if current_chapter is None:
                    raise ValueError(f"Subseção sem capítulo: {title}")
                current_subchapter = soup.new_tag("section", attrs={"class": "subchapter", "aria-labelledby": anchor})
                current_subchapter.append(node.extract())
                current_chapter.append(current_subchapter)
                current_topic = None
                chapters[-1].children.append(heading)
            else:
                if current_subchapter is None:
                    raise ValueError(f"Tópico sem subseção: {title}")
                current_topic = soup.new_tag("section", attrs={"class": "topic", "aria-labelledby": anchor})
                current_topic.append(node.extract())
                current_subchapter.append(current_topic)
                chapters[-1].children.append(heading)
            continue

        destination = current_topic or current_subchapter or current_chapter
        if destination is None:
            raise ValueError("Conteúdo encontrado antes do primeiro capítulo")
        destination.append(node.extract())

    for table in container.find_all("table"):
        heading = table.find_previous(["h4", "h3", "h2"])
        caption = soup.new_tag("caption", attrs={"class": "sr-only"})
        caption.string = heading.get_text(" ", strip=True) if heading else "Tabela do material"
        table.insert(0, caption)
        for th in table.find_all("th"):
            th["scope"] = "col"
        wrapper = soup.new_tag("div", attrs={"class": "table-scroll", "tabindex": "0", "role": "region", "aria-label": caption.string})
        table.wrap(wrapper)

    return str(container), chapters


def build_toc(chapters: list[Chapter]) -> str:
    """Sumário no padrão do ebook Well-Architected: faixa por capítulo e itens numerados."""
    groups: list[str] = []
    for chapter in chapters:
        heading = chapter.heading
        numbered = re.match(r"^(\d+)\.\s+(.*)$", heading.title)
        number = numbered.group(1) if numbered else None
        label = f"Capítulo {number} — {numbered.group(2)}" if numbered else heading.title
        if not chapter.children:
            groups.append(
                '<div class="toc-group">'
                f'<a class="toc-group-title" href="#{heading.anchor}">{html.escape(label)}</a></div>'
            )
            continue
        links: list[str] = []
        section = 0
        for child in chapter.children:
            if child.level == 3:
                section += 1
                n = f"{number}.{section}" if number else ""
                links.append(
                    f'<li><a href="#{child.anchor}"><span class="n">{n}</span> {html.escape(child.title)}</a></li>'
                )
            else:
                links.append(
                    f'<li class="toc-topic"><a href="#{child.anchor}"><span class="n"></span> {html.escape(child.title)}</a></li>'
                )
        groups.append(
            '<details class="toc-group">'
            f'<summary class="toc-group-title">{html.escape(label)}</summary>'
            '<ul class="toc-list">' + "".join(links) + '</ul></details>'
        )
    return "\n".join(groups)


CSS = r"""
  :root{
    color-scheme:light;
    --paper:#fff;
    --canvas:#e7ecef;
    --ink:#1b2d3b;
    --text:#263643;
    --muted:#52616d;
    --line:#cbd5db;
    --surface:#f2f6f7;
    --accent:#ff9900;
    --accent-ink:#8a4b00;
    --teal:#086b70;
    --sans:'IBM Plex Sans',Arial,sans-serif;
    --mono:'IBM Plex Mono',Consolas,monospace;
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;background:var(--canvas);color:var(--text);font:16px/1.65 var(--sans)}
  a{color:var(--teal);text-underline-offset:3px}
  a:focus-visible,summary:focus-visible,.table-scroll:focus-visible{outline:3px solid var(--accent-ink);outline-offset:4px}
  .skip-link{position:absolute;left:-9999px;top:8px;background:var(--paper);padding:8px 12px;z-index:10}
  .skip-link:focus{left:12px}
  .book{max-width:920px;margin:24px auto;background:var(--paper);box-shadow:0 16px 55px #20344324;padding:0 70px 72px}
  .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  h1,h2,h3,h4{color:var(--ink);line-height:1.2;margin:0;text-wrap:balance}
  p{margin:0 0 .9em;max-width:75ch}
  li{margin:.32em 0;max-width:75ch}
  code{font:.86em var(--mono);padding:.1em .25em;background:var(--surface);border-radius:3px;overflow-wrap:anywhere}
  strong{color:var(--ink)}

  /* Capa: os cinco domínios são o motivo gráfico da página. */
  .cover{min-height:770px;display:grid;grid-template-rows:auto 1fr auto;gap:30px;padding:40px 0 50px;border-top:10px solid var(--ink);position:relative}
  .cover:before{content:'';position:absolute;top:-10px;left:0;width:92px;height:10px;background:var(--accent)}
  .cover-top,.cover-bottom-label{font:700 .75rem/1.4 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
  .cover-top{display:flex;justify-content:space-between;gap:20px}
  .cover-main{align-self:center;max-width:690px}
  .cover-code{display:block;font:700 clamp(4rem,11vw,7.1rem)/.98 var(--mono);letter-spacing:-.085em;color:var(--ink);margin:0 0 14px}
  .cover-exam{display:block;font:700 .95rem/1.4 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--accent-ink);margin:0 0 30px}
  .cover-main h1{font-size:clamp(2rem,4.4vw,3rem);font-weight:600;letter-spacing:-.045em;max-width:13em;margin:0 0 20px}
  .cover-subtitle{font-size:1.14rem;color:var(--muted);max-width:40rem;margin:0 0 14px}
  .cover-note{font:.76rem/1.5 var(--mono);color:var(--teal);margin:0}
  .cover-bottom{border-top:1px solid var(--ink);padding-top:16px}
  .cover-bottom-label{margin:0 0 16px}
  .domain-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px}
  .domain{border-top:4px solid var(--accent);padding-top:8px;min-width:0}
  .domain strong{display:block;font:600 1.65rem/1 var(--mono);color:var(--ink);margin-bottom:7px}
  .domain span{display:block;font-size:.78rem;line-height:1.3;color:var(--muted)}

  /* Sumário no padrão do ebook Well-Architected: faixa por capítulo, itens numerados em duas colunas. */
  .toc{padding:40px 0 64px}
  .toc h2{font-size:1.9rem;letter-spacing:-.04em;padding-bottom:12px;margin-bottom:22px;border-bottom:3px solid var(--ink)}
  .toc-intro{font-size:.95rem;color:var(--muted);margin:-8px 0 22px}
  .toc-group+.toc-group{margin-top:10px}
  .toc-group-title{display:block;list-style:none;cursor:pointer;font:700 .76rem/1.4 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--ink);text-decoration:none;background:var(--surface);border-left:4px solid var(--accent);padding:10px 12px;break-after:avoid}
  .toc-group-title::-webkit-details-marker{display:none}
  details.toc-group .toc-group-title:after{content:'+';float:right;margin-left:12px;font-size:1rem;line-height:1}
  details.toc-group[open] .toc-group-title:after{content:'−'}
  .toc-list{list-style:none;margin:0;padding:8px 10px 0;column-count:2;column-gap:28px}
  .toc-list li{margin:0;max-width:none;break-inside:avoid}
  .toc-list a{display:flex;gap:8px;align-items:baseline;padding:3px 0;font-size:.88rem;line-height:1.35;color:var(--text);text-decoration:none;border-bottom:1px dotted var(--line)}
  .toc-list a:hover{color:var(--accent-ink)}
  .toc-list a .n{font:.74rem var(--mono);color:var(--accent-ink);flex:0 0 3.2em}
  .toc-list .toc-topic a{padding-left:14px;font-size:.82rem;color:var(--muted)}
  .toc-ending{margin:18px 0 0;font-size:.9rem}
  .toc-ending a{color:var(--text);text-decoration:none}

  /* Capítulos e notas de revisão. */
  .chapter{padding:46px 0 0;margin:0 0 20px;border-top:6px solid var(--ink);break-before:page}
  .chapter>h2{font-size:2.1rem;letter-spacing:-.04em;margin:0 0 24px}
  .subchapter{margin:32px 0 0;padding:25px 0 0;border-top:1px solid var(--line)}
  .subchapter>h3{font-size:1.4rem;letter-spacing:-.025em;margin:0 0 14px}
  .topic{margin:26px 0 0}
  .topic>h4{font-size:1.08rem;margin:0 0 11px}
  .chapter>ul,.subchapter>ul,.topic>ul{padding-left:1.35em}
  .book-content hr{border:0;border-top:1px solid var(--line);margin:30px 0}
  .book-content blockquote{margin:18px 0;padding:12px 18px;border-left:4px solid var(--teal);background:var(--surface);color:var(--muted)}
  .book-content blockquote p:last-child{margin-bottom:0}
  .book-content ol{padding-left:1.5em}
  .book-content ol>li{padding-left:.25em}
  .book-content ol>li::marker{font-family:var(--mono);font-weight:700;color:var(--accent-ink)}
  .back-link{font:.75rem var(--mono);display:inline-block;margin:10px 0 22px;text-decoration:none}

  .table-scroll{overflow-x:auto;border:1px solid var(--line);border-radius:4px;margin:20px 0 24px}
  table{border-collapse:collapse;width:100%;min-width:590px;font-size:.88rem;line-height:1.42}
  th,td{text-align:left;vertical-align:top;padding:9px 11px;border-bottom:1px solid var(--line)}
  th{background:var(--ink);color:#fff;font-size:.78rem;font-weight:600}
  tr:last-child td{border-bottom:0}
  tbody tr:nth-child(even){background:#f7f9fa}

  .flashcard{margin:14px 0;border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:0 5px 5px 0;background:var(--paper);break-inside:avoid}
  .flashcard summary{cursor:pointer;padding:14px 38px 14px 16px;position:relative;font-weight:600;color:var(--ink);line-height:1.45;list-style:none}
  .flashcard summary::-webkit-details-marker{display:none}
  .flashcard summary:after{content:'+';position:absolute;right:14px;top:12px;font:500 1.2rem var(--mono);color:var(--accent-ink)}
  .flashcard[open] summary:after{content:'−'}
  .flashcard-answer{padding:13px 16px 16px;border-top:1px solid var(--line);background:var(--surface);font-size:.94rem}
  .flashcard-answer p:last-child{margin-bottom:0}
  .answer-label{font:700 .7rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--teal);margin:0 0 9px}

  .closing{margin-top:76px;padding:26px 30px;background:var(--ink);color:#eaf0f2;border-top:8px solid var(--accent);break-inside:avoid}
  .closing h2{color:#fff;font-size:1.65rem;margin-bottom:13px}
  .closing p,.closing li{color:#eaf0f2}
  .closing ul{margin:0;padding-left:1.2em}
  .closing li::marker{color:var(--accent)}

  @media(max-width:700px){
    body{background:var(--paper)}
    .book{margin:0;padding:0 20px 45px;box-shadow:none}
    .cover{min-height:0;padding:24px 0 34px;gap:45px}
    .cover-top{flex-direction:column;gap:3px}
    .cover-code{font-size:clamp(3.2rem,16vw,5rem);margin-bottom:20px}
    .cover-main h1{font-size:2rem}
    .domain-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
    .toc-list{column-count:1}
    .chapter{padding-top:34px}
    .chapter>h2{font-size:1.7rem}
    .subchapter>h3{font-size:1.25rem}
    .closing{padding:22px 20px}
  }
  @media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}

  @page{size:A4;margin:19mm 17mm 21mm;
    @bottom-left{content:'AIF-C01  /  GUIA DE REVISÃO  |  Erik Nathan (eriknathan.me)';font:8pt 'IBM Plex Mono',monospace;color:#52616d}
    @bottom-right{content:counter(page);font:9pt 'IBM Plex Mono',monospace;color:#1b2d3b}
  }
  @page:first{@bottom-left{content:none}@bottom-right{content:none}}
  @media print{
    *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
    html{font-size:9.5pt}
    body{background:#fff;font-size:9.5pt;line-height:1.48}
    .book{max-width:none;margin:0;padding:0;box-shadow:none}
    .cover{min-height:235mm;break-after:page;padding-top:18px}
    .cover-code{font-size:62pt}
    .cover-exam{font-size:10.5pt}
    .cover-main h1{font-size:30pt}
    .cover-subtitle{font-size:12pt}
    .toc{break-after:page}
    .toc{padding:0}
    .toc-intro,.toc-ending{display:none}
    .toc h2{font-size:18pt}
    .toc-group-title{cursor:default;padding:6px 10px;font-size:8pt}
    details.toc-group .toc-group-title:after,details.toc-group[open] .toc-group-title:after,
    .flashcard summary:after,.flashcard[open] summary:after{content:none}
    .toc-list{display:block!important}
    .toc-list a{font-size:8.9pt;line-height:1.32;padding:1.5px 24px 1.5px 0}
    .toc-list a .n{font-size:7.8pt}
    .toc-list .toc-topic a{font-size:8.3pt}
    .chapter{break-before:page;padding-top:10px;margin:0;border-top:5px solid var(--ink)}
    .chapter>h2{font-size:20pt;margin-bottom:16px;break-after:avoid}
    .subchapter{margin-top:22px;padding-top:15px}
    .subchapter>h3,.topic>h4{break-after:avoid}
    .book-content p,.book-content li{max-width:none;orphans:3;widows:3}
    .book-content ol{padding-left:2.25em}
    .book-content ol>li::marker{color:var(--ink)}
    .book-content hr{display:none}
    .back-link{display:none}
    .table-scroll{overflow:visible;border:0}
    table{min-width:0;font-size:7.4pt}
    thead{display:table-header-group}
    tr{break-inside:avoid}
    th,td{padding:5px 7px;border:1px solid var(--line)}
    .flashcard{break-inside:avoid;margin:10px 0}
    .flashcard summary{padding:10px 12px}
    .flashcard-answer{display:block!important;padding:9px 12px 11px}
    details::details-content{content-visibility:visible;display:block}
    details>*:not(summary){display:block!important}
    .closing{background:#fff;color:var(--ink);border:1px solid var(--ink);border-top:6px solid var(--accent);margin-top:35px}
    .closing h2,.closing p,.closing li{color:var(--ink)}
  }
"""


def build_html(content: str, toc: str, flashcards: int) -> str:
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Guia de revisão AIF-C01 com fundamentos de IA, IA generativa, agentes, IA responsável, tabelas de decisão e flashcards.">
<title>AIF-C01 — Guia de revisão</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&amp;family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
<article class="book">
  <header class="cover">
    <div class="cover-top"><span>Guia de estudo</span><span>AWS Certified AI Practitioner</span></div>
    <div class="cover-main">
      <span class="cover-code">AIF-C01</span>
      <span class="cover-exam">AWS Certified AI Practitioner</span>
      <h1>Guia de revisão</h1>
      <p class="cover-subtitle">Fundamentos de IA e ML, IA generativa, agentes, foundation models, IA responsável e segurança para a revisão da certificação.</p>
      <p class="cover-note">Por Erik Nathan · <a href="https://eriknathan.me/">eriknathan.me</a></p>
    </div>
    <div class="cover-bottom">
      <p class="cover-bottom-label">Domínios do exame · pesos oficiais</p>
      <div class="domain-grid">
        <div class="domain"><strong>20%</strong><span>Fundamentals of AI and ML</span></div>
        <div class="domain"><strong>24%</strong><span>Fundamentals of GenAI</span></div>
        <div class="domain"><strong>28%</strong><span>Applications of Foundation Models</span></div>
        <div class="domain"><strong>14%</strong><span>Guidelines for Responsible AI</span></div>
        <div class="domain"><strong>14%</strong><span>Security, Compliance, and Governance</span></div>
      </div>
    </div>
  </header>

  <nav class="toc" id="sumario" aria-label="Sumário">
    <h2>Sumário</h2>
    <p class="toc-intro">Abra um capítulo para ir diretamente ao tópico que deseja revisar.</p>
    {toc}
    <p class="toc-ending"><a href="#sintese-de-revisao">Ir para a síntese de revisão</a></p>
  </nav>

  {content}

  <section class="closing" id="sintese-de-revisao" aria-labelledby="sintese-title">
    <h2 id="sintese-title">Síntese de revisão</h2>
    <p>Este guia organiza a revisão pelos quatro domínios do exame e reúne formatos de consulta rápida e prática ativa.</p>
    <ul>
      <li>Os pesos oficiais são 20% para fundamentos de IA e ML, 24% para fundamentos de IA generativa, 28% para aplicações de foundation models, 14% para IA responsável e 14% para segurança, conformidade e governança.</li>
      <li>As tabelas de decisão rápida ao fim de cada capítulo e os padrões recorrentes (seção 12) concentram as palavras-chave e os pares de conceitos e serviços que mais se confundem.</li>
      <li>O mapa de domínios (seção 13) orienta prioridades; serviços, nomes e disponibilidade foram conferidos em setembro de 2026, após a revisão 1.1 do guia e as mudanças de julho de 2026.</li>
      <li>O autoteste e as questões de múltipla resposta, ordenação e correspondência (seções 14 e 15) oferecem {flashcards} perguntas para revisão ativa.</li>
      <li>O mapa da seção 15 relaciona as 14 tarefas publicadas no guia oficial às seções correspondentes.</li>
    </ul>
  </section>
</article>
<script>
  // Mostra todos os tópicos e respostas na impressão, restaurando o estado depois.
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
    expected_flashcards = len(re.findall(r"^> \[!question\]-", source, re.MULTILINE))
    expected_chapters = len(re.findall(r"^## ", source, re.MULTILINE))
    converted, flashcards = convert_flashcards(source)
    rendered = MARKDOWN.render(converted)
    content, chapters = organize_content(rendered)
    if flashcards != expected_flashcards or len(chapters) != expected_chapters:
        raise ValueError(f"Estrutura inesperada: {flashcards} flashcards, {len(chapters)} capítulos")
    output = build_html(content, build_toc(chapters), flashcards)
    OUTPUT.write_text(output, encoding="utf-8")
    print(f"Gerado {OUTPUT}: {len(chapters)} capítulos e {flashcards} flashcards")


if __name__ == "__main__":
    main()
