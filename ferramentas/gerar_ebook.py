#!/usr/bin/env python3
"""Converte o material Markdown de um e-book em ebook.html, com o visual de template/ebook-template.html.

Uso (a partir de qualquer pasta):
  python3 ferramentas/gerar_ebook.py                 # todos os e-books com ebook.toml e Markdown
  python3 ferramentas/gerar_ebook.py docker saa-c03  # por trecho do nome da pasta
  python3 ferramentas/gerar_ebook.py aws-aif-c01     # ou pelo nome exato da pasta

Cada pasta precisa de um ebook.toml (capa, síntese, rodapé) e do Markdown indicado em `fonte`.
Títulos ## viram capítulos, ### seções e #### tópicos; a numeração é gerada pelo script.
Callouts `> [!question]-` viram flashcards; parágrafos `Q01.` seguidos de lista viram questões.
"""

from __future__ import annotations

import argparse
import base64
import html
import re
import sys
from dataclasses import dataclass, field

from bs4 import BeautifulSoup, NavigableString, Tag
from markdown_it import MarkdownIt

from comum import FONTES, TEMPLATE, Ebook, resolver_ebooks, slug


MARKDOWN = MarkdownIt("commonmark", {"html": True}).enable("table")
MARCA_FONTES = "/* @font-face embutidos pelo gerar_ebook.py */"
AUTORIA = '<p class="cover-author"><strong>Erik Nathan</strong><a href="https://eriknathan.me/">eriknathan.me</a></p>'


@dataclass
class Heading:
    title: str
    anchor: str
    number: str
    level: int
    children: list[Heading] = field(default_factory=list)


def content_text(root: Tag | BeautifulSoup) -> str:
    """Normaliza só espaços; usado para assegurar a preservação do texto."""
    return re.sub(r"\s+", " ", root.get_text(" ", strip=True)).strip()


def sem_blocos_de_codigo(source: str) -> str:
    return re.sub(r"^(```|~~~).*?^\1", "", source, flags=re.MULTILINE | re.DOTALL)


def convert_flashcards(source: str) -> tuple[str, int]:
    """Troca callouts Obsidian `> [!question]-` por details sem alterar perguntas ou respostas."""
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


def split_chapter_numbers(soup: BeautifulSoup) -> dict[int, str]:
    """Na numeração "markdown", tira o "N. " dos títulos ## e devolve {id do tag: N}."""
    numbers: dict[int, str] = {}
    for node in soup.find_all("h2", recursive=False):
        first = node.contents[0] if node.contents else None
        if not isinstance(first, NavigableString):
            continue
        match = re.match(r"^(\d+)\.\s+", str(first))
        if match:
            numbers[id(node)] = match.group(1)
            first.replace_with(str(first)[match.end():])
    return numbers


def organize_content(rendered: str, numbering: str) -> tuple[Tag, list[Heading]]:
    soup = BeautifulSoup(rendered, "html.parser")
    # A âncora usa o título original (com "N. "), para manter os links já publicados.
    original_titles = {id(node): node.get_text(" ", strip=True) for node in soup.find_all(["h2", "h3", "h4"], recursive=False)}
    markdown_numbers = split_chapter_numbers(soup) if numbering == "markdown" else {}
    expected_text = content_text(soup)
    expected_code = [node.get_text() for node in soup.select("pre code")]
    container = soup.new_tag("main", attrs={"id": "conteudo", "class": "book-content"})
    chapters: list[Heading] = []
    used: set[str] = set()
    chapter = subsection = topic = None
    chapter_number = ""
    section_count = topic_count = auto_count = 0
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
            base = slug(original_titles[id(node)]) or f"secao-{len(used) + 1}"
            anchor = base
            suffix = 2
            while anchor in used:
                anchor = f"{base}-{suffix}"
                suffix += 1
            used.add(anchor)
            node["id"] = anchor
            if level == 2:
                section_count = topic_count = 0
                if numbering == "markdown":
                    chapter_number = markdown_numbers.get(id(node), "")
                else:
                    auto_count += 1
                    chapter_number = str(auto_count)
                heading = Heading(title, anchor, chapter_number, level)
                chapters.append(heading)
                chapter = soup.new_tag("section", attrs={"class": "chapter", "aria-labelledby": anchor})
                header = soup.new_tag("header", attrs={"class": "chapter-head"})
                if chapter_number:
                    kicker = soup.new_tag("span", attrs={"class": "kicker", "data-generated": "true"})
                    kicker.string = f"Capítulo {chapter_number}"
                    header.append(kicker)
                header.append(node.extract())
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
                number = f"{chapter_number}.{section_count}" if chapter_number else ""
                subsection = soup.new_tag("section", attrs={"class": "section", "aria-labelledby": anchor})
                header = soup.new_tag("div", attrs={"class": "section-head"})
                if number:
                    label = soup.new_tag("span", attrs={"class": "sec-label", "data-generated": "true"})
                    label.string = number
                    header.append(label)
                header.append(node.extract())
                subsection.append(header)
                chapter.append(subsection)
                topic = None
                chapters[-1].children.append(Heading(title, anchor, number, level))
            else:
                if subsection is None:
                    raise ValueError(f"Tópico sem seção: {title}")
                topic_count += 1
                number = f"{chapter_number}.{section_count}.{topic_count}" if chapter_number else ""
                topic = soup.new_tag("section", attrs={"class": "topic", "aria-labelledby": anchor})
                if number:
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

    # Questões "Q01." seguidas da lista de alternativas; o gabarito continua no ponto original.
    for paragraph in list(container.find_all("p")):
        if not re.match(r"^Q\d{2}\.", paragraph.get_text(strip=True)):
            continue
        options = paragraph.find_next_sibling()
        if options is None or options.name != "ul":
            raise ValueError(f"Questão sem alternativas: {paragraph.get_text(strip=True)[:60]}")
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
        label = f"Capítulo {chapter.number} — {chapter.title}" if chapter.number else chapter.title
        label = html.escape(label)
        if not chapter.children:
            groups.append(f'<div class="toc-group"><a class="toc-group-title" href="#{chapter.anchor}">{label}</a></div>')
            continue
        items = []
        for child in chapter.children:
            css = ' class="toc-topic"' if child.level == 4 else ""
            items.append(f'<li{css}><a href="#{child.anchor}"><span class="n">{child.number}</span> {html.escape(child.title)}</a></li>')
        groups.append(f'<details class="toc-group"><summary class="toc-group-title">{label}</summary><ul class="toc-list">{"".join(items)}</ul></details>')
    return "\n    ".join(groups)


