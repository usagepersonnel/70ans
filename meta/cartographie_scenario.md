# Cartographie structurelle du scénario

Date : 21/10/2026 (J-3), mis à jour le jour même après les retours de Batiste (les points concernés sont marqués « résolu », « tranché » ou « décidé le 21/10 »). Objet : repérer les problèmes qui font échouer le jeu en conditions réelles, pas les contradictions de détail. Ce document est une carte vue sous plusieurs angles ; il ne tranche rien à la place des auteurs.

## 0. Méthode et limites

**Sources lues** : `design/`, `lore/`, `joueurs/`, `decisions/validation_2026-10-19.md`, et dans le repo du site `ivan-beaulieu-photos` : `SPEC.md`, `src/lib/keys.ts`, `src/lib/auth.ts`, `src/pages/archives/`. Les autres fichiers de `meta/` n'ont volontairement pas été ouverts (regard neuf). Transparence : je gardais en tête quelques résultats de la passe précédente (via la conversation) ; chaque constat ci-dessous a été revérifié dans les textes sources.

**Étiquettes de fiabilité** :
- **[Lu]** constaté dans un texte précis, cité.
- **[Déduit]** conséquence logique de plusieurs [Lu], à confirmer.
- **[À vérifier]** je ne peux pas le savoir depuis le repo (terrain, objets réels, intentions non écrites).

**Gravité** : BLOQUANT (le jeu ne peut pas se dérouler comme prévu) · MAJEUR (une équipe est coincée ou l'effet est perdu) · MOYEN (dégradation) · MINEUR.

**Ce que ce rapport ne peut pas faire** : jouer le jeu. Marcher le parcours, chronométrer une lecture et faire lire les props à quelqu'un d'extérieur restent des tests humains (cf. §9).

---

## 1. Le modèle : qui fait quoi, avec quoi, produit quoi

Statut documentaire : **OK** (écrit, exploitable) · **PARTIEL** · **ABSENT**.

### Samedi

| ID | Qui | Heure | Il faut | Ça produit | Doc |
|---|---|---|---|---|---|
| S0 | Tous (~35) | 14h00 | Email imprimé (`joueurs/slow/props/01_lancement_email_enfant.md`), lu à voix haute par un orga ; affiche déchirée au mur | Savoir : Ivan est mort, gîte depuis 2011, 3 parcours, existence d'un site (sans URL) | OK |
| S1 | Tous | 14h00-14h30 | Les « trois dossiers de parcours » promis par l'email | Formation des 3 équipes par auto-sélection | **ABSENT** (cf. G-3) |
| B1 | Slow | 14h30 | Livre d'or 2011 + feuillet glissé + étiquettes sur les portes (`joueurs/slow/props/03_livre_dor_2011_chambre.md`) | Savoir : quelle chambre | OK (dépend d'une photo à prendre vendredi) |
| B2 | Slow | 14h45 | Pochette sous un lit (`joueurs/slow/pochette/`) | 7 pièces, loupe, calendrier, aide-mémoire des 4 clés, « il faut la briser » (voyante) | OK |
| B3 | Slow | 15h15-16h15 | Affiche intacte (URL), tableau + loupe, fontaine, tombe, plante | URL + 4 réponses | PARTIEL (cf. G-1, G-4) |
| B4 | Slow | 16h15-17h15 | Site (réseau du gîte) + 4 clés ; calendrier | Accès `/archives` ; échéance 11h30 | PARTIEL (cf. §6) |
| A1-A7 | Rando | 14h15-17h30 | 7 props (1 au gîte, 6 en terrain ; détail §2) | Statuette + carte de Cassini | PARTIEL (cf. §2) |
| C0-Cfin | Sportif | 14h15-17h30 | Photos de pièges d'Ivan, énigmes animaux | Tenues, masques, cailloux peints | **ABSENT** sauf le produit final |
| D1 | Tous | ~17h30 | Statuette (Rando), masques (Sportif), dossier (Slow) | Mise en commun | PARTIEL |
| D2 | Tous | 17h30-18h | Acte de destruction (qui, comment, avec quoi) | Message au « je » découvert dans la statuette | **ABSENT** (cf. §5) |

### Nuit et dimanche

