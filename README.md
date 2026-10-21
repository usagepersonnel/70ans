# 70ans — Jeu de rôle grandeur nature dans le Vercors

Projet de conception d'un GN (jeu de rôle grandeur nature) sur le thème du Triangle du Vercors, du folklore Perchtenlauf et d'un rituel de conjuration séculaire.

## Ce qui compte

L'essentiel du projet est constitué de **fichiers Markdown** :

- `lore/lore.md` — Lore général : contexte, personnages, objets, rituel (source de vérité narrative)
- `lore/lore_precisions.md` — Décisions, pistes et questions ouvertes sur le lore --> à valider d'abord
- `design/deroule.md` — Répartition des équipes, déroulement et mécaniques d'énigmes
- `design/enigmes.md` — Cartographie du parcours joueur : étapes, difficultés, déblocages (tranche les questions ouvertes)
- `joueurs/remi/feuilles_rando.md` — Texte des feuilles trouvées par l'équipe Rémi (récit du fugitif)
- `design/reperage.md` — Checklist et retours de la visite terrain
- `design/retroplanning.md` — Jalons et calendrier (le suivi des tâches est dans `TODO.md`)
- `TODO.md` — Tâches, responsables et état d'avancement (travail qui ne demande aucune décision)
- `questions.md` — Questions ouvertes pour l'équipe (ouvertes uniquement ; où vit chaque information : `AGENTS.md`)
- `joueurs/batiste/pochette/` — Contenu de la pochette d'Ivan (7 pièces + index) — le cœur documentaire de l'arc de Batiste
- `joueurs/batiste/props/` — Props de lancement et de l'arc de Batiste (email, affiche, livre d'or, tableau, calendrier)
- `joueurs/seb/` — Espace de l'arc de Seb (Seb) — parcours pièges photo et cache des Perchten
- `joueurs/rituel/` — Conception du rituel du dimanche (structure, 12 sons, énigmes, production) — fait foi pour le dimanche
- `assets/ivan/` — Bio et portraits d'Ivan · `assets/photos/` — clichés de pièges · `assets/sources/` — textes Perchtenlauf · `assets/cartes/` — cartes du dimanche
- `meta/` — méthode, rapport et récap de la passe de cohérence (`meta/audit_coherence_2026-10-20.md`, `meta/mise_en_coherence_etape1_recap.md`, et `meta/methode_coherence.md`, fichier local non versionné), cartographie structurelle du scénario (`meta/cartographie_scenario.md`) et message d'équipe (`meta/message_equipe_2026-10-21.md`). Ce sont des instantanés, pas des sources de faits
- `archive/` — Documents retirés de la conception courante (références, pas de mise à jour)
- `AGENTS.md` — Vue d'ensemble du projet, pour les IAs

Préfixes : `meta/timeline_*` = documents de vérification (`meta/timeline_lore.md`, `meta/timeline_rando.md`), `validation_*` = comptes rendus datés des réunions et points de validation (`decisions/validation_2026-10-02.md`, `decisions/validation_2026-10-11.md`, `decisions/validation_2026-10-19.md`), `ref_*` = références non vivantes (`archive/ref_archive.md`).

## Le dossier `tools/`

- `tools/check_links.py` — vérifie les liens, les chemins cités dans les `.md` et les renvois aux questions (`questions.md` #N) : `python tools/check_links.py`
- `tools/extract_excalidraw_text.py` + `tools/input/` — extraction de texte d'un board Excalidraw (brainstorm initial — non essentiel)
