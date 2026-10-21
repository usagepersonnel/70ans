# TODO

## Cohérence du dossier (passe du 04/10)

Principe : chaque info vit en un seul endroit — lore canonique dans `lore.md`, décisions et questions dans `lore_precisions.md`, game design dans `deroule.md`, terrain dans `reperage.md`, état et tâches dans ce fichier. Préfixes : `timeline_*` = documents de vérification (peuvent reprendre des infos d'ailleurs), `validation_*` = comptes rendus datés soumis à validation d'équipe, `ref_*` = références non vivantes.

- `lore.md` synchronisé avec les décisions validées (cycle 140 ans, cultistes conscients, statuette, mort d'Ivan, calendrier, planning du dimanche)
- `feuilles_rando.md` reste à réécrire une fois les points de lore tranchés (sac, squelette, voix)

Décisions validées en équipe (réunion du 04/10 — détail dans `lore_precisions.md` et `validation_2026-10-02.md`) :

- Pas de PNJ « enfant d'Ivan » pour l'instant : le carnet d'Ivan porte l'infodump et le code du site secret (réversible)
- Squelette du scialet ≠ fugitif (victime collectée par le triangle ; époque à choisir sans lieux de mémoire réels)
- Mapping des manifestations par groupe (miroirs→statuette, petit-déj→danse, voitures→terrain) : OK, textes à écrire

Décisions validées en équipe (réunion du 11/10 — détail dans `validation_2026-10-11.md`) :

- **Pas de communication entre équipes le samedi** : chaque arc est autonome — géoguesser et talkies abandonnés ; l'équipe tranquille fait une enquête complète (gîte → village → recoupements)
- **Bouteilles des parents** apportées au gîte comme décor : l'une cache un secret d'Ivan (ex. dernière carte à superposer)
- **Message de la statuette** écrit au « je » par un ancien Perchtenlauf — Mareva rédige
- Manifestations nocturnes = échos du passé confirmé, sources élargies (potentiellement d'anciens Perchtenlauf entre autres)
- Visite du cimetière voisin pendant le jeu : OK (jugé respectueux)

Reste à trancher :

- **Défiance envers la statuette** (demande du 11/10) : quels éléments concrets la rendent suspecte le samedi, pour que les joueurs finissent par la détruire ? Leviers existants : site d'Ivan, voyante, journal du fugitif, tableau

- Nature des voix de la forêt — contradiction avec « le maléfice n'a pas de volonté » (piste recommandée : échos/projection, pas d'entité)
- ~~Mécanisme de la voyante~~ — ✅ résolu : document (`documents_ivan/05`), pas de PNJ

## Incohérences connues (à résoudre)

Point d'entrée unique : on y ajoute toute contradiction repérée entre documents, et on la raye une fois résolue.
**Audit complet du 20/10** : `meta/audit_coherence_2026-10-20.md` (62 corrections 🟢 appliquées, 17 arbitrages 🟠 listés).

1. **Date du fugitif** — `lore.md` : « cycle précédent (~1886) » ; `feuilles_rando.md` : 1746, soit deux cycles avant 2026 (`timeline_lore.md` : 1886, 1746, 1606). À trancher avec Rémi. ⚠️ Impact site : `disparitions.astro` code déjà « vers 1746 ».
2. ~~**`lore.md` périmé**~~ — ✅ corrigé (passe du 20/10) : géoguesser, « transmettre aux équipes », PNJ enfant, noms de groupes, tableau, site jour 2.
3. ~~**Partie secrète du site**~~ — ✅ corrigé (20/10) : `lore_precisions.md` aligné sur l'accès samedi via les 4 clés.
4. ~~**Horaires du samedi**~~ — ✅ corrigé (20/10) : `lore.md`, `reperage.md`, `timeline_lore.md`, `deroule.md` alignés sur le lancement 14h + arcs autonomes.
5. ~~**Mort d'Ivan « récente »**~~ — ✅ déjà corrigé : `ivanbio.md` dit « décès en octobre 2025 ».
6. **Apparitions Perchten hors-cycle** — les 3 docs `ivan/Perchtenlauf *` (Loup 1894, Hiboux 1944, Bouquetin non daté) : si le rituel « éteint » le triangle ~140 ans, pourquoi des manifestations hors-cycle ? 💡 L'audit du 20/10 tranche en faveur de (a) : l'almanach (`slow_05`) ne liste que 1606/1746/1886 comme Grandes Veilles → ce sont des **patrouilles ordinaires** (« ils veillent » — le mot du tableau) ; le rituel ne se rejoue qu'en fin de cycle. À confirmer en équipe.
7. ~~**Doc Perchten manquant pour le Bouquetin**~~ → ✅ trio complet depuis le 20/10 (Seb a ajouté `ivan/Perchtenlauf bouquetin` — un article moderne sur un grimpeur masqué en free solo). **Reste à régler avec Seb** : le texte n'est pas daté, et l'apparition est à la **Grande Moucherotte** (nord Vercors, ~60 km du jeu — le texte de 1944 est lui local, « nord de Vassieux ») ; + placement des 3 textes en jeu (pochette `07` vs épinglés au gîte — `documents_ivan/07` dit aujourd'hui « pas encore trouvé de coupure » pour le bouquetin, l'absence est diegétique et peut rester).

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

### Lancement du samedi (décision 19/10)

- [x] Rédiger l'email de l'enfant d'Ivan (Camille) — `props_slow/slow_01` : commande annulée, père mort il y a un an, remboursement, ton triste, sans appel à répondre. **Reste : l'imprimer**
- [x] Rédiger l'**affiche déchirée** d'Ivan — `props_slow/slow_02` (version gîte déchirée + version café intacte). **Reste : vieillir, déchirer, accrocher**
- [ ] Café-librairie : créer l'**image** du tableau du chasseur + préparer les **tirages d'Ivan** à exposer (accord à compléter pour les tirages)
- [ ] Bambou (message du fugitif, arc de Rémi) : vérifier si on en a un, sinon trouver une alternative — à confirmer avec Rémi
- [ ] Décider et huiler comment les **3 groupes se forment et partent chacun avec leur référent (Batiste / Seb / Rémi)** à partir du lancement de 14h
- [ ] **Équipe Slow — météo pluie & rythme** : gîte à ~10 min à pied du centre-ville (un éclaireur peut refaire un aller-retour si un indice a été oublié), mais pluie annoncée → concentrer le temps au sec (gîte + café-librairie) et limiter les arrêts sous la pluie (cimetière, fontaine) à des vérifications rapides (5 min)

- [x] **Contenu du carnet d'Ivan rédigé (v1)** — `documents_ivan/` (7 pièces + index `00_README_carnet.md`) : notes & aide-mémoire des 4 clés, relevés 2011–2025, procès du notable, lettre de l'enfant, voyante, coupure accident « trois piétons », annexes 1894/1944
- [x] **Props de l'équipe Slow & lancement rédigés (v1)** — `props_slow/` (5 pièces + index `00_README_props_slow.md`) : email imprimé de l'enfant (`slow_01`), affiche déchirée/intacte (`slow_02`), livre d'or 2011 + portes des chambres (`slow_03`), tableau du chasseur + loupe (`slow_04`), énigme du vieux calendrier → 11h30 (`slow_05`)
- [ ] **Mise en forme & impression** des fichiers de `documents_ivan/` et `props_slow/` (une fois les retours de l'équipe intégrés)

- [x] **Spec complète écrite** — `ivan-beaulieu-photos/SPEC.md` (structure, gate à 4 clés, zone secrète, stack)
- [ ] **Questions en suspens** — voir `questions.md` (fontaine, photos repérage, chambres, plantes, dates d'Ivan…)
- [x] Construire la v1 : façade portfolio + journal + conférence + gate `/archives` (4 champs, API `/api/unlock`, cookie) — déployé et vérifié Playwright en prod ; audio = placeholder WAV en attendant les vrais enregistrements
- [ ] Déployer les variables d'env Vercel (`KEY_*`, `ARCHIVES_TOKEN`) avec les vraies valeurs — `ARCHIVES_TOKEN` à changer impérativement (le défaut est dans le code)
- [x] Choisir le mot caché dans le tableau du chasseur (clé 2) — **`VEILLE` retenu** (`props_slow/slow_04` ; double sens : « la veille » le samedi / « ils veillent » le dimanche — déjà configuré côté site)
- [ ] Remplacer les 3 WAV placeholder par les enregistrements de Mareva + photos de pièges réelles (page `/archives/pieges`)
- [ ] **PR de cohérence sur le site** (`ivan-beaulieu-photos` — workflow du repo : branche + PR, jamais de push direct sur `main`) :
  - `journal.ts` + `dossier.astro` : « quinze ans » → « vingt ans » (2 occurrences — Ivan affûte depuis 2005, cf. audit point K)
  - `sorties.astro` : « Réservations closes » → dater/préciser que c'est Camille qui a fermé le formulaire en découvrant notre réservation (oct. 2026) — sinon contradiction avec l'email de 14h qui dit que le site acceptait encore les résas (point J)
  - `audio.astro` : « trois nuits » → « trois veilles » (les 3 bandes datent du même week-end, cf. `documents_ivan/02`) + reformuler « le compteur s'est arrêté » + aligner le carnet d'écoute sur `rituel/enigmes_dimanche.md` (point L)
  - `disparitions.astro` : « vers 1746 » codé en dur → **ne pas toucher tant que Rémi n'a pas tranché** l'arbitrage A (1746 vs 1886)
  - Vérifier le déploiement preview Vercel de la PR avant merge

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