def template_css(ebook: Ebook) -> str:
    template = BeautifulSoup(TEMPLATE.read_text(encoding="utf-8"), "html.parser")
    css = template.style.string.replace("{{RODAPE}}", ebook.config["rodape"])
    extra = ebook.pasta / "extra.css"
    if extra.is_file():
        css += f"\n  /* ---------- Ajustes deste e-book ({extra.name}) ---------- */\n" + extra.read_text(encoding="utf-8")
    return css


def unicode_range(faixa: str) -> list[range]:
    faixas = []
    for parte in faixa.split(","):
        inicio, _, fim = parte.strip().removeprefix("U+").partition("-")
        faixas.append(range(int(inicio, 16), int(fim or inicio, 16) + 1))
    return faixas


def font_faces(texto: str) -> str:
    """@font-face de template/fontes em base64, só das faces cujo unicode-range aparece no texto.

    Assim o HTML continua autônomo e o PDF sai igual com ou sem rede."""
    usados = {ord(c) for c in texto}
    regras = []
    for regra in re.findall(r"@font-face\{[^}]+\}", FONTES.read_text(encoding="utf-8")):
        faixas = unicode_range(re.search(r"unicode-range:([^;}]+)", regra).group(1))
        if not any(c in faixa for faixa in faixas for c in usados):
            continue
        arquivo = re.search(r"url\(([^)]+)\)", regra).group(1)
        dados = base64.b64encode((FONTES.parent / arquivo).read_bytes()).decode("ascii")
        regras.append("  " + regra.replace(f"url({arquivo})", f"url(data:font/woff2;base64,{dados})"))
    return "\n".join(regras)


def build_cover(capa: dict) -> str:
    codigo = html.escape(capa["codigo"]).replace("-", '<span class="dash">-</span>')
    linhas = [
        f'<div class="cover-top"><span>{capa["categoria"]}</span><span>Atualizado em {capa["atualizado"]}</span></div>',
        '<div class="cover-main">',
    ]
    if capa.get("selo"):
        linhas.append(f'  <span class="cover-level">{capa["selo"]}</span>')
    linhas.append(f'  <span class="cover-code">{codigo}</span>')
    if capa.get("exame"):
        linhas.append(f'  <span class="cover-exam">{capa["exame"]}</span>')
    linhas += [
        f'  <h1>{capa["titulo"]}</h1>',
        f'  <p class="cover-subtitle">{capa["subtitulo"]}</p>',
        "</div>",
        '<div class="cover-bottom">',
        f'  <p class="cover-bottom-label">{capa["rotulo_destaques"]}</p>',
    ]
    destaques = capa.get("destaques", [])
    if not 1 <= len(destaques) <= 6:
        raise ValueError("A capa deve ter de 1 a 6 destaques")
    com_peso = bool(capa.get("destaques_com_peso"))
    if com_peso:
        # Barra proporcional aos pesos; a legenda abaixo fica em colunas iguais, na mesma ordem.
        segmentos = "".join(f'<span style="flex:{d["peso"]}"></span>' for d in destaques)
        linhas.append(f'  <div class="cover-bar" aria-hidden="true">{segmentos}</div>')
    classe = "highlight-grid weighted" if com_peso else "highlight-grid"
    linhas.append(f'  <div class="{classe}" style="grid-template-columns:repeat({len(destaques)},minmax(0,1fr))">')
    for destaque in destaques:
        idioma = f' lang="{destaque["idioma"]}"' if destaque.get("idioma") else ""
        nota = f'<span class="highlight-note">{destaque["nota"]}</span>' if destaque.get("nota") else ""
        linhas.append(f'    <div class="highlight"><strong>{destaque["valor"]}</strong><span{idioma}>{destaque["texto"]}</span>{nota}</div>')
    linhas += [
        "  </div>",
        "</div>",
        f'<footer class="cover-foot">{AUTORIA}<span class="cover-series">Guias de estudo</span></footer>',
    ]
    return "\n      ".join(linhas)


