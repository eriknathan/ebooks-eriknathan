#!/usr/bin/env python3
"""Confere se os links relativos dos arquivos .md do repositório apontam para arquivos existentes.

Ignora URLs externas, âncoras soltas (#...), código (blocos e inline) e os material.md (o conteúdo dos e-books pode citar
caminhos de exemplo). Sai com código 1 se encontrar algum link quebrado.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

from comum import ROOT


def links_quebrados(arquivo: Path) -> list[str]:
    texto = arquivo.read_text(encoding="utf-8")
    texto = re.sub(r"^(```|~~~).*?^\1", "", texto, flags=re.MULTILINE | re.DOTALL)
    texto = re.sub(r"`[^`\n]+`", "", texto)  # exemplos em código inline não são links
    quebrados = []
    for match in re.finditer(r"\]\((<[^>]+>|[^)\s]+)\)", texto):
        alvo = match.group(1).strip("<>")
        if re.match(r"[a-z][a-z0-9+.-]*:", alvo) or alvo.startswith("#"):
            continue
        caminho = (arquivo.parent / unquote(alvo.split("#")[0])).resolve()
        if not caminho.exists():
            quebrados.append(alvo)
    return quebrados


def main() -> int:
    arquivos = sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and p.name != "material.md" and "legado" not in p.parts
    )
    total = 0
    for arquivo in arquivos:
        for alvo in links_quebrados(arquivo):
            print(f"{arquivo.relative_to(ROOT)}: link quebrado → {alvo}")
            total += 1
    print(f"{len(arquivos)} arquivos conferidos, {total} links quebrados")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
