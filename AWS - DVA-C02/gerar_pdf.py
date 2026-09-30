#!/usr/bin/env python3
"""Gera a versão PDF do ebook.html do DVA-C02 usando as regras de impressão do Chrome."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_INPUT = ROOT / "ebook.html"
DEFAULT_OUTPUT = ROOT / "output" / "pdf" / "dva-c02-guia-de-revisao.pdf"


def find_chrome(explicit: str | None) -> Path:
    candidates = [
        explicit,
        os.environ.get("CHROME_BIN"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "chrome",
        "msedge",
    ]
    for candidate in candidates:
        if not candidate:
            continue
        found = shutil.which(candidate)
        if found:
            return Path(found)
        path = Path(candidate).expanduser()
        if path.is_file() and os.access(path, os.X_OK):
            return path
    raise FileNotFoundError(
        "Chrome/Chromium não encontrado. Instale o navegador ou informe "
        "--chrome /caminho/para/o/executável."
    )


def pdf_complete(path: Path) -> bool:
    try:
        if path.stat().st_size < 1000:
            return False
        with path.open("rb") as pdf:
            if pdf.read(5) != b"%PDF-":
                return False
            pdf.seek(-1024, os.SEEK_END)
            return b"%%EOF" in pdf.read()
    except OSError:
        return False


def add_toc_page_numbers(pdf_path: Path, html_path: Path, output_path: Path) -> None:
    """Use the printed PDF's link destinations to number every TOC entry."""
    try:
        import fitz
    except ImportError as error:
        raise RuntimeError("PyMuPDF não instalado; execute: python3 -m pip install pymupdf") from error

    source = html_path.read_text(encoding="utf-8")
    toc = re.search(r'<nav\b[^>]*\bid="sumario"[^>]*>(.*?)</nav>', source, re.DOTALL)
    if toc is None:
        raise RuntimeError("Sumário não encontrado no HTML")
    targets = set(re.findall(r'<li(?:\s[^>]*)?><a href="#([^"]+)"', toc.group(1)))
    if not targets:
        raise RuntimeError("Nenhum tópico encontrado no sumário")

    with fitz.open(pdf_path) as pdf:
        destinations = pdf.resolve_names()
        missing = targets - destinations.keys()
        if missing:
            raise RuntimeError(f"Destinos ausentes no PDF: {', '.join(sorted(missing)[:5])}")
        first_content_page = min(destinations[target]["page"] for target in targets)
        seen: set[str] = set()
        for page_index in range(1, first_content_page):
            page = pdf[page_index]
            for link in page.get_links():
                target = link.get("nameddest")
                if target not in targets:
                    continue
                if target in seen:
                    raise RuntimeError(f"Tópico duplicado no sumário: {target}")
                seen.add(target)
                number = str(destinations[target]["page"] + 1)
                row = fitz.Rect(link["from"])
                font_size = 7.6
                x = row.x1 - 2 - fitz.get_text_length(number, fontname="cour", fontsize=font_size)
                page.insert_text(
                    (x, row.y0 + 10.5), number, fontname="cour",
                    fontsize=font_size, color=(0.32, 0.38, 0.43),
                )
        if seen != targets:
            raise RuntimeError(f"Tópicos sem linha no PDF: {', '.join(sorted(targets - seen)[:5])}")
        pdf.save(output_path, garbage=3, deflate=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="HTML de origem")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="PDF de destino")
    parser.add_argument("--chrome", help="Caminho para o executável do Chrome/Chromium")
    args = parser.parse_args()

    source = args.input.expanduser().resolve()
    destination = args.output.expanduser().resolve()
    if not source.is_file():
        parser.error(f"HTML não encontrado: {source}")
    if destination.suffix.lower() != ".pdf":
        parser.error("O arquivo de saída deve ter extensão .pdf")
    try:
        chrome = find_chrome(args.chrome)
    except FileNotFoundError as error:
        parser.error(str(error))

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="ebook-pdf-", dir=destination.parent) as temporary:
        work = Path(temporary)
        candidate = work / "ebook.pdf"
        command = [
            str(chrome),
            "--headless=new",
            "--disable-gpu",
            "--disable-extensions",
            "--no-first-run",
            "--no-default-browser-check",
            "--no-pdf-header-footer",
            f"--user-data-dir={work / 'chrome-profile'}",
            f"--print-to-pdf={candidate}",
            source.as_uri(),
        ]
        log = work / "chrome.log"
        with log.open("w", encoding="utf-8") as messages:
            process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=messages)
            deadline = time.monotonic() + 180
            stable_since = None
            last_size = 0
            complete = False
            try:
                while time.monotonic() < deadline:
                    if pdf_complete(candidate):
                        size = candidate.stat().st_size
                        if size != last_size:
                            last_size = size
                            stable_since = time.monotonic()
                        elif stable_since is not None and time.monotonic() - stable_since >= 1:
                            complete = True
                            break
                    if process.poll() is not None:
                        complete = pdf_complete(candidate)
                        break
                    time.sleep(0.25)
            finally:
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()

        if not complete:
            print("Erro: o Chrome não conseguiu gerar o PDF.", file=sys.stderr)
            details = log.read_text(encoding="utf-8").strip()
            if details:
                print(details[-2000:], file=sys.stderr)
            return 1
        numbered = work / "numbered.pdf"
        try:
            add_toc_page_numbers(candidate, source, numbered)
        except RuntimeError as error:
            print(f"Erro: {error}", file=sys.stderr)
            return 1
        numbered.replace(destination)

    print(f"PDF gerado: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
