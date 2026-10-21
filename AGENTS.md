# AGENTS - Documentation du Projet

## 📋 Vue d'ensemble

Ce projet vise à préparer un **jeu de piste grandeur nature** pour l'anniversaire de Bill et Monique (70 ans).

- **Lieu** : Massif du Vercors (région du Diois)
- **Format** : Jeu sur un week-end (samedi + dimanche) avec 3 équipes superposées
- **Équipes** : 3 niveaux de compétences sportives (débutants, amateurs, athlètes)
- **Thème** : Mystère historique et folklore alpin avec éléments surnaturels (dilatation espace-temps)

## 👥 Équipe de création

- **Batiste** - Création du dossier, développement web (site d'Ivan, repo privé `ivan-beaulieu-photos` déployé sur Vercel)
- **Mareva** - Création du jeu
- **Rémi** - Création du jeu
- **Sébastien (Seb)** - Création du jeu

## Equipes

- Les 3 équipes coexistent sur le terrain
- Jour 1 : séparation avec un but chacun (+ ou - physique)
- Jour 2 : rituel ensemble

## 📁 Structure du projet

- `lore/lore.md` — canon narratif (source de vérité)
- `lore/lore_precisions.md` — décisions et questions de lore
- `design/deroule.md` — game design : équipes, déroulé, énigmes
- `design/enigmes.md` — cartographie du parcours joueur (étape → difficulté → déblocage)
- `joueurs/rando/feuilles_rando.md` — texte joueur de l'arc rando (récit du fugitif)
- `design/reperage.md` — checklist et retours terrain
- `design/retroplanning.md` — plan de travail à J-20
- `TODO.md` — état du projet, priorités, tâches
- `questions.md` — questions en suspens pour l'équipe + draft du message de synchro
- `joueurs/slow/pochette/` — contenu de la pochette d'Ivan (7 pièces + index) — arc tranquille
- `joueurs/slow/props/` — props du lancement et de l'arc tranquille
- `joueurs/sportif/` — espace de l'arc sportif (Seb)
- `joueurs/rituel/` — conception complète du rituel du dimanche (structure, partition des 12 sons, énigmes, checklist production)
- `assets/` — bio/portraits (`assets/ivan/`), clichés de pièges (`assets/photos/`), textes Perchtenlauf (`assets/sources/`), cartes (`assets/cartes/`)
- `meta/` — méthode, rapport et récap de la passe de cohérence (`meta/methode_coherence.md`, `meta/audit_coherence_2026-10-20.md`, `meta/mise_en_coherence_etape1_recap.md`) et cartographie structurelle du scénario (`meta/cartographie_scenario.md`)
- `meta/timeline_*.md` — chronologies de vérification
- `decisions/validation_*.md` — points soumis à validation d'équipe, datés
- `archive/` — snapshots et références non vivantes (`archive/ref_*.md`, `archive/excalidraw/`)
- `tools/` — `tools/check_links.py` (vérification des références) + extraction Excalidraw (non essentiel)

## 🧭 Conventions de nommage

- Fichiers : minuscules, `snake_case`, ASCII, extension `.md` obligatoire.
- Comptes rendus datés : `decisions/validation_*.md` — figés, ne pas réécrire.
- Séquences ordonnées (pièces de la pochette, props) : préfixe `NN_`.
- Contenu joueur : un dossier par équipe dans `joueurs/`, chacun avec un `README.md` d'index.
- Références entre docs : chemins relatifs à la racine du repo, entre backticks ; liens `[x](...)` relatifs au fichier.
- Avant de merger un déplacement : `python tools/check_links.py` doit répondre « aucune référence morte ».

## 🎭 Synopsis du scénario

Des disparitions étranges ont lieu dans le Vercors depuis l'Antiquité. Le « Triangle du Vercors » est une zone mystérieuse où des phénomènes inexpliqués se produisent (distorsions temporelles, météo soudaine, voix anciennes).

**Points clés de l'intrigue** :

- Ivan Beaulieu, photographe animalier, a capturé des images d'êtres masqués dans la forêt avant de mourir dans un accident de la route (oct. 2025, un an avant le jeu). Il est convaincu qu'ils sont malveillants
- Les joueurs découvrent que ces êtres (liés au folklore Perchten) ne sont pas dangereux mais protègent contre les phénomènes étranges
- Un rituel de danse avec costumes spécifiques permet de désamorcer le « triangle » pour les 140 prochaines années (selon la qualité du rituel, les effets peuvent être plus ou moins atténués, voire le triangle complètement neutralisé)
- Le rituel doit être effectué le dimanche du changement d'heure d'octobre, avant 11h30 à la montre (10h au soleil + corrections, cf. `joueurs/slow/props/05_enigme_vieux_calendrier.md`)

**Progression narrative (mécanisme de révélation)** :

Le scénario utilise une structure de **fausse prise de conscience** avec retournement :

1. **Phase 1 - Mise en place** : Découverte des phénomènes étranges et du triangle
   - Les joueurs découvrent les disparitions et les photos d'Ivan Beaulieu
   - L'ambiance suggère une menace surnaturelle ou une "dissimulation de menace"

2. **Phase 2 - Fausses pistes** : Investigation sur les êtres masqués
   - Les joueurs croient que les êtres masqués sont dangereux
   - Un "piège qui fait peur" les pousse à vouloir briser un objet magique/rituel
   - Croyance erronée : ils pensent que cela résoudra la malédiction

Fin du jour 1 : les joueurs détruisent la statuette

3. **Phase 3 - Retournement** : Compréhension que les êtres masqués sont bienveillants
   - Après avoir brisé l'objet : prise de conscience que c'était une erreur
   - Les Perchten étaient des protecteurs, pas des menaces
   - Nécessité de réparer/réaliser le rituel correctement

4. **Phase 4 - Résolution** : Apprentissage du rituel et préparation du final
   - Recherche des costumes, masques et chorégraphie corrects
   - Le rituel du changement d'heure pour désamorcer le triangle

## 📚 Tâches de recherche en cours

### Web

- Créer un site web avec des photos animalières qui virent vers la théorie du complot (tâche pour Batiste — Astro+TS, repo privé `ivan-beaulieu-photos`, Vercel)
