#!/usr/bin/env python3
"""Gera os PDFs de todos os e-books do repositório e os reúne em PDF-Geral/.

Cada pasta da raiz que tem um ebook.toml é um e-book. Se o ebook.toml indicar a
`fonte` em Markdown, o ebook.html é regenerado antes do PDF. O nome do PDF é o
campo `pdf` do ebook.toml.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import time
from pathlib import Path

from comum import ROOT, descobrir_ebooks
from gerar_ebook import gerar
from gerar_pdf import gerar_pdf


DESTINO_PADRAO = ROOT / "PDF-Geral"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--destino", type=Path, default=DESTINO_PADRAO, help="Pasta onde os PDFs serão salvos (padrão: PDF-Geral)")
    parser.add_argument("--apenas", action="append", default=[], metavar="TEXTO",
                        help="Gera só os e-books cuja pasta contém o texto (pode repetir). Ex.: --apenas docker --apenas dva")
    parser.add_argument("--sem-html", action="store_true", help="Não regenera o ebook.html a partir do Markdown")
    parser.add_argument("--chrome", help="Caminho para o Chrome/Chromium")
    parser.add_argument("--listar", action="store_true", help="Só lista os e-books encontrados e sai")
    args = parser.parse_args()

    ebooks = descobrir_ebooks()
    if args.apenas:
        filtros = [f.lower() for f in args.apenas]
        ebooks = [e for e in ebooks if any(f in e.nome.lower() for f in filtros)]
    if not ebooks:
        print("Nenhum e-book encontrado.", file=sys.stderr)
        return 1

    if args.listar:
        largura = max(len(e.nome) for e in ebooks) + 2
        for ebook in ebooks:
            fluxo = "Markdown → HTML → PDF" if ebook.fonte else "HTML → PDF"
            print(f"{ebook.nome:<{largura}} {ebook.nome_pdf:<34} {fluxo}")
        return 0

    destino = args.destino.expanduser().resolve()
    destino.mkdir(parents=True, exist_ok=True)
    nomes = [e.nome_pdf for e in ebooks]
    repetidos = {n for n in nomes if nomes.count(n) > 1}
    if repetidos:
        print(f"Nomes de PDF repetidos entre pastas: {', '.join(sorted(repetidos))}", file=sys.stderr)
        return 1

    falhas: list[str] = []
    inicio_geral = time.monotonic()
    for numero, ebook in enumerate(ebooks, start=1):
        print(f"[{numero}/{len(ebooks)}] {ebook.nome}", flush=True)
        inicio = time.monotonic()

        if ebook.fonte and not args.sem_html:
            try:
                print(f"      HTML: {gerar(ebook)}", flush=True)
            except (ValueError, OSError) as error:
                print(f"      ERRO ao gerar o HTML: {error}")
                falhas.append(ebook.nome)
                continue

        saida = destino / ebook.nome_pdf
        try:
            gerar_pdf(ebook.html, saida, args.chrome)
        except (RuntimeError, FileNotFoundError) as error:
            print(f"      ERRO ao gerar o PDF: {str(error).splitlines()[0]}")
            falhas.append(ebook.nome)
            continue
        tamanho = saida.stat().st_size / 1024 / 1024
        exibido = saida.relative_to(ROOT) if saida.is_relative_to(ROOT) else saida
        print(f"      PDF: {exibido} ({tamanho:.1f} MB, {time.monotonic() - inicio:.0f} s)", flush=True)

    # Se o Chrome ainda estiver escrevendo no perfil quando a geração termina, sobram
    # pastas temporárias ao lado do PDF. Remove as que ficarem no destino.
    for resto in destino.glob("ebook-pdf-*"):
        if resto.is_dir():
            shutil.rmtree(resto, ignore_errors=True)

    total = time.monotonic() - inicio_geral
    print(f"\n{len(ebooks) - len(falhas)} de {len(ebooks)} PDFs gerados em {total:.0f} s → {destino}")
    if falhas:
        print("Falharam: " + ", ".join(falhas), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