def build_closing(sintese: dict, flashcards: int) -> str:
    linhas = []
    if sintese.get("introducao"):
        linhas.append(f'<p>{sintese["introducao"]}</p>')
    linhas.append("<ul>")
    linhas += [f'  <li>{item.replace("{flashcards}", str(flashcards))}</li>' for item in sintese["itens"]]
    linhas.append("</ul>")
    return "\n    ".join(linhas)


def build_html(ebook: Ebook, content: Tag, chapters: list[Heading], flashcards: int) -> str:
    config = ebook.config
    pagina = config["pagina"]
    return f'''<!DOCTYPE html>
<!-- Gerado por ferramentas/gerar_ebook.py a partir de {config["fonte"]} e ebook.toml. Não edite à mão. -->
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{html.escape(pagina["descricao"])}">
<title>{html.escape(pagina["titulo"])}</title>
<style>
  /* ---------- Fontes (template/fontes, IBM Plex, OFL) ---------- */
{MARCA_FONTES}
{template_css(ebook)}</style>
</head>
<body>
<a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
<article class="book">
  <header class="cover">
      {build_cover(config["capa"])}
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
    {build_closing(config["sintese"], flashcards)}
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


def gerar(ebook: Ebook) -> str:
    """Gera o ebook.html da pasta e devolve um resumo de uma linha."""
    if ebook.fonte is None:
        raise ValueError(f"{ebook.nome}: o ebook.toml não define `fonte`; o ebook.html é editado à mão")
    numbering = ebook.config.get("numeracao", "automatica")
    if numbering not in ("automatica", "markdown"):
        raise ValueError(f"{ebook.nome}: numeracao deve ser 'automatica' ou 'markdown'")
    source = ebook.fonte.read_text(encoding="utf-8")
    sem_codigo = sem_blocos_de_codigo(source)
    expected_flashcards = len(re.findall(r"^> \[!question\]-", sem_codigo, re.MULTILINE))
    expected_chapters = len(re.findall(r"^## ", sem_codigo, re.MULTILINE))
    converted, flashcards = convert_flashcards(source)
    content, chapters = organize_content(MARKDOWN.render(converted), numbering)
    if flashcards != expected_flashcards or len(chapters) != expected_chapters:
        raise ValueError(f"Estrutura inesperada: {flashcards} flashcards, {len(chapters)} capítulos")
    questions = len(content.select("details.flashcard"))
    output = build_html(ebook, content, chapters, questions)
    output = output.replace(MARCA_FONTES, font_faces(output), 1)

    soup = BeautifulSoup(output, "html.parser")
    ids = [node["id"] for node in soup.select("[id]")]
    if len(ids) != len(set(ids)):
        raise ValueError("IDs duplicados no HTML")
    for link in soup.select('a[href^="#"]'):
        if link["href"][1:] not in ids:
            raise ValueError(f"Link interno sem destino: {link['href']}")
    if re.search(r"\{\{[A-Z_]+\}\}", output):
        raise ValueError("Marcador de template não preenchido")
    ebook.html.write_text(output, encoding="utf-8")
    return f"{len(chapters)} capítulos, {questions} perguntas e {len(soup.select('pre'))} blocos de código"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("ebooks", nargs="*", help="Pastas ou trechos do nome; vazio = todos")
    args = parser.parse_args()
    ebooks = [e for e in resolver_ebooks(args.ebooks) if e.fonte is not None or args.ebooks]
    falhas = 0
    for ebook in ebooks:
        try:
            print(f"{ebook.nome}: {gerar(ebook)}")
        except (ValueError, OSError) as error:
            print(f"{ebook.nome}: ERRO {error}", file=sys.stderr)
            falhas += 1
    return 1 if falhas else 0


if __name__ == "__main__":
    raise SystemExit(main())
