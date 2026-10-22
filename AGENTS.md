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
- **Nommage (21/10)** : les équipes portent le prénom de leur référent — **équipe Batiste** (village/gîte), **équipe Seb** (~200 m D+), **équipe Rémi** (grande rando des crêtes). Niveau physique croissant : Batiste < Seb < Rémi. Les dossiers `joueurs/` suivent ce nommage ; les anciens labels « slow / rando / sportif » sont abandonnés (ils restent dans les fichiers figés `meta/`, `decisions/` et `archive/`).

## 📁 Structure du projet

- `lore/lore.md` — canon narratif (source de vérité)
- `lore/lore_precisions.md` — décisions et questions de lore
- `design/deroule.md` — game design : équipes, déroulé, énigmes
- `design/enigmes.md` — cartographie du parcours joueur (étape → difficulté → déblocage)
- `joueurs/remi/feuilles_rando.md` — texte joueur de l'arc de Rémi (récit du fugitif)
- `design/reperage.md` — checklist et retours terrain
- `design/retroplanning.md` — jalons et calendrier (le suivi des tâches est dans `TODO.md`)
- `TODO.md` — tâches, responsables et état d'avancement (travail qui ne demande aucune décision)
- `questions.md` — questions ouvertes pour l'équipe (ouvertes uniquement ; règles en tête du fichier)
- `joueurs/batiste/pochette/` — contenu de la pochette d'Ivan (7 pièces + index) — arc de Batiste
- `joueurs/batiste/props/` — props du lancement et de l'arc de Batiste
- `joueurs/seb/` — espace de l'arc de Seb
- `joueurs/rituel/` — conception complète du rituel du dimanche (structure, partition des 12 sons, énigmes, checklist production)
- `assets/` — bio/portraits (`assets/ivan/`), clichés de pièges (`assets/photos/`), textes Perchtenlauf (`assets/sources/`), cartes (`assets/cartes/`)
- `meta/` — analyses subsidiaires et instantanés datés, **jamais une source de faits** : méthode, rapport et récap de la passe de cohérence (`meta/audit_coherence_2026-10-20.md`, `meta/mise_en_coherence_etape1_recap.md`, et `meta/methode_coherence.md`, fichier local non versionné), cartographie structurelle du scénario (`meta/cartographie_scenario.md`), message d'équipe (`meta/message_equipe_2026-10-21.md`)
- `meta/timeline_*.md` — chronologies de vérification
- `decisions/validation_*.md` — points soumis à validation d'équipe, datés
- `archive/` — snapshots et références non vivantes (`archive/ref_*.md`, `archive/excalidraw/`)
- `tools/` — `tools/check_links.py` (vérification des références) + extraction Excalidraw (non essentiel)

## Où vit l'information (single source of truth)

Chaque information vit à **un seul endroit**. Les autres documents y renvoient par un chemin ou un lien ; ils ne la recopient pas.

| Type d'information | Document qui fait foi |
|---|---|
| Fait narratif (personnages, objets, dates, cycle de 140 ans, description d'un objet) | `lore/lore.md` |
| Décision de lore et son contexte | `lore/lore_precisions.md` |
| Parcours joueur, énigmes, déblocages | `design/enigmes.md` |
| Équipes, déroulé, mécaniques | `design/deroule.md` |
| Terrain et repérage | `design/reperage.md` |
| Jalons et calendrier (le suivi des tâches est dans `TODO.md`) | `design/retroplanning.md` |
| Texte joueur et fabrication d'un prop | `joueurs/<équipe>/` (un fichier par prop) |
| Dimanche et rituel | `joueurs/rituel/` |
| Tâche, responsable et état d'avancement (travail qui ne demande aucune décision) | `TODO.md` |
| Question ouverte à un membre de l'équipe | `questions.md` (questions ouvertes uniquement) |
| Décision prise en réunion (datée, figée) | `decisions/` |
| Analyse, audit, vérification, message d'équipe | `meta/` (instantanés, jamais source de faits) |

Règles :

- Une réponse à une question s'écrit dans le document qui fait foi, puis la question est supprimée de `questions.md` (les règles détaillées sont en tête de ce fichier).
- `meta/` est **subsidiaire** : une analyse n'est pas un lieu de stockage. On ne met pas à jour ces fichiers après coup. Un problème repéré dans `meta/` se règle dans le document qui fait foi, et se suit dans `TODO.md` ou `questions.md`.
- Si deux documents se contredisent, celui qui fait foi l'emporte ; on corrige l'autre.
- Les ❓ placés dans les documents de design (`lore/lore_precisions.md`, `design/deroule.md`, `design/enigmes.md`) restent attachés à leur contexte ; les questions qui attendent la réponse d'une personne précise sont listées dans `questions.md`.

## Points de vigilance (repo du site `ivan-beaulieu-photos`)

- **Branche prop/almanach** : branche **locale uniquement**, qui porte les pages de props imprimables (`src/pages/almanach.astro`, `src/pages/dossier-parcours.astro`, et les suivantes). **Ne jamais la pousser ni la fusionner dans `main`** (le merge déploierait ces pages sur le site public). Avant de reprendre le travail normal du site, revenir sur `main` (`git switch main`) et partir de là pour toute nouvelle branche ; vérifier la branche courante avant tout commit sur le site.
- Les fichiers imprimables produits (PDF/PNG) se déposent dans `assets/photos/site_ivan/`, avec une section « Fichier imprimable » dans le doc du prop.

## 🧭 Conventions de nommage

- Documents Markdown : minuscules, `snake_case`, ASCII, extension `.md`. Images : noms parlants, en minuscules et sans espace pour les nouveaux fichiers ; les noms déjà cités ailleurs ne sont pas renommés.
- Comptes rendus datés : `decisions/validation_*.md` — figés, ne pas réécrire.
- Séquences ordonnées (pièces de la pochette, props) : préfixe `NN_`.
- Contenu joueur : un dossier par équipe dans `joueurs/`, chacun avec un `README.md` d'index.
- Références entre docs : chemins relatifs à la racine du repo, entre backticks ; liens `[x](...)` relatifs au fichier.
- Renvoi à une question : `questions.md` #N ou ❓ #N, avec N un numéro stable de `questions.md`.
- Avant de pousser (déplacement de fichier, suppression d'une question) : `python tools/check_links.py` doit répondre OK. Il vérifie les liens, les chemins cités et les renvois aux questions ; si le dépôt voisin `ivan-beaulieu-photos` est absent, les références vers le site sont ignorées avec un avis.

## 🎭 Synopsis du scénario

Des disparitions étranges ont lieu dans le Vercors depuis l'Antiquité. Le « Triangle du Vercors » est une zone mystérieuse où des phénomènes inexpliqués se produisent (distorsions temporelles, météo soudaine, voix anciennes).

**Points clés de l'intrigue** :

- Ivan Beaulieu, photographe animalier, a capturé des images d'êtres masqués dans la forêt avant de mourir dans un accident de la route (oct. 2025, un an avant le jeu). Il est convaincu qu'ils sont malveillants
- Les joueurs découvrent que ces êtres (liés au folklore Perchten) ne sont pas dangereux mais protègent contre les phénomènes étranges
- Un rituel de danse avec costumes spécifiques permet de désamorcer le « triangle » pour les 140 prochaines années (selon la qualité du rituel, les effets peuvent être plus ou moins atténués, voire le triangle complètement neutralisé)
- Le rituel doit être effectué le dimanche du changement d'heure d'octobre, avant 11h30 à la montre (10h au soleil + corrections, cf. `joueurs/batiste/props/05_enigme_vieux_calendrier.md`)

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

