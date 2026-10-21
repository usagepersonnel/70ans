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

- `lore.md` — canon narratif (source de vérité)
- `lore_precisions.md` — décisions et questions de lore
- `deroule.md` — game design : équipes, déroulé, énigmes
- `enigmes.md` — cartographie du parcours joueur (étape → difficulté → déblocage)
- `feuilles_rando.md` — texte joueur de l'arc rando (récit du fugitif)
- `reperage.md` — checklist et retours terrain
- `retroplanning.md` — plan de travail à J-20
- `TODO.md` — état du projet, priorités, tâches
- `questions.md` — questions en suspens pour l'équipe + draft du message de synchro
- `documents_ivan/` — contenu de la pochette d'Ivan (7 pièces + index) — arc tranquille
- `props_slow/` — props du lancement et de l'arc tranquille
- `rituel/` — conception complète du rituel du dimanche (structure, partition des 12 sons, énigmes, checklist production)
- `ivan/` — biographie et photos d'Ivan Beaulieu (assets pour le site web)
- `meta/` — méthode, rapport et récap de la passe de cohérence (`methode_coherence.md`, `audit_coherence_2026-10-20.md`, `mise_en_coherence_etape1_recap.md`)
- `timeline_*.md` — chronologies de vérification
- `validation_*.md` — points soumis à validation d'équipe, datés
- `ref_*.md` — références non vivantes
- `code/` — script utilitaire Mermaid → markdown (non essentiel)

## 🎭 Synopsis du scénario

Des disparitions étranges ont lieu dans le Vercors depuis l'Antiquité. Le « Triangle du Vercors » est une zone mystérieuse où des phénomènes inexpliqués se produisent (distorsions temporelles, météo soudaine, voix anciennes).

**Points clés de l'intrigue** :

- Ivan Beaulieu, photographe animalier, a capturé des images d'êtres masqués dans la forêt avant de mourir dans un accident de la route (oct. 2025, un an avant le jeu). Il est convaincu qu'ils sont malveillants
- Les joueurs découvrent que ces êtres (liés au folklore Perchten) ne sont pas dangereux mais protègent contre les phénomènes étranges
- Un rituel de danse avec costumes spécifiques permet de désamorcer le « triangle » pour les 140 prochaines années (selon la qualité du rituel, les effets peuvent être plus ou moins atténués, voire le triangle complètement neutralisé)
- Le rituel doit être effectué le dimanche du changement d'heure d'octobre, avant 11h30 à la montre (10h au soleil + corrections, cf. `props_slow/slow_05`)

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
