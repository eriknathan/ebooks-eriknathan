#!/usr/bin/env python3
"""Gera a versão PDF do ebook.html usando as regras de impressão do Chrome."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_INPUT = ROOT / "ebook.html"
DEFAULT_OUTPUT = ROOT / "output" / "pdf" / "ebook-aws-well-architected.pdf"


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
        candidate.replace(destination)

    print(f"PDF gerado: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
