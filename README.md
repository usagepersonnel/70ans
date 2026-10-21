# 70ans — Jeu de rôle grandeur nature dans le Vercors

Projet de conception d'un GN (jeu de rôle grandeur nature) sur le thème du Triangle du Vercors, du folklore Perchtenlauf et d'un rituel de conjuration séculaire.

## Ce qui compte

L'essentiel du projet est constitué de **fichiers Markdown** :

- `lore/lore.md` — Lore général : contexte, personnages, objets, rituel (source de vérité narrative)
- `lore/lore_precisions.md` — Décisions, pistes et questions ouvertes sur le lore --> à valider d'abord
- `design/deroule.md` — Répartition des équipes, déroulement et mécaniques d'énigmes
- `design/enigmes.md` — Cartographie du parcours joueur : étapes, difficultés, déblocages (tranche les questions ouvertes)
- `joueurs/rando/feuilles_rando.md` — Texte des feuilles trouvées par l'équipe rando (récit du fugitif)
- `design/reperage.md` — Checklist et retours de la visite terrain
- `design/retroplanning.md` — Plan de travail à J-20 (jalons, tâches par semaine, propriétaires)
- `TODO.md` — État du projet, priorités et tâches
- `questions.md` — Questions en suspens pour l'équipe + draft du message de synchro
- `joueurs/slow/pochette/` — Contenu de la pochette d'Ivan (7 pièces + index) — le cœur documentaire de l'arc tranquille
- `joueurs/slow/props/` — Props de lancement et de l'arc tranquille (email, affiche, livre d'or, tableau, calendrier)
- `joueurs/sportif/` — Espace de l'arc sportif (Seb) — parcours pièges photo et cache des Perchten
- `joueurs/rituel/` — Conception du rituel du dimanche (structure, 12 sons, énigmes, production) — fait foi pour le dimanche
- `assets/ivan/` — Bio et portraits d'Ivan · `assets/photos/` — clichés de pièges · `assets/sources/` — textes Perchtenlauf · `assets/cartes/` — cartes du dimanche
- `meta/` — méthode, rapport et récap de la passe de cohérence (`meta/methode_coherence.md`, `meta/audit_coherence_2026-10-20.md`, `meta/mise_en_coherence_etape1_recap.md`)
- `archive/` — Documents retirés de la conception courante (références, pas de mise à jour)
- `AGENTS.md` — Vue d'ensemble du projet, pour les IAs

Préfixes : `meta/timeline_*` = documents de vérification (`meta/timeline_lore.md`, `meta/timeline_rando.md`), `validation_*` = comptes rendus datés des réunions et points de validation (`decisions/validation_2026-10-02.md`, `decisions/validation_2026-10-11.md`, `decisions/validation_2026-10-19.md`), `ref_*` = références non vivantes (`archive/ref_archive.md`).

## Le dossier `tools/`

- `tools/check_links.py` — vérifie que les liens et chemins cités dans les `.md` existent (`python tools/check_links.py`)
- `tools/extract_excalidraw_text.py` + `tools/input/` — extraction de texte d'un board Excalidraw (brainstorm initial — non essentiel)
