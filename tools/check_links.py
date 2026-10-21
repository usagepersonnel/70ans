#!/usr/bin/env python3
"""Vérifie que les liens et chemins référencés dans les .md du repo existent.

Usage: uv run tools/check_links.py   (ou python tools/check_links.py)

Vérifie deux familles de références :
1. Les liens Markdown `](cible)` — résolus relativement au fichier qui les contient.
2. Les jetons entre backticks qui ressemblent à des chemins (`a/b.md`, `foo.md`) —
   résolus relativement à la racine du repo (convention du projet).
   Les fichiers du repo site voisin `ivan-beaulieu-photos` (*.astro, *.ts, SPEC.md…)
   sont résolus contre ce repo s'il est présent en dossier voisin.

Sortie : liste des références mortes. Code retour 1 s'il en reste.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SITE_REPO = REPO.parent / "ivan-beaulieu-photos"

# Dossiers figés (archives, snapshots, comptes rendus datés) : non vérifiés.
FROZEN_DIRS = {"archive", "decisions", ".git", "node_modules"}

# Jetons qui ressemblent à des chemins mais n'en sont pas (faux positifs connus).
NOT_PATHS = {
    ".env", ".env.example", "env.example", ".gitignore", "git status", "l.179",
    "ivan-beaulieu-photos.vercel.app",
}
# Fichiers supprimés/renommés cités volontairement comme historique (ex. dans les docs meta/).
KNOWN_GONE = {"Rituel.md", "scenario_statique.md"}
# Fichiers prévus mais pas encore produits (props à fabriquer).
PLANNED_FILES = {"00_03.mp3", "06_12.mp3", "18_47.mp3"}

DATE_TOKEN_RE = re.compile(r"^\d{2}/\d{2}/\d{4}$")

LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
BACKTICK_RE = re.compile(r"`([^`\n]+)`")
PATHISH_RE = re.compile(r"^[\w\-./~*]+$")


def md_files() -> list[Path]:
    files = []
    for p in sorted(REPO.rglob("*.md")):
        rel = p.relative_to(REPO)
        if rel.parts[0] in FROZEN_DIRS:
            continue
        files.append(p)
    return files


def token_is_pathlike(tok: str) -> bool:
    """Heuristique : le jeton ressemble-t-il à un chemin de repo ?"""
    if tok in NOT_PATHS or tok in PLANNED_FILES or tok in KNOWN_GONE:
        return False
    if DATE_TOKEN_RE.match(tok):
        return False
    if not PATHISH_RE.match(tok):
        return False
    if tok.startswith(("/", "~", "KEY_", "ARCHIVES_", "NODE_")):
        return False
    if "://" in tok or tok.startswith("mailto:"):
        return False
    if "/" not in tok and "." not in tok:
        return False
    if ".." in tok or tok.startswith("."):
        return False
    return True


def resolve_token(tok: str) -> bool:
    """Le jeton pointe-t-il vers quelque chose qui existe ?"""
    if (REPO / tok).exists():
        return True
    # Références préfixées vers le repo site voisin (`ivan-beaulieu-photos/...`)
    if tok.startswith("ivan-beaulieu-photos"):
        target = REPO.parent / tok
        if "*" in tok:
            parent, _, pattern = tok.rpartition("/")
            base = REPO.parent / parent
            return base.is_dir() and any(base.glob(pattern))
        return target.exists()
    if SITE_REPO.exists():
        # Basenames du repo site (journal.ts, pieges.astro, SPEC.md…) :
        # résolus dans src/ (récursif) ou à la racine du repo site.
        if "/" not in tok:
            src = SITE_REPO / "src"
            if src.is_dir() and any(src.rglob(tok)):
                return True
            if (SITE_REPO / tok).exists():
                return True
        elif (SITE_REPO / tok).exists():
            return True
    # Jetons avec wildcard (ex. `validation_*`, `perchtenlauf_*`, `timeline_*`)
    if "*" in tok:
        parent = REPO / tok.rsplit("/", 1)[0] if "/" in tok else REPO
        pattern = tok.rsplit("/", 1)[-1]
        if parent.is_dir() and any(parent.glob(pattern)):
            return True
    return False


def main() -> int:
    problems: list[str] = []
    for f in md_files():
        rel = f.relative_to(REPO)
        text = f.read_text(encoding="utf-8")

        for m in LINK_RE.finditer(text):
            target = m.group(1).split("#")[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (f.parent / target).resolve().exists():
                problems.append(f"{rel}: lien mort -> {target}")

        for m in BACKTICK_RE.finditer(text):
            for raw in m.group(1).split():
                tok = raw.strip("«»\"'.,;:()[]<>")
                if not token_is_pathlike(tok):
                    continue
                if not resolve_token(tok):
                    problems.append(f"{rel}: chemin introuvable `{tok}`")

    if problems:
        for p in problems:
            print(p)
        print(f"\n{len(problems)} référence(s) morte(s).")
        return 1
    print("OK — aucune référence morte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