| ID | Qui | Heure | Il faut | Ça produit | Doc |
|---|---|---|---|---|---|
| N1 | Un orga | nuit sam → dim | Miroirs (marqueur), papiers sous 3 bols et dans des céréales, vitres des voitures | Amorce des 3 groupes | PARTIEL (qui, quand ? cf. G-6) |
| D-1 | Tous | 9h30-10h | Lecture du message, constitution de 3 groupes, désignation de 3 masqués | Groupes terrain / statuette / danse | PARTIEL (tailles, règle de casting) |
| D-2 | Terrain | 10h00-10h30 | Cartes à superposer, énigme du lieu | Position du champ | **ABSENT** (cf. G-9) |
| D-3 | Statuette | 10h00-10h45 | 8 éléments, pictogrammes des miroirs, matériel pré-stagé | Nouvelle statuette | OK (`joueurs/rituel/enigmes_dimanche.md`) |
| D-4 | Danse | 10h00-10h45 | 3 clips audio, 3 photos horodatées, 12 objets sonores | Chorégraphie apprise | PARTIEL (12 sons non choisis) |
| D-5 | Tous | 10h45-11h30 | Environ 8 voitures (estimation : 35 personnes), 10 min de route, rituel 6-10 min, fumigènes, statuette dorée | Fin du jeu avant 12h | OK sur le papier, aucune marge |

---

## 2. La chaîne de l'équipe Rando (A1-A7)

Chaque prop contient le texte d'une étape et doit permettre de trouver le lieu suivant. Je vérifie ce lien pour chaque étape, sur `joueurs/rando/feuilles_rando.md` et `design/enigmes.md` §A.

