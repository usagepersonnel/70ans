# TODO

## Cohérence du dossier (passe du 04/10)

Principe : chaque info vit en un seul endroit — lore canonique dans `lore/lore.md`, décisions et questions dans `lore/lore_precisions.md`, game design dans `design/deroule.md`, terrain dans `design/reperage.md`, état et tâches dans ce fichier. Préfixes : `meta/timeline_*` = documents de vérification (peuvent reprendre des infos d'ailleurs), `validation_*` = comptes rendus datés soumis à validation d'équipe, `ref_*` = références non vivantes.

- `lore/lore.md` synchronisé avec les décisions validées (cycle 140 ans, cultistes conscients, statuette, mort d'Ivan, calendrier, planning du dimanche)
- `joueurs/rando/feuilles_rando.md` reste à réécrire une fois les points de lore tranchés (sac, squelette, voix)

Décisions validées en équipe (réunion du 04/10 — détail dans `lore/lore_precisions.md` et `decisions/validation_2026-10-02.md`) :

- Pas de PNJ « enfant d'Ivan » pour l'instant : la pochette d'Ivan porte l'infodump et le code du site secret (réversible)
- Squelette du scialet ≠ fugitif (victime collectée par le triangle ; époque à choisir sans lieux de mémoire réels)
- Mapping des manifestations par groupe (miroirs→statuette, petit-déj→danse, voitures→terrain) : OK, textes à écrire

Décisions validées en équipe (réunion du 11/10 — détail dans `decisions/validation_2026-10-11.md`) :

- **Pas de communication entre équipes le samedi** : chaque arc est autonome — géoguesser et talkies abandonnés ; l'équipe tranquille fait une enquête complète (gîte → village → recoupements)
- **Bouteilles des parents** apportées au gîte comme décor : l'une cache un secret d'Ivan (ex. dernière carte à superposer)
- **Message de la statuette** écrit au « je » par un ancien Perchtenlauf — Mareva rédige
- Manifestations nocturnes = échos du passé confirmé, sources élargies (potentiellement d'anciens Perchtenlauf entre autres)
- Visite du cimetière voisin pendant le jeu : OK (jugé respectueux)

Reste à trancher :

- **Défiance envers la statuette** (demande du 11/10) : quels éléments concrets la rendent suspecte le samedi, pour que les joueurs finissent par la détruire ? Leviers existants : site d'Ivan, voyante, journal du fugitif, tableau

- **Scène de destruction de 17h30** (21/10) : piste de Batiste, un rituel sommaire avec les 3 masques + la statuette, **à confirmer avec la team** (`questions.md` #20) ; le texte du message caché reste à écrire (Mareva)
- ~~**Zone secrète du site, côté samedi**~~ — ✅ **accepté le 21/10 (Batiste)** : pas de verrouillage de l'audio. Slow aura tous les éléments le samedi soir (le carnet d'écoute donne déjà la clé du groupe danse) mais n'y verra pas forcément d'intérêt ; au pire ils se diront « c'est nul » : risque assumé. Option restante, facultative : une pièce lisible et marquante dans la zone dès le samedi. Voir `meta/cartographie_scenario.md` §5.4 et §6
- **Équipe sportive** (21/10) : objectif annoncé à 14h15, étapes, raison de détruire la statuette. Seb a promis de répondre (« ce soir ou quand j'ai du temps »)
- Nature des voix de la forêt — contradiction avec « le maléfice n'a pas de volonté » (piste recommandée : échos/projection, pas d'entité)
- ~~Mécanisme de la voyante~~ — ✅ résolu : document (`joueurs/slow/pochette/05_transcription_voyante.md`), pas de PNJ

## Incohérences connues (à résoudre)

Point d'entrée unique : on y ajoute toute contradiction repérée entre documents, et on la raye une fois résolue.
**Audit complet du 20/10** : `meta/audit_coherence_2026-10-20.md` (62 corrections 🟢 appliquées, 17 arbitrages 🟠 listés).

1. **Date du fugitif** — `lore/lore.md` : « cycle précédent (~1886) » ; `joueurs/rando/feuilles_rando.md` : 1746, soit deux cycles avant 2026 (`meta/timeline_lore.md` : 1886, 1746, 1606). À trancher avec Rémi. ⚠️ Impact site : `disparitions.astro` code déjà « vers 1746 ».
2. ~~**`lore/lore.md` périmé**~~ — ✅ corrigé (passe du 20/10) : géoguesser, « transmettre aux équipes », PNJ enfant, noms de groupes, tableau, site jour 2.
3. ~~**Partie secrète du site**~~ — ✅ corrigé (20/10) : `lore/lore_precisions.md` aligné sur l'accès samedi via les 4 clés.
4. ~~**Horaires du samedi**~~ — ✅ corrigé (20/10) : `lore/lore.md`, `design/reperage.md`, `meta/timeline_lore.md`, `design/deroule.md` alignés sur le lancement 14h + arcs autonomes.
5. ~~**Mort d'Ivan « récente »**~~ — ✅ déjà corrigé : `assets/ivan/ivanbio.md` dit « décès en octobre 2025 ».
6. **Apparitions Perchten hors-cycle** — les 3 docs `assets/sources/perchtenlauf_*` (Loup 1894, Hiboux 1944, Bouquetin non daté) : si le rituel « éteint » le triangle ~140 ans, pourquoi des manifestations hors-cycle ? 💡 L'audit du 20/10 tranche en faveur de (a) : l'almanach (`joueurs/slow/props/05_enigme_vieux_calendrier.md`) ne liste que 1606/1746/1886 comme Grandes Veilles → ce sont des **patrouilles ordinaires** (« ils veillent » — le mot du tableau) ; le rituel ne se rejoue qu'en fin de cycle. À confirmer en équipe.
7. ~~**Doc Perchten manquant pour le Bouquetin**~~ → ✅ trio complet depuis le 20/10 (Seb a ajouté `assets/sources/perchtenlauf_bouquetin.md` — un article moderne sur un grimpeur masqué en free solo). **Reste à régler avec Seb** : le texte n'est pas daté, et l'apparition est à la **Grande Moucherotte** (nord Vercors, ~60 km du jeu — le texte de 1944 est lui local, « nord de Vassieux ») ; + placement des 3 textes en jeu (pochette `07` vs épinglés au gîte — `joueurs/slow/pochette/07_annexes_1894_1944.md` dit aujourd'hui « pas encore trouvé de coupure » pour le bouquetin, l'absence est diegétique et peut rester).

## Acquis du repérage terrain

- Lieu du rituel : champ circulaire, petit arbre, foyer — ~10 min en voiture + 1 min à pied
- Tableau du chasseur : accord du café/librairie
- Tombe sans inscription (candidate tombe du notable), fontaine à statues d'ours (~1,5 m) et dates gravées 1894-1994 (clé 1 ; ce n'est pas la « source » du fugitif, qui est en montagne), plantes à noms évocateurs (« Barbe de bouc » → ingrédients du rituel)
- Contraintes relevées : pas de givre (marqueurs craie), douches plastiques (→ miroirs), réseau faible (→ papier ; communication entre équipes de toute façon abandonnée le 11/10), OT fermé, pas de cadran solaire
- La grotte aux coordonnées connues est à ~23 km : les 3 points du triangle maillent la région, le centre tombe sur le champ du rituel

## Critiques de game design à adresser (une par une)

**Porte d'entrée (19/10)** : la cartographie du parcours joueur [`design/enigmes.md`](design/enigmes.md) tranche les points 1, 5, 6 et les questions pendantes de `decisions/validation_2026-10-19.md`. Le plus gros trou = l'arc sportif (mapping avec Seb requis).

1. **Verrou du twist** — sécuriser le timing et la mécanique de la destruction de la statuette : ni trop tôt (l'équipe rando seule l'après-midi), ni jamais (joueurs qui la conservent comme preuve)
2. **Dimanche trop serré** — pré-stager les matériaux, chorégraphie apprenable en ~20 min, recherche du lieu ≤30 min, trajet voiture intégré
3. ~~**Signal de réussite du rituel**~~ — ✅ résolu (`joueurs/rituel/README.md` §4) : statuette échangée contre une version dorée + fumigènes sûrs (vert = parfait, orange = partiel) ; reste l'achat du matériel (`joueurs/rituel/checklist_production.md`)
4. **Plans B météo et réseau** — **prévision du 21/10 : pas de pluie samedi (~8°C), pluie dimanche** ; couverture faible hors du gîte — partiellement résolu : pas de communication entre équipes le samedi (11/10), seul le site d'Ivan suppose le réseau (au gîte). **Réseau : risque accepté le 21/10** ; repli = demander le wifi au personnel du gîte, ou aller au café-librairie
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

- [x] Décrire l'arc jouable — rédigé dans `design/deroule.md` (chambre d'Ivan → boucle village → recoupements au gîte → regroupement), arc autonome validé le 11/10
- [ ] Concevoir les éléments de **défiance envers la statuette** (décision 11/10) — répartis entre les arcs : site d'Ivan, voyante, journal du fugitif, tableau
- [ ] Arc équipe sportive : détailler le samedi (objets de destruction + costumes) — crée le verrou du twist

### Lancement du samedi (décision 19/10)

- [x] Rédiger l'email de l'enfant d'Ivan (Camille) — `joueurs/slow/props/01_lancement_email_enfant.md` : commande annulée, père mort il y a un an, remboursement, ton triste, sans appel à répondre. **Reste : l'imprimer**
- [x] Rédiger l'**affiche déchirée** d'Ivan — `joueurs/slow/props/02_affiche_habitants_de_la_nuit.md` (version gîte déchirée + version café intacte). **Reste : vieillir, déchirer, accrocher**
- [ ] Café-librairie : créer l'**image** du tableau du chasseur + préparer les **tirages d'Ivan** à exposer (accord à compléter pour les tirages)
- [ ] **Écrire les 3 dossiers de parcours** promis par l'email de Camille (une enveloppe par équipe, posée à côté de l'email) : c'est probablement la réponse à « premier indice à 14h15 » (`questions.md` #16). Slow : Batiste ; Sportif : Seb ; Rando : Rémi (la 1re feuille du fugitif, « jointe en l'état »). Objectif : rapide, un feuillet chacun
- [ ] Bambou (message du fugitif, arc de Rémi) : vérifier si on en a un, sinon trouver une alternative — à confirmer avec Rémi (en lien avec le dossier Rando ci-dessus)
- [ ] **Référent par équipe comme filet de sécurité** (21/10) : Batiste / Seb / Rémi aident leur équipe si un trophée n'est pas livré (statuette, masques). À cadrer vendredi : heure limite après laquelle le référent intervient (ex. 16h45) et ce qu'il peut donner comme coup de pouce
- [ ] Décider et huiler comment les **3 groupes se forment et partent chacun avec leur référent (Batiste / Seb / Rémi)** à partir du lancement de 14h
- [ ] **Équipe Slow — météo pluie & rythme** : gîte à ~10 min à pied du centre-ville (un éclaireur peut refaire un aller-retour si un indice a été oublié), prévision du 21/10 : **pas de pluie samedi, ~8°C**. Garder des arrêts extérieurs courts (cimetière, fontaine : vérifications de 5 min, à cause du froid et au cas où la prévision change) et le café-librairie comme abri

