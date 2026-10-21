Voici le recap façon PR — prêt à partager ou à paraphraser pour la team :

## Passe de cohérence (commits `bbfef9e` + `f39f3a2`, non pushés)

### Ce qu'on a fait

Audit complet du repo (et lecture croisée du site) selon `meta/methode_coherence.md` : 5 passes — hygiène des docs, table des invariants, plausibilité matérielle des props, graphe d'information heure par heure, synchro site. Résultat détaillé dans `meta/audit_coherence_2026-10-20.md`. Verdict : **aucune contradiction bloquante** dans le socle narratif ; l'essentiel était du doc rot dans les fichiers de synthèse.

### Corrigé — chronologie & mécanique du jeu

- **Samedi réécrit partout pareil** : lancement 14h (email de Camille + affiche déchirée, 100 % physique) → séparation des 3 arcs autonomes ~14h15–14h30 → regroupement ~17h30 + destruction de la statuette. Fini le vieux planning « fouille commune 14h–14h30 puis formation des groupes ».
- **Dimanche** : les 3 groupes s'appellent partout pareil — **terrain / statuette / danse** (fini « lieu / arts plastiques / rituel »).
- **Zone secrète du site** : ouverte **dès le samedi** via les 4 clés de la pochette (plus « jour 2 ») ; ses contenus ne prennent sens que dimanche.
- **Décisions du 11/10 propagées** : zéro communication entre équipes (géoguesser, talkies, « transmettre des infos aux équipes mobiles » rayés), pas de PNJ enfant d'Ivan, cimetière OK.
- **Voyante tranchée** : c'est un **document** (transcription dans la pochette), pas un acteur — casting PNJ rayé du retroplanning.
- **Chambre d'Ivan** : mécanisme acté = livre d'or 2011 + étiquette de la Chouette décollée sur la porte.

### Corrigé — plausibilité des props (le fun du détail)

- Le « carnet d'Ivan » est maintenant décrit comme une **pochette à élastiques de feuilles volantes** — son vrai carnet était sur lui dans la voiture la nuit de l'accident. Terminologie alignée partout où ça compte.
- La **coupure de presse** a été découpée et glissée dans la pochette **par les hôtes du gîte** en attendant Camille (résout l'anachronisme : elle ne pouvait pas être dans la sacoche avant sa mort). Post-it reformulé au passage.
- **Lettre de Marcellin : 1921 → 1931.** À 9 ans en 1886, il avait 44 ans en 1921 — trop jeune pour des « petits-enfants » ; à 54 en 1931, ça passe.
- **Relevés d'Ivan** : 2011 ne parle plus de « déclenchement » (pas d'enregistreur avant 2019, pas de pièges avant 2021) ; la remontée du 18 oct. 2025 est signalée comme exceptionnelle (il meurt avant sa veille du changement d'heure).
- **Almanach** : plus de « cadran solaire du bourg » (il n'en existe pas au village → risque de fausse piste), et « la brèche ouverte pour un siècle » → 140 ans, le vrai cycle.
- **Cartel du tableau** : « novembre 1886 » → « fin octobre 1886 » (colle à la Grande Veille).
- `assets/sources/perchtenlauf_loup.md` et `Hiboux` marqués « document source » (la version joueur est `joueurs/slow/pochette/07_annexes_1894_1944.md`) + coquilles corrigées (« Rpport », « desgrands »).

### Corrigé — docs de suivi

- `AGENTS.md` : Ivan « meurt dans un accident », ne « disparaît » plus — un joueur aurait pu croire qu'il se cachait.
- `questions.md` : renuméroté (deux fois « 14 »), 3 questions résolues — **Camille** (prénom épicène choisi), Ivan **né ~1952** (73 ans dans l'article), accident **nuit du 18–19 oct. 2025**.
- `README`, `TODO`, `retroplanning` : inventaires et statuts à jour (`joueurs/slow/pochette/`, `joueurs/slow/props/`, mot du tableau = `VEILLE` acté).

### Pas touché volontairement

- **Les arcs de Seb et Rémi** : rien de tranché à leur place — uniquement balisé `<a_confirmer>` et listé en questions.
- **Le site** : 5 petits fixes identifiés mais non appliqués → PR à part (règle : jamais de push direct sur `main`).
- `archive/`, `validation_*`, `tools/` : figés par principe.

### Reste ouvert — à trancher avec la team (17 points dans l'audit)

Les principaux : **date du fugitif** 1746 vs 1886 (1746 recommandé — mais le site code déjà « vers 1746 »), **la statuette « dans ma gourde »** (trop grande — « à côté de » ou « baluchon »), **destruction physique vs « rituel de purification »**, « réservations closes » sur le site vs formulaire actif, « quinze/vingt ans » et « trois nuits » sur le site, apparitions 1894/1944 = patrouilles ordinaires (« ils veillent » — le mot caché du tableau).