| Étape | Prop | Le texte joueur désigne-t-il le lieu suivant ? | Statut |
|---|---|---|---|
| A1 Gîte | Bambou (n'existe pas) | Vers le Col de Carri : **aucun localisateur**. Le texte ne nomme pas le col ; seule indication directionnelle : « la montagne au Sud ». Il n'a pas de bloc « Indices du lieu » | **ABSENT** |
| A2 Col de Carri | Gourde cirée | Vers le Scialet Royer : le texte dit « scialets jumeaux » ; l'indice « Royer = aérer la terre en creusant des sillons » n'existe que dans une **note de conception**, il n'est dans aucune phrase du fugitif | PARTIEL |
| A3 Scialet Royer | Crâne en résine | Vers le Refuge de Crobache : le texte dit « la cabane » ; la note de lieu parle du sac, pas de la localisation | PARTIEL |
| A4 Refuge | Sacoche + livre + cryptex | Vers la Plaine de Fauchier : « les faucheurs ont fait leur œuvre » | OK |
| A5 Fauchier | Code du cryptex → page + Cassini | Vers le Belvédère : « trouée dans la forêt, surplombe la route » ; **le code du cryptex n'est défini nulle part** | PARTIEL |
| A6 Belvédère | Corne à poudre + gourde | Vers la Grotte des Ferrières : la note dit « Voir description Ferrière pour compléter » ; **cette description n'existe pas** | **ABSENT** |
| A7 Grotte | Statuette | — | Lieu réel non documenté |

**Autres constats sur cette chaîne** :
- **[Lu]** La grotte réelle du lore est à ~23 km à vol d'oiseau (`lore/lore.md`, section « Lieux ») ; la case « repérer les grottes et scialets visitables autour du village » de `design/reperage.md` n'est pas cochée. Aucun document ne dit où se trouve A7.
- **[Lu]** `design/reperage.md` : « Faire le trajet gîte → Col de Carri » et « Vérifier que le texte colle au terrain » ne sont pas cochés. Aucune distance, durée ni dénivelé du parcours Rando dans le repo (grep : aucune occurrence pour la Rando).
- **[Lu]** Aucune carte n'est donnée à l'équipe Rando le samedi. L'achat de l'IGN est prévu pour la superposition du dimanche (`design/reperage.md`, « Production »). Les indices de lieu sont des étymologies (Royer, Fauchier), qui supposent une carte.
- **[Lu]** 4 feuilles sur 6 ont une version « adaptée à l'époque (à régénérer) » ; les deux versions divergent sur des faits (A3→A4 : le fugitif retourne à la cabane et abandonne son sac, ou ses fidèles l'ont devancé). Aucune version n'est désignée comme définitive.
- **[Lu]** Le dernier message (A1) dit que le fugitif cache la statuette « à côté de la source, dans sa gourde ». **Précisé par Batiste le 21/10 : c'est une source en montagne, que Rémi connaît ; ce n'est pas la fontaine du village.** (Ma première lecture, qui supposait la fontaine, était fausse, et `design/reperage.md` le laissait entendre : corrigé.) **[À vérifier]** Aucun document ne localise cette source ni ne dit si elle aide les joueurs à trouver le Col de Carri (`questions.md` #18).

---

## 3. Contrôles sur le graphe d'information

### 3.1 Entrées consommées sans producteur documenté

| # | Entrée | Qui la consomme | Constat |
|---|---|---|---|
| G-1 | **Année gravée sur la fontaine** (clé 1) | Slow, pour ouvrir le site | **Résolu le 21/10** : dates gravées « 1894-1994 » (Batiste), statues d'ours de ~1,5 m. Reste à régler `KEY_FOUNTAIN` sur Vercel et à redéployer : le défaut du code (`1878`, `ivan-beaulieu-photos/src/lib/keys.ts`) est faux (`TODO.md`). **MAJEUR** tant que ce n'est pas fait |
| G-2 | Texte du message dans la statuette | Tout le jeu (le retournement) | **[Lu]** « Reste : le message dans la statuette (Mareva) », `design/retroplanning.md` ; `questions.md` n°19 |
| G-3 | Contenu des « trois dossiers de parcours » | Les 3 équipes à 14h15 | **[Lu]** L'email les dit « déposés » ; `design/enigmes.md` §0 les décrit comme photocopies des « dernières notes d'Ivan ». Aucun contenu écrit pour aucun des trois, pas même celui de Slow |
| G-4 | Image du tableau du chasseur (mot `VEILLE` en corps 4-5 pt) | Slow, clé 2 | **[Lu]** « créer l'image du tableau » non coché (`TODO.md`, `design/retroplanning.md`) |
| G-5 | Navigation Rando et Sportif | Ces deux équipes | Voir §2 : aucune carte ni parcours chiffré |
| G-6 | Qui prépare quoi, quand | Tous | Voir §4 |
| G-7 | Les 12 sons → 3 clips → page audio du site | Groupe danse | **[Lu]** table des 12 sons vide (`joueurs/rituel/partition_et_sons.md` §2) ; `SPEC.md` : audio = « Placeholder WAV » ; les enregistrements bruts existent localement (Mareva). **Montage en cours (Batiste, 21/10).** La table des 12 sons du document reste à renseigner |
| G-8 | 3 photos de pièges horodatées | Groupe danse (`00:03`, `06:12`, `18:47`) | **[Lu]** `SPEC.md` « À shooter » ; la page affiche `[tirage en cours de numérisation]` (`src/pages/archives/pieges.astro`) |
| G-9 | Énigme du lieu du champ (superposition de cartes) | Groupe terrain, qui doit partir à 10h30 | **[Lu]** « Énigme du lieu réalisée par Rémi (ok) » (`joueurs/rituel/README.md`) mais aucun document ne la décrit ; `lore/lore.md` dit « chaque groupe revient avec une carte d'une époque différente », alors que la table de convergence (`design/enigmes.md` §D) ne mentionne qu'une carte (Cassini, Rando) ; 3 des 4 cartes n'ont pas de source ; « les trous dans les cartes » reste ❓. **Rémi y travaille (Batiste, 21/10)** |
| G-10 | Amorce de l'équipe Sportif ; indice « détruire » | Sportif | Voir §5 |

### 3.2 Sorties sans consommateur scripté (les « aha » qui ne se déclenchent pas)

| Élément | Où il est planté | Ce qui est censé le payer | Le payer est-il prévu au déroulé ? |
|---|---|---|---|
| `VEILLE` / « ils veillent » | tableau (`joueurs/slow/props/04_tableau_chasseur_et_loupe.md`) | « Relecture du dimanche » | **Non** : aucun beat de `joueurs/rituel/` n'y renvoie (grep) |
| Étiquette Chouette → « Slow = Chouette » | livre d'or, pochette | Casting dimanche | **Non** : le casting est « 3 volontaires désignés au petit-déj », sans règle d'équipe |
| « Trois piétons » + coup de volant | coupure de presse (`joueurs/slow/pochette/06_coupure_presse_accident.md`) | Compréhension qu'Ivan a évité les masqués | Seulement si le message de la statuette (G-2) le dit |
| Cailloux peints | Seb (21/10) | **Inconnu** | Non. Hypothèse **[À vérifier]** : ce sont les 3 pierres de départ (Chouette N, Bouquetin SO, Loup SE), aujourd'hui « ramassées sur place » |
| Échéance 11h30 | calendrier (pochette, Slow seul) | Deadline du rituel | Aucun beat écrit ne la transmet aux deux autres équipes |
| Bouteilles des parents | décor gîte | Dernière carte à superposer | « Plutôt dimanche », non tranché |

---

## 4. Points de défaillance : que se passe-t-il si ça rate ?

| Élément | Si ça rate | Repli documenté | Gravité |
|---|---|---|---|
| Variables d'environnement du site (clé 1 : le défaut `1878` est faux) | Slow ne peut pas ouvrir le site ; sa récompense du samedi disparaît | Aucun. Le gate accepte les champs partiels, mais une clé fausse reste bloquante | MAJEUR tant que `KEY_FOUNTAIN` n'est pas réglée |
| Slow ne trouve pas la chambre ou la pochette | Plus de loupe, de clés, de calendrier, de voyante : toute l'équipe est à l'arrêt | Double piste (fenêtre + étiquette) ; aucun « coup de pouce » orga prévu | MAJEUR |
| Réseau au gîte à 16h15 | Pas de site | **Risque accepté (21/10).** Au pire : demander le wifi au personnel du gîte, ou aller au café-librairie. Pas de copie hors-ligne prévue pour le samedi (le secours hors-ligne ne concerne que le dimanche, `joueurs/rituel/enigmes_dimanche.md` §4). **[Lu]** `design/reperage.md` : couverture « faible et inconstante » | MOYEN |
| Rando en retard ou chaîne coupée | Pas de statuette : pas de destruction à 17h30 | Référent d'équipe (Rémi) comme filet de sécurité (décision du 21/10) ; heure limite et aide possible à cadrer vendredi | MOYEN |
| Sportif ne trouve pas la cache | Pas de masques : pas de danse dimanche (les masques de Mareva n'existent qu'en un exemplaire) | Référent d'équipe (Seb), même règle | MOYEN |
| Pluie samedi | Papier en forêt ; parcours longs | **Prévision du 21/10 : pas de pluie, ~8°C**, donc risque faible. Reste le froid (lire et manipuler dehors). Le « Plan B météo » du rétroplanning n'a pas de propriétaire (`design/retroplanning.md`), utile seulement si la prévision change | MINEUR |
| Pluie dimanche | Rituel en extérieur | **Prévision du 21/10 : pluie dimanche**, donc le plan B est le scénario probable, pas l'exception. Plan B écrit : version courte sous la pluie, ou repli au gîte ; mais il suggère d'attendre une « trouée sèche entre 10h30 et 11h30 » alors que l'arrivée est à 11h00 et la deadline à 11h30 : **[Déduit]** aucune marge pour attendre. Point à vérifier : la peinture dorée (séchage) et les fumigènes sous la pluie (`TODO.md`) | MOYEN |
| Un orga indisponible | 3 gestes critiques lui sont attribués : échange de la statuette dorée, indice de secours à 10h25, signal de début/fin | Les orgas sont aussi guides, danseurs ou participants ; aucun rôle assigné (à répartir vendredi) | MAJEUR |
| Mareva indisponible | Seul vrai risque individuel (avis de Batiste, 21/10) : masques, statuette ancienne et son message, sons et voix, chorégraphie reposent sur elle | Aucun écrit. Pistes dans `TODO.md` : finir ses fabrications tôt, partager le texte du message et les notes de chorégraphie, copier sons et voix chez Batiste (montage en cours) | MAJEUR |
| Batiste, Seb ou Rémi indisponible | Chacun a un rôle de référent d'équipe | Aucun | MINEUR (jugé peu probable d'ici samedi, 21/10) |