- [x] **Contenu de la pochette d'Ivan rédigé (v1)** — `joueurs/slow/pochette/` (7 pièces + index `joueurs/slow/pochette/README.md`) : notes & aide-mémoire des 4 clés, relevés 2011–2025, procès du notable, lettre de l'enfant, voyante, coupure accident « trois piétons », annexes 1894/1944
- [x] **Props de l'équipe Slow & lancement rédigés (v1)** — `joueurs/slow/props/` (5 pièces + index `joueurs/slow/props/README.md`) : email imprimé de l'enfant (`joueurs/slow/props/01_lancement_email_enfant.md`), affiche déchirée/intacte (`joueurs/slow/props/02_affiche_habitants_de_la_nuit.md`), livre d'or 2011 + portes des chambres (`joueurs/slow/props/03_livre_dor_2011_chambre.md`), tableau du chasseur + loupe (`joueurs/slow/props/04_tableau_chasseur_et_loupe.md`), énigme du vieux calendrier → 11h30 (`joueurs/slow/props/05_enigme_vieux_calendrier.md`)
- [ ] **Mise en forme & impression** des fichiers de `joueurs/slow/pochette/` et `joueurs/slow/props/` (une fois les retours de l'équipe intégrés)

- [x] **Spec complète écrite** — `ivan-beaulieu-photos/SPEC.md` (structure, gate à 4 clés, zone secrète, stack)
- [ ] **Questions en suspens** — voir `questions.md` (fontaine, photos repérage, chambres, plantes, dates d'Ivan…)
- [x] Construire la v1 : façade portfolio + journal + conférence + gate `/archives` (4 champs, API `/api/unlock`, cookie) — déployé et vérifié Playwright en prod ; audio = placeholder WAV en attendant les vrais enregistrements
- [ ] Déployer les variables d'env Vercel (`KEY_*`, `ARCHIVES_TOKEN`) avec les vraies valeurs — `ARCHIVES_TOKEN` à changer impérativement (le défaut est dans le code). **Clé 1 connue depuis le 21/10** (fontaine gravée « 1894-1994 ») : sans modification de code, régler `KEY_FOUNTAIN` sur `1894;1994;1894 1994;1994 1894` (le séparateur est `;`, la comparaison ignore casse, accents et tirets), puis **redéployer** pour que la valeur soit prise en compte. Le défaut du code (`1878`) est faux
- [x] Choisir le mot caché dans le tableau du chasseur (clé 2) — **`VEILLE` retenu** (`joueurs/slow/props/04_tableau_chasseur_et_loupe.md` ; double sens : « la veille » le samedi / « ils veillent » le dimanche — déjà configuré côté site)
- [ ] Remplacer les 3 WAV placeholder par les enregistrements de Mareva + photos de pièges réelles (page `/archives/pieges`) — **montage audio en cours (Batiste, 21/10)** ; photos de pièges encore à shooter
- [ ] **PR de cohérence sur le site** (`ivan-beaulieu-photos` — workflow du repo : branche + PR, jamais de push direct sur `main`) :
  - `journal.ts` + `dossier.astro` : « quinze ans » → « vingt ans » (2 occurrences — Ivan affûte depuis 2005, cf. audit point K)
  - `sorties.astro` : « Réservations closes » → dater/préciser que c'est Camille qui a fermé le formulaire en découvrant notre réservation (oct. 2026) — sinon contradiction avec l'email de 14h qui dit que le site acceptait encore les résas (point J)
  - `audio.astro` : « trois nuits » → « trois veilles » (les 3 bandes datent du même week-end, cf. `joueurs/slow/pochette/02_releves_2011_2025.md`) + reformuler « le compteur s'est arrêté » + aligner le carnet d'écoute sur `joueurs/rituel/enigmes_dimanche.md` (point L)
  - `keys.ts` + `.env.example` : défaut de la clé 1 `1878` → `1894` / `1994`, et passer cette clé en comparaison « contient » (comme la clé 3) pour accepter « de 1894 à 1994 » ; adapter le libellé du champ dans `ivan-beaulieu-photos/src/pages/archives/index.astro` (« L'année gravée » → « Les dates gravées »)
  - (optionnel, détail sans importance) `ivan-beaulieu-photos/src/lib/auth.ts` : durée du cookie `COOKIE_MAX_AGE` de 4 h à 48 h, pour que l'équipe Slow n'ait pas à ressaisir les clés le dimanche (c'est un site de jeu, pas une banque)
  - `dossier.astro` : **réécrire le paragraphe où Ivan doute** (« ce que j'ai pris pour de la malveillance pendant trop longtemps, je commence à me demander si ce n'est pas autre chose »), qui contredit la certitude d'Ivan et affaiblit le retournement. Proposition : « Ils ne sont pas des rêves. Ils viennent quand l'heure change, ils ont toujours trois pas d'avance sur la mémoire des gens, et chaque année je suis un peu plus certain qu'ils ne nous veulent aucun bien. » (Le passage de `journal.ts` « pourrait être autre chose » parle des animaux, il reste cohérent.)
  - `disparitions.astro` : « vers 1746 » codé en dur → **ne pas toucher tant que Rémi n'a pas tranché** l'arbitrage A (1746 vs 1886)
  - Vérifier le déploiement preview Vercel de la PR avant merge

- [x] Créer un dépôt distinct dédié au site — fait : repo **privé** `ivan-beaulieu-photos` (Astro+TS), déployé sur Vercel → https://ivan-beaulieu-photos.vercel.app (zone secrète = gate serveur, pas de contenu sensible dans le repo public)
- [ ] Définir la frontière entre le contenu public et les éléments secrets du scénario — ne publier aucun indice ni contenu réservé à la partie secrète
- [ ] Créer la partie publique du site : photos animalières qui évoluent vers une enquête sur les êtres masqués
- [ ] Intégrer les photos de pièges photographiques dans le site

Note : le photographe a séjourné au gîte. Les joueurs peuvent découvrir quelle était sa chambre et y faire une fouille.

### Continuité / lore à trancher

- [ ] **Continuité de la randonnée** — `joueurs/rando/feuilles_rando.md` mentionne un squelette au Scialet Royer, mais le fugitif poursuit ensuite sa fuite (proposition : le squelette n'est pas le sien — victime collectée par le triangle, époque à choisir sans lieux de mémoire réels). Deux versions incompatibles du sac. Réécriture des feuilles une fois les points de lore tranchés.
- [ ] **Voix de la forêt** — elles manipulent le fugitif alors que le maléfice « n'a pas de volonté » : contradiction à trancher (options dans `lore/lore_precisions.md`)

### Logistique

- [ ] **Cartes physiques** — acheter l'IGN du secteur + reproductions de cartes anciennes (Cassini, état-major). OT fermé : mairie ou web
- [ ] **Plan de mise en place — qui place quoi, quand, où** (décision **vendredi 23/10**, une fois que tout existe : site, affiches, matériel). Décidé le 21/10 de ne pas répartir avant. À répartir ce jour-là : affiche déchirée et livre d'or modifié, étiquettes sur **toutes** les portes, pochette dans la chambre, tableau et affiche au café, les 7 props Rando (1 au gîte, 6 en terrain), la cache des masques et le parcours Sportif ; **la nuit** : miroirs, bols et céréales, vitres des voitures ; **dimanche** : échange de la statuette dorée, indice de secours à 10h25 si le groupe terrain bloque, signal de début et de fin de la foule ; plus les 8 tâches du rétroplanning (`design/retroplanning.md`) encore sans propriétaire
- [ ] **Dimanche : plan pluie** — la pluie est prévue (prévision du 21/10), la version « sous la pluie » du plan B (`joueurs/rituel/README.md` §5) est donc le scénario probable. À vérifier : ponchos pour ~35 personnes, supports plastifiés, masques et sachets de riz à l'abri, **peinture dorée à séchage rapide** et **fumigènes** utilisables sous la pluie, et le seuil de repli au gîte. Le plan B actuel suggère d'attendre une « trouée sèche » : cela laisse peu de marge avec une arrivée à 11h00 et une deadline à 11h30
- [ ] **Réduire le risque « Mareva indisponible »** (avis de Batiste, 21/10 : seul vrai risque individuel d'ici samedi) — masques, statuette ancienne et son message, sons et voix, chorégraphie reposent sur elle. Pistes à valider avec elle : terminer ses fabrications le plus tôt possible, partager dès maintenant le texte du message et les notes de chorégraphie (dans le repo ou ailleurs), copier sons et voix chez Batiste (montage en cours)
- [ ] **Matériel des manifestations** — encre invisible adaptée aux miroirs (douches en plastique), marqueurs craie effaçables pour les voitures (pas de givre attendu)
- [x] **Communication entre équipes** — sans objet : pas de communication le samedi (décidé 11/10)
- [ ] **Prop bouteilles** — bouteilles des parents apportées au gîte comme décor ; préparer le secret d'Ivan à y cacher (ex. dernière carte à superposer)
