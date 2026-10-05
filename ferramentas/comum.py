"""Partes compartilhadas pelos scripts de geração: raiz do repositório, ebook.toml e descoberta dos e-books."""

from __future__ import annotations

import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

if sys.version_info >= (3, 11):
    import tomllib
else:  # Python 3.9 e 3.10
    try:
        import tomli as tomllib
    except ImportError as error:
        raise SystemExit("Pacote tomli não instalado; execute: python3 -m pip install -r requirements.txt") from error


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "template" / "ebook-template.html"
CONFIG = "ebook.toml"


def slug(texto: str) -> str:
    normalizado = unicodedata.normalize("NFKD", texto)
    ascii_texto = "".join(c for c in normalizado if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", ascii_texto.lower()).strip("-")


@dataclass
class Ebook:
    pasta: Path
    config: dict[str, Any]

    @classmethod
    def carregar(cls, pasta: Path) -> Ebook:
        arquivo = pasta / CONFIG
        if not arquivo.is_file():
            raise FileNotFoundError(f"{arquivo} não encontrado")
        with arquivo.open("rb") as entrada:
            return cls(pasta.resolve(), tomllib.load(entrada))

    @property
    def nome(self) -> str:
        return self.pasta.name

    @property
    def html(self) -> Path:
        return self.pasta / "ebook.html"

    @property
    def nome_pdf(self) -> str:
        return self.config.get("pdf") or f"{slug(self.nome)}.pdf"

    @property
    def fonte(self) -> Path | None:
        """Markdown de origem; None quando o ebook.html é editado diretamente."""
        fonte = self.config.get("fonte")
        return self.pasta / fonte if fonte else None


def descobrir_ebooks() -> list[Ebook]:
    pastas = sorted((p for p in ROOT.iterdir() if (p / CONFIG).is_file()), key=lambda p: p.name.lower())
    return [Ebook.carregar(p) for p in pastas]


def resolver_ebooks(alvos: list[str]) -> list[Ebook]:
    """Aceita caminhos de pasta ou trechos do nome (ex.: "docker", "saa-c03"); vazio = todos."""
    if not alvos:
        return descobrir_ebooks()
    escolhidos: list[Ebook] = []
    todos = None
    for alvo in alvos:
        caminho = Path(alvo)
        if (caminho / CONFIG).is_file():
            escolhidos.append(Ebook.carregar(caminho))
            continue
        todos = todos if todos is not None else descobrir_ebooks()
        achados = [e for e in todos if alvo.lower() in e.nome.lower()]
        if not achados:
            raise SystemExit(f"Nenhum e-book corresponde a {alvo!r}")
        escolhidos.extend(achados)
    unicos = {e.pasta: e for e in escolhidos}
    return list(unicos.values())