**Régie** : **[Lu]** il n'existe aucun plan de mise en place. Seules mentions : « photo prise le vendredi soir en arrivant » et « matériel pré-stagé ». Il faut pourtant placer, avant 14h00 le samedi : l'affiche déchirée, le livre d'or modifié, les étiquettes sur toutes les portes, la pochette, les 7 props Rando (dont 6 en terrain), la cache des masques et le parcours Sportif, le tableau et l'affiche au café ; et la nuit, les miroirs, les bols et les vitres. **[Lu]** `design/retroplanning.md` : sur 21 tâches, **8 n'ont pas de propriétaire** (`?`). Le dry-run est la dernière ligne, au 23/10. **Décidé le 21/10** : la répartition « qui place quoi » se fera vendredi 23/10, une fois que tout existe (`TODO.md`).

---

## 5. Motivation et logique du retournement

### 5.1 Pourquoi chaque équipe veut-elle détruire la statuette ?

| Équipe | Objectif énoncé à 14h15 | Raison de vouloir détruire | Statut |
|---|---|---|---|
| Slow | « Marcher sur les pas d'Ivan », retrouver ses affaires | Voyante (« il faut la briser… c'est écrit dedans ») + synthèse d'Ivan (« la mettre hors d'état de nuire ») | OK |
| Rando | Remonter la piste d'un fugitif | Le fugitif l'exige explicitement | OK, avec la réserve ci-dessous |
| Sportif | **Aucun énoncé** | **Aucune** | **ABSENT**, en attente de la réponse de Seb (annoncée le 21/10) |

