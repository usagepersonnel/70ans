#!/usr/bin/env python3
"""Vérifie la cohérence des références entre les .md du repo.

Usage: python tools/check_links.py   (ou uv run tools/check_links.py)

Trois contrôles :
1. Les liens Markdown `](cible)` : résolus relativement au fichier qui les contient.
2. Les jetons entre backticks qui ressemblent à des chemins (`a/b.md`, `foo.md`) :
   résolus relativement à la racine du repo (convention du projet).
3. Les renvois aux questions (`questions.md` #N, marqueur ❓ #N, listes « #15 et #17 »,
   plages « #18–19 ») : chaque numéro doit exister dans `questions.md`, qui ne contient
   que des questions ouvertes. Un renvoi vers une question supprimée est donc signalé.

Exemptions :
- `archive/` et `decisions/` (documents figés) ne sont pas vérifiés.
- `meta/` (instantanés datés) n'est pas vérifié pour les renvois aux questions : ces
  fichiers ne sont pas mis à jour, leurs numéros peuvent légitimement devenir obsolètes.
- Les références vers le dépôt du site `ivan-beaulieu-photos` sont résolues contre le
  dossier voisin ; s'il est absent (cas d'un collègue), elles sont ignorées avec un avis.

Sortie : liste des problèmes. Code retour 1 s'il en reste.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SITE_REPO = REPO.parent / "ivan-beaulieu-photos"
QUESTIONS = REPO / "questions.md"

# Dossiers figés (archives, comptes rendus datés) : non vérifiés.
FROZEN_DIRS = {"archive", "decisions", ".git", "node_modules"}
# Dossiers dont les renvois aux questions ne sont pas vérifiés (instantanés datés).
SNAPSHOT_DIRS = {"meta", "archive", "decisions"}

# Jetons qui ressemblent à des chemins mais n'en sont pas (faux positifs connus).
NOT_PATHS = {
    ".env", ".env.example", "env.example", ".gitignore", "git status", "l.179",
    "ivan-beaulieu-photos.vercel.app",
}
# Fichiers supprimés ou renommés cités volontairement comme historique.
KNOWN_GONE = {"Rituel.md", "scenario_statique.md"}
# Fichiers locaux volontairement non versionnés (.gitignore) : ignorés s'ils sont absents.
KNOWN_LOCAL = {"meta/methode_coherence.md"}
# Fichiers prévus mais pas encore produits (props à fabriquer).
PLANNED_FILES = {"00_03.mp3", "06_12.mp3", "18_47.mp3"}
# Noms de fichiers du dépôt du site cités sans chemin complet.
SITE_BASENAMES = {"SPEC.md"}
SITE_SUFFIXES = (".astro", ".ts")

DATE_TOKEN_RE = re.compile(r"^\d{2}/\d{2}/\d{4}$")

LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
BACKTICK_RE = re.compile(r"`([^`\n]+)`")
PATHISH_RE = re.compile(r"^[\w\-./~*]+$")

QUESTION_LINE_RE = re.compile(r"^(\d+)\.\s")
# « questions.md #15 et #17 », « ❓ #16, #18 », « questions.md #18–19 »
QUESTION_REF_RE = re.compile(
    r"(?:questions\.md`?\)?|❓)\s*(#\d+(?:\s*(?:,|et|–)\s*#?\d+)*)"
)
RANGE_RE = re.compile(r"#?(\d+)\s*–\s*#?(\d+)")

skipped_site_refs: list[str] = []


def md_files(exclude: set[str]) -> list[Path]:
    files = []
    for p in sorted(REPO.rglob("*.md")):
        rel = p.relative_to(REPO)
        if rel.parts[0] in exclude:
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


def is_site_token(tok: str) -> bool:
    """Le jeton désigne-t-il un fichier du dépôt du site ?"""
    if tok.startswith(("ivan-beaulieu-photos", "src/")):
        return True
    return "/" not in tok and (tok in SITE_BASENAMES or tok.endswith(SITE_SUFFIXES))


def resolve_token(tok: str) -> bool:
    """Le jeton pointe-t-il vers quelque chose qui existe ?"""
    if (REPO / tok).exists() or tok in KNOWN_LOCAL:
        return True
    if is_site_token(tok):
        if not SITE_REPO.exists():
            skipped_site_refs.append(tok)
            return True
        if tok.startswith("ivan-beaulieu-photos"):
            if "*" in tok:
                parent, _, pattern = tok.rpartition("/")
                base = REPO.parent / parent
                return base.is_dir() and any(base.glob(pattern))
            return (REPO.parent / tok).exists()
        # Basenames du site (journal.ts, pieges.astro, SPEC.md…) : dans src/ ou à la racine.
        if "/" not in tok:
            src = SITE_REPO / "src"
            if src.is_dir() and any(src.rglob(tok)):
                return True
        return (SITE_REPO / tok).exists()
    # Jetons avec wildcard (ex. `validation_*`, `perchtenlauf_*`, `timeline_*`)
    if "*" in tok:
        parent = REPO / tok.rsplit("/", 1)[0] if "/" in tok else REPO
        pattern = tok.rsplit("/", 1)[-1]
        if parent.is_dir() and any(parent.glob(pattern)):
            return True
    return False


def open_question_ids(problems: list[str]) -> set[int]:
    """Numéros des questions de `questions.md` ; signale les doublons."""
    ids: list[int] = []
    for line in QUESTIONS.read_text(encoding="utf-8").splitlines():
        m = QUESTION_LINE_RE.match(line)
        if m:
            ids.append(int(m.group(1)))
    for n in sorted({i for i in ids if ids.count(i) > 1}):
        problems.append(f"questions.md: numéro de question en double -> #{n}")
    return set(ids)


def referenced_ids(sequence: str) -> set[int]:
    """Numéros désignés par « #15 et #17 », « #16, #18 » ou « #18–19 » (plage incluse)."""
    ids = {int(n) for n in re.findall(r"\d+", sequence)}
    for m in RANGE_RE.finditer(sequence):
        a, b = int(m.group(1)), int(m.group(2))
        ids.update(range(min(a, b), max(a, b) + 1))
    return ids


def check_paths(problems: list[str]) -> None:
    for f in md_files(FROZEN_DIRS):
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
                if token_is_pathlike(tok) and not resolve_token(tok):
                    problems.append(f"{rel}: chemin introuvable `{tok}`")


def check_question_refs(problems: list[str]) -> None:
    open_ids = open_question_ids(problems)
    for f in md_files(SNAPSHOT_DIRS):
        if f == QUESTIONS:
            continue
        rel = f.relative_to(REPO)
        for lineno, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for m in QUESTION_REF_RE.finditer(line):
                for n in sorted(referenced_ids(m.group(1)) - open_ids):
                    problems.append(
                        f"{rel}:{lineno}: renvoi à la question #{n}, absente de "
                        f"questions.md (répondue et supprimée, ou numéro inexistant)"
                    )


def main() -> int:
    problems: list[str] = []
    check_paths(problems)
    check_question_refs(problems)

    if skipped_site_refs:
        print(
            f"Avis : {len(skipped_site_refs)} référence(s) vers le dépôt du site ignorée(s) "
            f"(dossier voisin {SITE_REPO.name} absent)."
        )
    if problems:
        for p in problems:
            print(p)
        print(f"\n{len(problems)} problème(s).")
        return 1
    print("OK : aucune référence morte, tous les renvois aux questions sont valides.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
