#!/usr/bin/env python3
"""Gera os PDFs de todos os e-books do repositório e os reúne em PDF-Geral/.

Cada pasta da raiz que tem um gerar_pdf.py é tratada como um e-book. Se a pasta
também tiver gerar_ebook.py, o HTML é regenerado a partir do Markdown antes do PDF.
O nome do arquivo final é o mesmo DEFAULT_OUTPUT definido no gerar_pdf.py da pasta.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DESTINO_PADRAO = ROOT / "PDF-Geral"
IGNORAR = {"template", "PDF-Geral"}


@dataclass
class Ebook:
    pasta: Path
    nome_pdf: str

    @property
    def tem_gerador_html(self) -> bool:
        return (self.pasta / "gerar_ebook.py").exists()


def slug(texto: str) -> str:
    normalizado = unicodedata.normalize("NFKD", texto)
    ascii_texto = "".join(c for c in normalizado if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", ascii_texto.lower()).strip("-")


def nome_do_pdf(pasta: Path) -> str:
    """Usa o nome definido em DEFAULT_OUTPUT no gerar_pdf.py; senão, o nome da pasta."""
    codigo = (pasta / "gerar_pdf.py").read_text(encoding="utf-8")
    encontrado = re.search(r'^DEFAULT_OUTPUT\s*=.*?"([^"/]+\.pdf)"\s*$', codigo, re.MULTILINE)
    return encontrado.group(1) if encontrado else f"{slug(pasta.name)}.pdf"


def descobrir_ebooks() -> list[Ebook]:
    ebooks = []
    for pasta in sorted(ROOT.iterdir(), key=lambda p: p.name.lower()):
        if not pasta.is_dir() or pasta.name.startswith(".") or pasta.name in IGNORAR:
            continue
        if (pasta / "gerar_pdf.py").exists():
            ebooks.append(Ebook(pasta, nome_do_pdf(pasta)))
    return ebooks


def executar(comando: list[str], pasta: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(comando, cwd=pasta, capture_output=True, text=True)


def ultima_linha(resultado: subprocess.CompletedProcess[str]) -> str:
    saida = (resultado.stderr or resultado.stdout).strip().splitlines()
    return saida[-1] if saida else f"código de saída {resultado.returncode}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--destino", type=Path, default=DESTINO_PADRAO, help="Pasta onde os PDFs serão salvos (padrão: PDF-Geral)")
    parser.add_argument("--apenas", action="append", default=[], metavar="TEXTO",
                        help="Gera só os e-books cuja pasta contém o texto (pode repetir). Ex.: --apenas docker --apenas dva")
    parser.add_argument("--sem-html", action="store_true", help="Não regenera o ebook.html a partir do Markdown")
    parser.add_argument("--chrome", help="Caminho para o Chrome/Chromium, repassado a cada gerar_pdf.py")
    parser.add_argument("--listar", action="store_true", help="Só lista os e-books encontrados e sai")
    args = parser.parse_args()

    ebooks = descobrir_ebooks()
    if args.apenas:
        filtros = [f.lower() for f in args.apenas]
        ebooks = [e for e in ebooks if any(f in e.pasta.name.lower() for f in filtros)]
    if not ebooks:
        print("Nenhum e-book encontrado.", file=sys.stderr)
        return 1

    if args.listar:
        for ebook in ebooks:
            html = "Markdown → HTML → PDF" if ebook.tem_gerador_html else "HTML → PDF"
            print(f"{ebook.pasta.name:<34} {ebook.nome_pdf:<40} {html}")
        return 0

    destino = args.destino.resolve()
    destino.mkdir(parents=True, exist_ok=True)
    nomes = [e.nome_pdf for e in ebooks]
    repetidos = {n for n in nomes if nomes.count(n) > 1}
    if repetidos:
        print(f"Nomes de PDF repetidos entre pastas: {', '.join(sorted(repetidos))}", file=sys.stderr)
        return 1

    falhas: list[str] = []
    inicio_geral = time.monotonic()
    for numero, ebook in enumerate(ebooks, start=1):
        print(f"[{numero}/{len(ebooks)}] {ebook.pasta.name}")
        inicio = time.monotonic()

        if ebook.tem_gerador_html and not args.sem_html:
            resultado = executar([sys.executable, "gerar_ebook.py"], ebook.pasta)
            if resultado.returncode != 0:
                print(f"      ERRO ao gerar o HTML: {ultima_linha(resultado)}")
                falhas.append(ebook.pasta.name)
                continue
            print("      HTML atualizado")

        saida = destino / ebook.nome_pdf
        comando = [sys.executable, "gerar_pdf.py", "--output", str(saida)]
        if args.chrome:
            comando += ["--chrome", args.chrome]
        resultado = executar(comando, ebook.pasta)
        if resultado.returncode != 0 or not saida.exists():
            print(f"      ERRO ao gerar o PDF: {ultima_linha(resultado)}")
            falhas.append(ebook.pasta.name)
            continue
        tamanho = saida.stat().st_size / 1024 / 1024
        print(f"      PDF: {saida.relative_to(ROOT) if saida.is_relative_to(ROOT) else saida} "
              f"({tamanho:.1f} MB, {time.monotonic() - inicio:.0f} s)")

    # O gerar_pdf.py cria pastas temporárias ao lado do PDF; se o Chrome ainda estiver
    # escrevendo no perfil quando ele termina, sobram restos. Remove só as dessa execução.
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