**[Lu]** Le seul levier mécanique côté Sportif est « les masques sont nécessaires au rituel » (Rando, A2). Il n'est pas écrit comment ce « verrou » s'exerce à 17h30.

### 5.2 L'acte de destruction est le moment le moins spécifié du jeu

Contradictions **[Lu]** :
- `design/enigmes.md` A3 : « il faut un rituel de purification pour la détruire (canon : la statuette ne se brise pas à coups de marteau) ».
- `joueurs/rituel/checklist_production.md` : « statuette ancienne en terre (samedi, à briser) ».
- `design/deroule.md` : le verrou « nécessite les objets/conditions préparés par l'équipe sportive (à concevoir) ».
- `joueurs/slow/pochette/05_transcription_voyante.md` : « il faut la briser en morceaux ».

Questions sans réponse écrite : qui brise, avec quoi, où, devant qui, avec quel masque, et ce que la destruction doit représenter pour les joueurs (« j'ai commis une erreur » ou « j'ai libéré un secret »).

**Piste du 21/10** (mémoire de Batiste, **à confirmer avec la team**, `questions.md` #20) : un rituel assez sommaire avec les 3 masques + la statuette, sans marteau. Elle réconcilie les trois premiers points ci-dessus (« rituel de purification », « statuette à briser », masques ramenés par Seb).

### 5.3 Ivan est-il convaincu ou en train de douter ?

**Tranché le 21/10 (Batiste) : Ivan ne doute jamais, il est persuadé qu'ils sont maléfiques.** Enregistré dans `lore/lore_precisions.md`.
- **[Lu]** La pochette est cohérente avec cela (feuillet de synthèse, pièce 1 : « il faudra trouver cet objet et le mettre hors d'état de nuire »).
- **[Lu]** Un seul passage contredit cette certitude : `src/pages/archives/dossier.astro`, accessible dès le samedi (« je commence à me demander si ce n'est pas autre chose »). Il entame l'effet du retournement. Correction prévue dans la PR du site, texte proposé dans `TODO.md`.

### 5.4 La fenêtre entre 18h00 samedi et 10h00 dimanche

- **[Lu]** La zone secrète du site est accessible dès le samedi, avec le `carnet d'écoute` qui dit : « toujours quatre sons, puis quatre secondes de silence, comme s'ils attendaient qu'une foule leur réponde » (`joueurs/rituel/enigmes_dimanche.md` §4).
- **[Lu]** Après le retournement de 18h00, les joueurs savent qu'ils doivent faire le rituel à la place des masqués (`design/deroule.md`) ; l'équipe Slow connaît déjà la deadline de 11h30.
- **[Déduit]** Conséquence : dès le samedi soir, l'équipe Slow a déjà les clips audio et cette note. Elle peut donc résoudre le décodage du groupe danse **avant** le dimanche matin, alors que ce décodage est prévu pour les 10h00-10h45 de tout le monde. Ce n'est pas un défaut en soi : c'est un effet de la décision « accès total dès le samedi » (19/10), dont ce point n'avait pas été examiné. Trois façons de le traiter : l'accepter (Slow aide les autres le dimanche), verrouiller l'audio jusqu'au dimanche matin, ou donner au groupe danse une difficulté différente. **Accepté le 21/10 (Batiste)** : pas de verrouillage ; ils auront tous les éléments mais ne trouveront pas forcément cela intéressant, et au pire ils écouteront en se disant « c'est nul ».
- **[Lu]** Quand Slow ouvre le site, le navigateur garde un jeton « connecté » pendant 4 h seulement (`src/lib/auth.ts`, `COOKIE_MAX_AGE = 4 * 60 * 60`). Ouvert vers 16h30, il expire vers 20h30. Le dimanche à 10h00, il faut donc ressaisir les 4 clés sur l'appareil utilisé (elles sont dans la pochette), ou utiliser la copie locale de Batiste, déjà prévue. Détail sans importance (Batiste, 21/10) : tant que les clés ne changent pas, ils peuvent les ressaisir ; on peut aussi porter la durée du cookie à 48 h dans la PR du site (optionnel, c'est un site de jeu). J'avais écrit trop vite que le dimanche « reposait » sur l'ordinateur de Batiste.
- **[À vérifier]** Aucun document ne décrit la soirée du samedi (dîner, temps libre).

---

## 6. Récompense réelle de la zone secrète pour l'équipe Slow

**[Lu]** `design/enigmes.md` B4 présente l'ouverture de la zone secrète comme le sommet de l'après-midi de Slow (« zone secrète ouverte + échéance de 11h30 connue → conviction : il faut détruire la statuette »). Mais :
- l'échéance de 11h30 vient du calendrier (dans la pochette), pas du site ;
- la conviction de détruire vient de la pochette (voyante, synthèse d'Ivan), pas du site ;
- ce que le site contient a été voulu « inexploitable » avant dimanche (`decisions/validation_2026-10-19.md` n°13) : clips audio, photos horodatées ; deux pages (« relevés de disparitions », « journal d'Ivan ») sont encore « à écrire » (`SPEC.md`).

**[Déduit]** Après une heure à chercher les 4 clés, l'équipe ouvre un site dont elle ne peut rien faire sur le moment : risque de déception (« tout ça pour ça »). Ce n'est pas une erreur de conception, c'est l'effet de deux décisions qui se cumulent : la récompense arrive à la fin de la quête, et son contenu est volontairement opaque. Piste : mettre dès le samedi une pièce lisible et marquante dans la zone, par exemple l'un des deux textes encore « à écrire ». **Risque assumé le 21/10** (Batiste : « au pire ils vont écouter et se dire c'est nul »). La pièce marquante dès le samedi reste une option facultative.

---

## 7. Registre graines et dénouements

| Graine | Dénouement | Écrit ? |
|---|---|---|
| L'être cornu « frappe deux fois du pied puis lève les bras » (lettre de 1931) | Geste de la danse (pied D, pied G, bras D, bras G) | Oui, dans une note de conception ; bonus facultatif |
| « C'est écrit dedans » (voyante) | Message dans la statuette | Oui |
| « Les masques sont essentiels » (fugitif) | Les 3 masqués dansent | Oui |
| Statuette « d'un seul bloc, rien ne la liait » | Le fil manquant | Oui |
| Tableau : statuette sur un rocher avec figure masquée et loups | Reconnaissance du prop à 17h30 | **[À vérifier]** : l'image du tableau et la statuette de Mareva doivent se ressembler ; aucun des deux n'est fini |
| Échéance 11h30 | Deadline du rituel | Oui |
| `VEILLE`, Chouette = Slow, « trois piétons » | Voir §3.2 | Non |
| Poids de la statuette | **Correction de ma part** : les textes ne se contredisent pas. Marcellin (1886, de loin, sans la toucher) dit qu'elle « semblait lourde comme du plomb » ; le fugitif (1746, en main) dit « elle semble lourde, mais elle est en fait très légère ». Le vrai écart est avec le prop en terre. Résolu le 21/10 par une description canonique : creuse, donc légère (`lore/lore.md`) | Oui ; reste la fabrication (Mareva, `questions.md` #19) |
| Voix de la forêt (fugitif) | Question ouverte depuis le 02/10 | Non |

---

## 8. Équité et charge entre les équipes

| Équipe | Texte joueur écrit (citations, ordre de grandeur) | Effort physique | Étapes documentées | Statut de production |
|---|---|---|---|---|
| Slow | ~4 000 mots (pochette 2 800 + props 1 150) | Faible, 4 sorties courtes | 5 sur 5 | Textes finis, objets à fabriquer |
| Rando | ~1 200 mots (6 feuilles) | Élevé, 7 stations | 7 stations, 3 sans localisateur | Chaîne à fermer, parcours non marché |
| Sportif | 0 (3 textes de Seb non placés, ~925 mots) | Moyen | 0 sur ~3 | À écrire |

**[Lu]** Aucun document ne donne d'effectif par équipe (seul le total ~35 apparaît), ni la composition (âges, mobilité), ni la place de Bill et Monique dans les équipes le samedi. **[Déduit]** Une seule pochette (et une seule loupe, alors que la loupe coûte environ 2 € pièce) pour une équipe dont la taille n'est pas bornée est un goulot ; l'auto-sélection de l'email ne garantit pas l'équilibre.

---

## 9. Synthèse priorisée

### À faire avant samedi (bloquant ou peu coûteux)

1. **Clé 1** : valeur connue (dates gravées 1894-1994, 21/10). Reste à régler `KEY_FOUNTAIN` sur Vercel et à redéployer (`TODO.md`). **En cours.**
2. **Plan de mise en place** : décidé le 21/10 de le répartir vendredi 23/10, une fois que tout existe (`TODO.md`). **Planifié.**
3. **Chaîne Rando** : relève de Rémi ; les points sont notés dans `questions.md` #18 (§2). **Noté, en attente de Rémi.**
4. **Amorce de 14h15** : écrire les 3 dossiers de parcours (G-3), un feuillet chacun ; Batiste estime que c'est rapide (`TODO.md`). **À faire.**
5. **Scène de 17h30** : piste de Batiste (rituel sommaire, 3 masques + statuette) à confirmer avec la team (`questions.md` #20) ; texte du message toujours à écrire (Mareva, G-2). **À confirmer.**

### À décider en équipe

6. **Sportif** : un objectif énoncé, des étapes, une raison de détruire (§5.1). **En attente de Seb** (réponse annoncée le 21/10).
7. **Zone secrète** : fenêtre entre 18h00 samedi et 10h00 dimanche (§5.4) et récompense de Slow (§6). **Accepté le 21/10**, pas de verrouillage ; une pièce marquante dès le samedi reste facultative (`TODO.md`).
8. **Ivan convaincu ou en doute** ? **Tranché le 21/10** : il ne doute jamais. Texte du site à corriger dans la PR (`TODO.md`).
9. **Repli si une équipe n'a pas livré son trophée** : **tranché le 21/10**, un référent par équipe aide si besoin. Heure limite et aide possible à cadrer vendredi.
10. **Superposition de cartes** : qui apporte quelles cartes ; rédiger l'énigme du lieu (G-9). **Ouvert** (Rémi).

### À surveiller

11. Pluie dimanche (prévue) : plan B du rituel et sa marge de 30 minutes, peinture dorée et fumigènes sous la pluie. Samedi : pas de pluie annoncée, ~8°C.
12. Effectifs par équipe, nombre de pochettes et de loupes.
13. Payoffs non scriptés (`VEILLE`, Chouette, « trois piétons »). Le poids de la statuette est résolu (description canonique, §7).

### Tests humains que le repo ne peut pas remplacer

- **Lecture à froid** : faire lire la pochette (Slow) à une personne qui ne connaît pas le jeu et noter où elle bloque ou s'ennuie.
- **Marcher la chaîne Rando** (Rémi) avec un chronomètre, papier en main.
- **Dry-run** : le prévoir avant le 23/10 (il reste 3 jours) et le centrer sur 17h30 et sur le dimanche, les deux moments les plus tendus.
- **Vérifier que le nom, l'adresse e-mail et le domicile fictifs d'Ivan ne correspondent pas à une personne réelle**, puisqu'ils figurent sur une affiche, un faux article et un site.
