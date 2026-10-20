# Méthode d'audit et de mise en cohérence du projet `70ans`

Ce document définit **comment** auditer méthodiquement l'ensemble du dépôt `70ans` (et son jumeau `ivan-beaulieu-photos`) pour débusquer et corriger toute contradiction avant push/production.

---

## 1. Pourquoi les incohérences apparaissent dans notre repo (Diagnostic)

Le projet a évolué par couches successives depuis début octobre (`excalidraw` → `archived/` → `lore.md` → `rituel/` → `enigmes.md` → `documents_ivan/` + `props_slow/` + site web). Les contradictions viennent de **4 mécanismes précis** :
1. **Sédimentation (doc rot)** : une décision récente (`validation_2026-10-11.md` ou `validation_2026-10-19.md`) est prise, mais les fichiers plus anciens (`lore.md`, `AGENTS.md`, `Rituel.md` à la racine) gardent l'ancienne version.
2. **Redondance sans source de vérité unique** : un même fait (ex. qui trouve les costumes, à quelle heure on fouille le gîte, quand s'ouvre la zone secrète du site) est raconté dans 4 fichiers différents.
3. **Collisions inter-équipes** : ce que vit l'équipe Slow (Batiste), l'équipe Sportive (Seb), l'équipe Rando (Rémi) et le groupe du Dimanche (Mareva) partage des objets (statuette, masques, cartes, pièges photo) dont les mains changent.
4. **Anachronismes matériels / diégétiques** : un objet physique contient une information qu'il ne pouvait matériellement pas contenir au moment où son auteur l'a posé (ex. l'article de la mort d'Ivan dans une sacoche oubliée la veille de sa mort, ou une photo de piège datée de mai 2026 après son décès).

---

## 2. Hiérarchie des sources de vérité (Qui gagne en cas de conflit ?)

Avant de corriger quoi que ce soit, il faut une règle d'arbitrage claire. Lorsqu'un fichier A contredit un fichier B :

| Niveau d'autorité | Fichiers | Règle en cas de conflit |
|---|---|---|
| **Niveau 1 — Décisions datées les plus récentes** | `validation_2026-10-19.md` > `validation_2026-10-11.md` > `validation_2026-10-02.md` | **Gagne toujours.** C'est le journal des décisions validées. |
| **Niveau 2 — Spécifications opérationnelles actives** | • Samedi & parcours : `enigmes.md`, `deroule.md`<br>• Dimanche : dossier `rituel/` (`README.md`, `partition_et_sons.md`, `enigmes_dimanche.md`, `checklist_production.md`)<br>• Terrain : `reperage.md` | **Fait foi sur sa spécialité.** Doit être aligné sur le Niveau 1. |
| **Niveau 3 — Textes et supports joueurs (« in-universe »)** | • Slow : `documents_ivan/*`, `props_slow/*`<br>• Rando : `feuilles_rando.md`<br>• Brut Ivan : `ivan/ivanbio.md`, `ivan/Perchtenlauf *`<br>• Site web : `ivan-beaulieu-photos/src/*` | **Critique : zéro erreur permise** (c'est ce que les joueurs lisent). Doit être 100 % compatible avec les Niveaux 1 et 2. |
| **Niveau 4 — Synthèses de référence et suivi** | `lore.md`, `lore_precisions.md`, `timeline_lore.md`, `timeline_rando.md`, `TODO.md`, `retroplanning.md`, `questions.md`, `AGENTS.md`, `README.md` | **Doit refléter les Niveaux 1–3.** C'est souvent ici que se cachent les vieilles phrases périmées. |
| **Niveau 5 — Archives figées (hors périmètre de correction)** | `archived/*`, `code/output/excalidraw*.md`, et potentiellement `Rituel.md` (racine, remplacé par `rituel/`) | **Ne pas modifier** (archives historiques), mais vérifier qu'aucun doc actif ne les cite comme source à jour — ou supprimer/archiver les doublons obsolètes comme `Rituel.md` racine. |

*Règle de protection Seb / Rémi* : tout conflit touchant le contenu interne de l'arc de Seb ou de Rémi n'est **pas tranché unilatéralement** ; il est isolé dans `questions.md` et balisé `<a_confirmer>`.

---

## 3. Les 5 passes complémentaires de la méthode

Aucune passe unique ne trouve tout : un `grep` trouve les dates contradictoires mais rate un anachronisme matériel ; une lecture narrative trouve les trous logiques mais rate un nom de fichier cassé. Je propose **5 passes courtes et orthogonales**.

### Passe 1 — Audit d'architecture documentaire & doublons (« Hygiène du repo »)
- **Objectif** : éliminer les faux jumeaux et vérifier les liens entre fichiers.
- **Vérifications concrètes** :
  1. Identifier les fichiers totalement supplantés (ex. `Rituel.md` à la racine vs le dossier `rituel/` ; `ivan/Perchtenlauf *` vs `documents_ivan/07_annexes_1894_1944.md`). Décider si on les déplace dans `archived/` ou si on met un bandeau en tête.
  2. Vérifier le principe **Single Source of Truth** : chaque information ne doit être détaillée qu'à un seul endroit, les autres fichiers faisant un renvoi explicite.
  3. Vérifier que tous les chemins de fichiers mentionnés dans les `.md` existent réellement.

### Passe 2 — Extraction et croisement de la « Table des Invariants Factuels » (Approche matricielle + `grep`)
- **Objectif** : s'assurer qu'une même entité a **exactement** la même valeur partout (docs + props + site web).
- **Méthode** : construire une table de ~20 invariants canoniques et lancer un `grep` systématique sur les deux repos (`70ans` et `ivan-beaulieu-photos`) pour vérifier chaque occurrence :
  - **Identités & contacts** : nom (*Ivan Beaulieu*, plus aucun *Dequene*), âge au décès (73 ans / né vers 1952), métier (ancien ingénieur CNRS + AMM + photographe), village du chalet (*Villard-de-Lans*), email (`ivanbeaulieu2@orange.fr`), prénom de l'enfant (*Camille*), nom du notable (*Anselme Giraud*), nom du médecin (*Dr Henri Brilleux*), auteur de la lettre (*Marcellin V.*), nom de la voyante (*Mme Solange*).
  - **Dates historiques & cycles** : durée du cycle (**140 ans**), jalons des cycles (**1606 — 1746 — 1886 — 2026**), date du procès (**1466**), date de la lettre de l'enfant (**souvenir d'oct. 1886, écrite en nov. 1931**), date de l'article du Loup (**12 nov. 1894**), date de la radio allemande (**17 fév. 1944**), premier séjour d'Ivan au gîte (**octobre 2011**), date de la conférence (**vendredi 17 octobre 2025, 19h**), date du décès d'Ivan (**nuit du samedi 18 au dimanche 19 octobre 2025**), date du jeu (**24–25 octobre 2026**).
  - **Constantes numériques & codes** : les 3 horodatages (**`00:03` / `06:12` / `18:47`**), les 4 clés du gate `/archives` (**année fontaine / `VEILLE` / tombe sans inscription / `Barbe de bouc`**), l'heure limite du dimanche (**11h30**), les 3 animaux (**Chouette / Bouquetin / Loup**).
  - **Règles de gameplay validées** : zéro communication inter-équipes le samedi (plus de trace de *Geoguessr* ou *talkie-walkie*), pas de PNJ enfant d'Ivan (remplacé par email imprimé + pochette), pas de fumigènes pyrotechniques (remplacés par poudre/produits safe orange/vert + statuette dorée), noms des 3 groupes du dimanche (*terrain / statuette / danse*).

### Passe 3 — Audit de plausibilité matérielle et causale (« Physique des objets »)
- **Objectif** : prendre chaque objet physique ou numérique que les joueurs auront en main et lui poser 4 questions :
  1. **Qui l'a créé dans la fiction, et à quelle date ?**
  2. **Où a-t-il été stocké depuis cette date jusqu'au samedi 24 oct. 2026 à 14h ?**
  3. **Contient-il une info postérieure à sa date de création ou de dépôt ?** *(Ex. le bug qu'on vient de corriger sur l'article de presse, ou la date `05/21/2026` incrustée sur la photo WhatsApp de la fouine/renard dans `ivan/` alors qu'Ivan est mort en octobre 2025 !)*
  4. **Son support matériel est-il crédible ?** *(Ex. feuilles perforées en vrac plutôt que carnet relié aux 3/4 vide ; affiche jaunie déchirée au gîte vs intacte sous cadre au café ; texte du fugitif de 1746 qui ne doit pas parler d'« heure d'hiver » moderne).*

### Passe 4 — Simulation chronologique du graphe d'information joueur (« Zéro dépendance circulaire, zéro impasse »)
- **Objectif** : parcourir heure par heure (de samedi 14h00 à dimanche 11h30) ce que chaque équipe **sait** et **possède** à l'instant $t$.
- **Vérifications concrètes** :
  1. **Préconditions d'énigme** : chaque fois qu'une étape demande un outil ou une info (ex. avoir la loupe au café à 15h30, connaître l'existence de la tombe du notable avant d'aller au cimetière, avoir l'URL avant d'ouvrir le site à 16h15), vérifier que l'objet a été obtenu à une étape $t' < t$ par **la même équipe**.
  2. **Étanchéité entre les 3 équipes du samedi** : vérifier qu'aucune énigme de l'équipe Slow ne dépend d'une info détenue par Seb ou Rémi avant 17h30 (et inversement).
  3. **Audit du double sens (Samedi vs Dimanche)** :
     - *Samedi 17h30* : les indices trouvés par les 3 équipes suffisent-ils à les convaincre de **détruire la statuette** sans que l'animateur ait à forcer la décision ?
     - *Dimanche 10h00* : une fois le message intérieur de la statuette lu et les manifestations nocturnes découvertes, les joueurs ont-ils **toutes** les briques pour reconstruire la statuette, trouver le champ du rituel (superposition des cartes) et exécuter la danse des 3 animaux avant 11h30 ?

### Passe 5 — Synchronisation inter-dépôts (`70ans` ↔ `ivan-beaulieu-photos`)
- **Objectif** : aligner le code du site web (`ivan-beaulieu-photos/src/`) avec les textes de `documents_ivan/` et `props_slow/`.
- **Vérifications concrètes** :
  - Les dates, titres et extraits de la conférence et du journal sur le site correspondent-ils au mot près à l'affiche (`slow_02`) et aux notes d'Ivan (`01`) ?
  - Les libellés des 4 questions sur la page `/archives` correspondent-ils exactement à l'aide-mémoire de la pochette d'Ivan (`01`) ?
  - Les relevés de disparitions et d'enregistrements sur `/archives/disparitions` et `/archives/audio` sont-ils alignés avec le procès (1466), le fugitif (1746), la lettre de l'enfant (1886), l'article du loup (1894) et le rapport allemand (1944) ?

---

## 4. Protocole d'exécution et livrable de l'audit

Si tu valides cette méthode, voici comment je déroulerai l'application :

1. **Étape A — Exécution des 5 passes en lecture seule** et génération d'un rapport structuré (ou mise à jour directe de la section `## Incohérences connues` de `TODO.md`) classant chaque anomalie trouvée en deux catégories :
   - 🟢 **Correction mécanique évidente** (ex. une vieille phrase dans `lore.md` ou `AGENTS.md` qui contredit une décision `✅` déjà actée dans `validation_2026-10-11.md` ou `19.md`).
   - 🟠 **Arbitrage de design ou question équipe** (ex. `1746` vs `1886` pour le fugitif de Rémi, ou la date `2026` sur la photo de piège photo de Seb) → je ne tranche pas seul, je te propose l'arbitrage ou je l'ajoute à `questions.md`.
2. **Étape B — Application chirurgicale des corrections 🟢** dans `70ans` (et proposition de PR séparée si retouche texte dans `ivan-beaulieu-photos`), suivie d'un `grep` de vérification finale prouvant qu'il ne reste plus aucune occurrence des termes obsolètes.
