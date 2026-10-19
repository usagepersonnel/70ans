# TODO

## Cohérence du dossier (passe du 04/10)

Principe : chaque info vit en un seul endroit — lore canonique dans `lore.md`, décisions et questions dans `lore_precisions.md`, game design dans `deroule.md`, terrain dans `reperage.md`, état et tâches dans ce fichier. Préfixes : `timeline_*` = documents de vérification (peuvent reprendre des infos d'ailleurs), `validation_*` = comptes rendus datés soumis à validation d'équipe, `ref_*` = références non vivantes.

- `lore.md` synchronisé avec les décisions validées (cycle 140 ans, cultistes conscients, statuette, mort d'Ivan, calendrier, planning du dimanche)
- `feuilles_rando.md` reste à réécrire une fois les points de lore tranchés (sac, squelette, voix)

Décisions validées en équipe (réunion du 04/10 — détail dans `lore_precisions.md` et `validation_2026-10-02.md`) :

- Pas de PNJ « enfant d'Ivan » pour l'instant : le carnet d'Ivan porte l'infodump et le code du site secret (réversible)
- Squelette du scialet ≠ fugitif (victime collectée par le triangle ; époque à choisir sans lieux de mémoire réels)
- Mapping des manifestations par groupe (douches/miroirs→statuette, petit-déj→rituel, voitures→lieu) : OK, textes à écrire

Décisions validées en équipe (réunion du 11/10 — détail dans `validation_2026-10-11.md`) :

- **Pas de communication entre équipes le samedi** : chaque arc est autonome — géoguesser et talkies abandonnés ; l'équipe tranquille fait une enquête complète (gîte → village → recoupements)
- **Bouteilles des parents** apportées au gîte comme décor : l'une cache un secret d'Ivan (ex. dernière carte à superposer)
- **Message de la statuette** écrit au « je » par un ancien Perchtenlauf — Mareva rédige
- Manifestations nocturnes = échos du passé confirmé, sources élargies (potentiellement d'anciens Perchtenlauf entre autres)
- Visite du cimetière voisin pendant le jeu : OK (jugé respectueux)

Reste à trancher :

- **Défiance envers la statuette** (demande du 11/10) : quels éléments concrets la rendent suspecte le samedi, pour que les joueurs finissent par la détruire ? Leviers existants : site d'Ivan, voyante, journal du fugitif, tableau

- Nature des voix de la forêt — contradiction avec « le maléfice n'a pas de volonté » (piste recommandée : échos/projection, pas d'entité)
- Mécanisme de la voyante — pas de lieu au village : PNJ au gîte (à caster) ou document (transcription de séance dans le carnet d'Ivan, cohérent avec « pas de PNJ »)

## Acquis du repérage terrain

- Lieu du rituel : champ circulaire, petit arbre, foyer — ~10 min en voiture + 1 min à pied
- Tableau du chasseur : accord du café/librairie
- Tombe sans inscription (candidate tombe du notable), fontaine datée avec ours (candidate « source » du fugitif), plantes à noms évocateurs (« Barbe de bouc » → ingrédients du rituel)
- Contraintes relevées : pas de givre (marqueurs craie), douches plastiques (→ miroirs), réseau faible (→ papier ; communication entre équipes de toute façon abandonnée le 11/10), OT fermé, pas de cadran solaire
- La grotte aux coordonnées connues est à ~23 km : les 3 points du triangle maillent la région, le centre tombe sur le champ du rituel

## Critiques de game design à adresser (une par une)

**Porte d'entrée (19/10)** : la cartographie du parcours joueur [`enigmes.md`](enigmes.md) tranche les points 1, 5, 6 et les questions pendantes de `validation_2026-10-19.md`. Le plus gros trou = l'arc sportif (mapping avec Seb requis).

1. **Verrou du twist** — sécuriser le timing et la mécanique de la destruction de la statuette : ni trop tôt (l'équipe rando seule l'après-midi), ni jamais (joueurs qui la conservent comme preuve)
2. **Dimanche trop serré** — pré-stager les matériaux, chorégraphie apprenable en ~20 min, recherche du lieu ≤30 min, trajet voiture intégré
3. ~~**Signal de réussite du rituel**~~ — ✅ résolu (`rituel/README.md` §4) : statuette échangée contre une version dorée + fumigènes sûrs (vert = parfait, orange = partiel) ; reste l'achat du matériel (`rituel/checklist_production.md`)
4. **Plans B météo et réseau** — pluie fin octobre probable (repli du rituel ?) ; couverture faible hors du gîte — partiellement résolu : pas de communication entre équipes le samedi (11/10), seul le site d'Ivan suppose le réseau (au gîte)
5. **« Aha » propre à l'équipe tranquille** — la fouille de la chambre d'Ivan est le meilleur candidat ; risque « guichet » écarté : l'arc est autonome depuis la décision du 11/10
6. **Casting PNJ** — le PNJ « enfant d'Ivan » est supprimé ; reste la voyante, uniquement si l'option PNJ est retenue (qui ?)
7. **Production** — costumes/masques pour tout le groupe le dimanche + props vieillis + site web : poste le plus lourd, à estimer tôt

## Tâches

### Histoire et contexte local

- [ ] Trouver des événements propres à la période du duché du Diois
- [ ] Se renseigner sur les cartes d'époques de la Chapelle en Vercors (OT fermé : mairie ou web)
- [ ] Définir les époques à étudier — ancrage fait pour le Moyen Âge (procès du notable), manque Antiquité / napoléonien / 2GM
- [ ] Identifier les événements marquants (séismes, etc.)

### Arc de l'équipe tranquille (samedi)

- [x] Décrire l'arc jouable — rédigé dans `deroule.md` (chambre d'Ivan → boucle village → recoupements au gîte → regroupement), arc autonome validé le 11/10
- [ ] Concevoir les éléments de **défiance envers la statuette** (décision 11/10) — répartis entre les arcs : site d'Ivan, voyante, journal du fugitif, tableau
- [ ] Arc équipe sportive : détailler le samedi (objets de destruction + costumes) — crée le verrou du twist

### Site web public

- [x] Créer un dépôt distinct dédié au site — fait : repo **privé** `ivan-beaulieu-photos` (Astro+TS), déployé sur Vercel → https://ivan-beaulieu-photos.vercel.app (zone secrète = gate serveur, pas de contenu sensible dans le repo public)
- [ ] Définir la frontière entre le contenu public et les éléments secrets du scénario — ne publier aucun indice ni contenu réservé à la partie secrète
- [ ] Créer la partie publique du site : photos animalières qui évoluent vers une enquête sur les êtres masqués
- [ ] Intégrer les photos de pièges photographiques dans le site

Note : le photographe a séjourné au gîte. Les joueurs peuvent découvrir quelle était sa chambre et y faire une fouille.

### Continuité / lore à trancher

- [ ] **Continuité de la randonnée** — `feuilles_rando.md` mentionne un squelette au Scialet Royer, mais le fugitif poursuit ensuite sa fuite (proposition : le squelette n'est pas le sien — victime collectée par le triangle, époque à choisir sans lieux de mémoire réels). Deux versions incompatibles du sac. Réécriture des feuilles une fois les points de lore tranchés.
- [ ] **Voix de la forêt** — elles manipulent le fugitif alors que le maléfice « n'a pas de volonté » : contradiction à trancher (options dans `lore_precisions.md`)

### Logistique

- [ ] **Cartes physiques** — acheter l'IGN du secteur + reproductions de cartes anciennes (Cassini, état-major). OT fermé : mairie ou web
- [ ] **Matériel des manifestations** — encre invisible adaptée aux miroirs (douches en plastique), marqueurs craie effaçables pour les voitures (pas de givre attendu)
- [x] **Communication entre équipes** — sans objet : pas de communication le samedi (décidé 11/10)
- [ ] **Prop bouteilles** — bouteilles des parents apportées au gîte comme décor ; préparer le secret d'Ivan à y cacher (ex. dernière carte à superposer)
