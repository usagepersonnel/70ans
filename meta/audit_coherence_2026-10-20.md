# Audit de cohérence — 20 octobre 2026

Application de `meta/methode_coherence.md` sur `70ans` + `ivan-beaulieu-photos`.

**Légende** : 🟢 correction mécanique évidente (doc rot vs décision actée) · 🟠 arbitrage design/équipe requis · 🔵 surveillance (pas faux, mais fragile ou à harmoniser)

**Bilan** : 0 contradiction bloquante dans le socle canonique. 3 familles de problèmes : (1) doc rot dans les fichiers de synthèse (`lore/lore.md`, `meta/timeline_lore.md`, `design/deroule.md`, `design/reperage.md`) — attendu, c'est le prix des docs de référence ; (2) quelques frictions matérielles/scénaristiques à trancher avec Seb & Rémi ; (3) micro-ajustements sur le site web.

---

## 🟠 Arbitrages à trancher (avec l'équipe, pas unilatéralement)

### A. Date du fugitif : 1746 vs ~1886
- `joueurs/rando/feuilles_rando.md` : « 9 septembre 1746 » partout ; `lore/lore.md` l.105 + `meta/timeline_lore.md` l.24,58 : « fin du cycle précédent (~1886) » ; `questions.md` #18 pose déjà la question à Rémi.
- **Impact collatéral trouvé** : le site code déjà « vers 1746 » (`disparitions.astro` l.12) — si Rémi choisit 1886, il faut modifier le site.
- **Recommandation** : 1746. Chaque année a alors un rôle propre : 1746 = fugitif (2 cycles avant), 1886 = Marcellin + almanach + tableau (1 cycle avant), et les apparitions 1894/1944 = patrouilles hors-cycle (point H). Si 1886 : réécrire les dates des feuilles + déplacer la lettre de Marcellin.

### B. La statuette « dans ma gourde » (plausibilité matérielle)
- `joueurs/rando/feuilles_rando.md` l.190 : le fugitif cache « ce que je leur ai subtilisé » (la statuette) **dans sa gourde** ; `joueurs/slow/pochette/04_lettre_enfant_grotte.md` : la statuette fait « à peine plus grande qu'une main » — ça ne rentre pas dans une gourde.
- Fix trivial : « à côté de ma gourde » / « dans mon baluchon » — ou réduire la statuette. À signaler à Rémi dans la réécriture des feuilles.

### C. Destruction de la statuette : marteau vs « rituel de purification »
- `joueurs/rando/feuilles_rando.md` (Scialet→Refuge) : « il faut un **rituel de purification** pour la détruire » ; `design/enigmes.md` A3 ajoute « (canon : la statuette ne se brise pas à coups de marteau) » — pourtant les joueurs la brisent physiquement à ~18h.
- Pont possible déjà esquissé : « les masques sont essentiels au rituel » (Col de Carri) → un joueur masqué la brise. Mais **nulle part le mécanisme exact n'est écrit** : la destruction physique marche-t-elle seule ? le « rituel de purification » était-il une croyance erronée du fugitif ? → à trancher dans la réponse de Seb/Rémi (déjà dans `questions.md` #17).

### D. Statuette « immuable » (réapparition magique) vs « replacée par les Perchten »
- `design/enigmes.md` l.60 propose *« la statuette réapparaît toujours dans la grotte »* ; le canon validé (02/10) dit : les Perchten ont rattrapé le fugitif et **replacé** la statuette (`lore/lore_precisions.md` l.53).
- Recommandation : garder la version validée — dans `joueurs/rando/feuilles_rando.md` « seule la statuette semble immuable » est déjà une croyance du fugitif, pas un fait. Annoter `design/enigmes.md` l.60 pour éviter de re-proposer la version magique.

### E. Apparitions Perchten hors-cycle (1894, 1944) — TODO #6
- Nouvel élément trouvé : l'almanach (`joueurs/slow/props/05_enigme_vieux_calendrier.md`) liste les Grandes Veilles à **1606 / 1746 / 1886** — donc 1894 et 1944 ne sont *pas* des années de cycle, ce qui élimine la piste (b) « cycles plus courts ».
- Reste la piste (a) : **les Perchten patrouillent en permanence** (« ils veillent » — le mot caché du tableau !). Le rituel n'est qu'en fin de cycle ; entre-temps ils gardent la montagne. C'est déjà compatible avec le lore — il suffit de l'écrire noir sur blanc pour fermer la question.

### F. Voix de la forêt — TODO, toujours ouvert
- `design/enigmes.md` l.112 suggère « voix = les phénomènes du Triangle qui veulent la fin des Perchtenlauf » — ça créerait un antagoniste mais **contredit « le maléfice n'a pas de volonté »** (✅ validé). L'option (a) « échos du passé » reste la plus compatible avec le canon ; l'option (b) « récit non fiable / psychologie du fugitif » est encore plus sûre.

### G. Les deux versions du sac (feuilles_rando, déjà connu)
- Texte de base : il retourne à la cabane et **abandonne** le sac (« je l'ai laissé là bas ») ; version « adaptée à l'époque » : des fidèles l'ont **devancé** — incompatibles. À trancher dans la réécriture (avec Rémi).

### H. Le « squelette du fuyard » au Col de Carri
- Indice on-site dans `joueurs/rando/feuilles_rando.md` l.146 alors que le squelette n'est **pas** le fugitif (validé) et que `validation_2026-10-19` pt 11 le marque « potentiellement abandonné ». Si gardé comme décor : rien ne dit aux joueurs que ce n'est pas lui — suggestion d'`design/enigmes.md` (crâne = décor « porte de l'Enfer ») à acter.

### I. Bouteilles des parents : samedi ou dimanche ?
- `design/deroule.md` l.29 : décor au gîte « secret d'Ivan » + note « [à voir si pas plutôt dimanche ?] » ; `design/enigmes.md` l.114 + `validation_2026-10-19` pt 10 : � **plutôt dimanche** (dernière carte à superposer). → Harmoniser `design/deroule.md` sur « dimanche ».

### J. Site — « Réservations closes » vs « formulaire resté actif »
- `sorties.astro` : « Réservations closes. Suite au décès d'Ivan… — La famille » ; mais l'email de Camille dit que **le formulaire fonctionnait encore** (sinon pas de réservation à annuler !).
- Fix élégant : dater la mention — « *(mise à jour du 24 octobre 2026)* » : Camille a fermé les résas **en découvrant** la réservation du groupe. Sinon, retirer la mention « closes » du texte de la famille. (PR côté repo site.)

### K. « Quinze ans » vs « vingt ans » d'affûts
- « Vingt ans » : affiche (`joueurs/slow/props/02_affiche_habitants_de_la_nuit.md`), conférence (`conference.astro`), fiche d'Ivan (`07`). « Quinze ans » : journal mai 2024 (`journal.ts`), dossier (`dossier.astro`).
- Recommandation : canon = « vingt ans » (3 sources dont les plus tardives) → corriger `journal.ts` et `dossier.astro`.

### L. « Trois nuits » et « le compteur s'est arrêté » (audio.astro)
- `02_releves` : les 3 bandes ont été enregistrées **le même week-end** (26–27 oct. 2024) — « trois nuits » est faux ; 18:47 n'est d'ailleurs pas la nuit.
- « Les heures sont celles où le compteur s'est arrêté de tourner » ≠ les heures où les voix se font entendre — pour l'énigme danse, ce sont les horaires des **sons**.
- Suggestion : « Trois bandes, trois veilles du même week-end. Les heures : celles où ils se sont fait entendre. » + harmoniser le carnet d'écoute du site (vague) avec la version détaillée de `joueurs/rituel/enigmes_dimanche.md` (« 4 sons + 4 s de silence + une foule pour répondre »), qui est le filet de sécurité du dimanche.

### M. « Le cadran solaire du bourg » (slow_05)
- `design/reperage.md` : **aucun cadran solaire** au village → risque de fausse piste (des joueurs qui partent le chercher). Suggestion : « 10 h 00 au soleil des anciens » sans mentionner un cadran « du bourg » (ou accepter qu'il a existé en 1886 et disparu — auquel cas l'almanach ne doit pas suggérer qu'on peut aller le lire).
- Et dans l'almanach : « la brèche demeurerait ouverte **pour un siècle** » → incohérent avec le cycle de 140 ans → « pour cent quarante ans » / « jusqu'à la prochaine Veille ».

### N. « Matériau inconnu, très légère » vs prop en terre (Mareva)
- Le fugitif décrit un matériau « qui ne provient pas de ce monde » ; la statuette fabriquée est en **terre** — la terre cuite est parfaitement connue au XVIIIe. Soit le prop reçoit une finition étrange (patine, éclat, légèreté = creuse), soit on ajuste la description (« d'une terre grasse bizarrement légère »). Vigilance à la fabrication.

### O. Les 3 « piétons » ont survécu — alors pourquoi la chaîne est-elle rompue ?
- La coupure (`06`) dit que les silhouettes « regagnèrent le sous-bois » → pas mortes en apparence. Le canon dit que la raison de l'absence des Perchten n'est **pas expliquée** (déductible, jamais énoncée) — OK en l'état, mais la note de design « l'accident a brisé leur relais » est une lecture, pas un fait : veiller à ce qu'aucun texte joueur ne la confirme explicitement. �-voisin de �🟠 : à garder en tête à la relecture.

### P. Survie physique des feuilles du fugitif
- Des feuillets de 1746 lisibles en 2026 le long d'un sentier : invraisemblable en physique stricte, mais **convention de genre acceptée** (comme les journaux trouvés dans les donjons). Le fait qu'Ivan ait trouvé le dernier message « près de la fontaine » peut même couvrir une partie (il les aurait collectées/étudiées ?). Pas de fix nécessaire — juste ne pas attirer l'attention dessus dans les textes.

### Q. Feuille du Belvédère : « le soleil se levait » vs horodatages
- Belvédère « milieu de matinée » évoque le lever de soleil passé ✓ cohérent. Par contre l'encre « ils m'encerclent » fin de journée à La Chapelle : le fugitif est descendu « en Nord » vers le village — la source = la fontaine du bourg ✓ ça boucle (Ivan a trouvé le message près de la fontaine). OK, juste vérifier que le parcours de Rémi rend cette boucle crédible géographiquement.

---

## 🟢 Corrections mécaniques (doc rot — appliquer directement)

> **État d'application (20/10, commit local)** : tout est appliqué **sauf** les items 56–60 (repo `ivan-beaulieu-photos` → PR séparée, jamais de push direct sur `main`), l'item 38 (dates du rétroplanning laissées indicatives), l'item 48 (années sautées du tableau : acceptable tel quel) et l'item 55 (timestamps des photos WhatsApp : vigilance de production, pas une correction). Items 61–62 (terminologie « carnet »/« Slow ») appliqués aux endroits où la précision compte.

### `lore/lore.md` (le plus périmé — TODO #2 en cours)
1. l.48–50 : planning samedi « 14h–14h30 fouille → 14h30–14h40 formation → 14h40–17h30 terrain » → remplacer par : 14h lancement commun, ~14h15–14h30 séparation des 3 arcs autonomes, 17h30 regroupement.
2. l.63 : « lieu / arts plastiques / rituel » → **terrain / statuette / danse**.
3. l.95 : supprimer le Géoguesser (abandonné 11/10).
4. l.141–144 : supprimer « Transmettre des infos aux équipes mobiles » + « Géoguesser » de l'arc tranquille.
5. l.146–148 : équipe sportive « conditions de destruction + partie des costumes » → actualiser : pièges photo + énigmes animaux → **toutes les tenues/masques**.
6. l.154–157 : « triangulation de photos de piège » chez la rando → c'est l'arc de Seb ; retirer « morceaux de costumes » du trésor rando.
7. l.204 : « partie secrète (jour 2) : nécessite un code » → accès **samedi** via les 4 clés de la pochette.
8. l.209 : « entrer en contact avec la fille/fils d'Ivan » → message unique au lancement.
9. l.190 : tableau « figure assise qui mange sur un rocher » vs `joueurs/slow/props/04_tableau_chasseur_et_loupe.md` « silhouette debout près d'un rocher » → harmoniser la description (debout + statuette sur le rocher plat + chasseur caché derrière un sapin).

### `meta/timeline_lore.md`
10. l.38–39 : « 14h–14h30 fouille commune » → lancement 14h ; « fouille de la chambre d'Ivan » = équipe Slow à 14h30 ; « trois équipes sur le terrain » → nuancer (Slow au gîte jusqu'à 15h15).
11. l.41 : « encre invisible dans les douches » → miroirs de l'espace commun.
12. l.43 : anciens noms de groupes → terrain / statuette / danse.
13. l.50 : « le carnet d'Ivan » → la pochette/sacoche (terminologie, cf. point 24).
14. l.58 : « ~1886 » pour le fugitif → dépend de l'arbitrage A.

### `lore/lore_precisions.md`
15. l.8 : « excalidraw plus fiable en cas de contradiction » → préciser « sauf décisions ultérieures actées dans `validation_*` ».
16. l.74, 96–98 : « partie secrète (jour 2) » → accès samedi via les 4 clés (TODO #3).
17. l.105 : anciens noms de groupes dans le mapping manifestations.
18. l.92 : « la grotte semble être à la fois repère et lieu du rituel » → contredit l.26 (centre = le champ, grotte à 23 km) — la version terrain gagne ; annoter.

### `design/deroule.md`
19. l.29 : bouteilles → « dimanche » (cf. I).
20. l.48 : regroupement « 17h15–18h » + destruction « ~18h » vs `design/enigmes.md` « ~17h30 » → unifier (regroupement ~17h30, destruction à la suite).
21. l.52 : « À trancher : mécanisme quelle chambre » → **résolu** (`joueurs/slow/props/03_livre_dor_2011_chambre.md` : livre d'or + étiquette Chouette décollée).
22. l.52 + l.110 : « forme de la voyante » → **résolu** : document (`joueurs/slow/pochette/05_transcription_voyante.md`), pas de PNJ.
23. l.95 : « douches/miroirs → arts plastiques » → « miroirs → statuette » (nouveaux noms + support).
24. l.108 : « quel document va à quelle équipe » → **mappé** : tout dans la pochette d'Ivan (arc Slow).
25. l.121 : « Fouille du gîte (14h–14h30) » → horaire périmé.
26. l.34 : « commerçant pas généreux : énigme ou service à rendre » vs `joueurs/slow/props/04_tableau_chasseur_et_loupe.md` Option 1 « zéro sollicitation » → trancher (🔵 : recommander Option 1/2 de `joueurs/slow/props/04_tableau_chasseur_et_loupe.md`, sobre).

### `design/enigmes.md`
27. l.97 : « 15 ans de relevés » vs carnet « quatorze ans » → harmoniser (« quinze veilles » ou « 14 ans », au choix).
28. l.111 : « (B5) » → référence inexistante → B4.
29. l.117 : « Chambre d'Ivan ❓ dernier trou » → résolu.
30. l.113 : « Manque : un lien site↔statuette » → partiellement comblé (carnet p.2 + voyante + tableau) ; l.60 : annoter « version magique écartée, cf. canon » (point D).
31. l.34 : « trois fiches itinéraire » vs `joueurs/slow/props/01_lancement_email_enfant.md` « trois dossiers de parcours » → harmoniser le terme.

### `design/reperage.md`
32. l.19 : « Fouille (samedi 14h–14h30) » → horaire périmé (14h30–15h15, Slow).
33. l.28 : « douches → arts plastiques » → miroirs → statuette.
34. l.36 : « groupe lieu » → terrain ; l.38 : « carnet » → pochette.

### `questions.md`
35. Numérotation : deux fois « 14 » (sections Assets et Équipe) → renuméroter.
36. Q6 : prénom → **Camille** choisi (`joueurs/slow/props/01_lancement_email_enfant.md`) ; Q7 : année de naissance → l'article `06` fixe **73 ans en oct. 2025 → né ~1952** ; Q8 : date accident → **nuit du 18 au 19 oct. 2025** fixée partout → marquer ces questions résolues/provisoires.

### `design/retroplanning.md`
37. l.48 : « Casting PNJ (voyante, si option PNJ) » → obsolète (document retenu).
38. Dates : jalons « 18 oct — contenus écrits » dépassés → rafraîchir ou marquer indicatif (🔵).
39. Mettre à jour les statuts : carnet ✅ (`joueurs/slow/pochette/`), props Slow ✅ (`joueurs/slow/props/`), email/affiche/livre d'or/calendrier rédigés.

### `README.md`
40. Inventaire incomplet : ajouter `questions.md`, `joueurs/slow/props/`, `joueurs/slow/pochette/`, `assets/cartes/`, `archive/`, `joueurs/rituel/README.md`, `meta/methode_coherence.md`, `meta/audit_coherence_2026-10-20.md` ; préciser que `archive/ref_archive.md` est dans `archive/`.

### `AGENTS.md`
41. « a capturé des images … **avant de disparaître** » → Ivan est **mort** dans un accident — « disparu » pourrait laisser croire qu'il est vivant/caché (faux lore !).
42. Structure : ajouter les dossiers/fichiers manquants (même liste que README).
43. Synopsys « ± 1 jour du changement d'heure » → le rituel = le dimanche du changement d'heure, deadline 11h30 (préciser).

### `TODO.md`
44. #5 « récent décès » → **résolu** (`assets/ivan/ivanbio.md` dit « décès en octobre 2025 »).
45. Ajouter pointeurs : l'audit complet = ce fichier ; mettre à jour #1 (impact site), #6 (nouvelle lecture ci-dessus).

### `joueurs/slow/pochette/02_releves_2011_2025.md`
46. 2011–2018 parlent de « déclenchements » alors que l'enregistreur arrive en 2019 et les pièges en 2021 → reformuler les premières lignes en « observations » (ou préciser un premier boîtier photo).
47. Ligne 2025 « 18–19 oct. » n'est **pas** le week-end du changement d'heure (25–26 oct.) — c'est poignant (il meurt avant sa veille) mais le tableau ne le souligne pas : ajouter une micro-note type « *(remontée exceptionnelle — la convergence approche)* » ou laisser tel quel (🔵, au choix).
48. Années sautées (2012, 2014, 2016) : acceptable (« années sans relevé ») ou compléter (🔵).

### `joueurs/slow/props/04_tableau_chasseur_et_loupe.md` et `joueurs/slow/props/05_enigme_vieux_calendrier.md`
49. `joueurs/slow/props/04_tableau_chasseur_et_loupe.md` : cartel « novembre 1886 » → la Grande Veille 1886 = dernier dimanche d'octobre ; une rencontre en novembre est plausible (patrouille) mais « fin octobre 1886 » collerait mieux au cycle (🔵).
50. `joueurs/slow/props/05_enigme_vieux_calendrier.md` : « cadran solaire du bourg » + « pour un siècle » → cf. point M.

### `joueurs/slow/pochette/04_lettre_enfant_grotte.md`
51. Marcellin : 9 ans en 1886 → ~44 ans en 1921 avec des « petits-enfants » — serré mais possible ; ✅ **appliqué** : lettre redatée au 3 novembre **1931** (54 ans, petits-enfants plausibles). Propagé dans `meta/methode_coherence.md`.

### `joueurs/slow/pochette/06_coupure_presse_accident.md`
52. Post-it des hôtes : « quand **iel** passera » — le pronom inclusif peut jurer sur un prop réaliste → « quand elle/il passera » ou « pour la famille » (🔵, choix de style).

### `assets/photos/` (sources)
53. `assets/sources/perchtenlauf_loup.md` + `assets/sources/perchtenlauf_hiboux.md` = sources dupliquées mot pour mot dans `07_annexes` — ajouter une ligne « source » dans chacun ou déplacer dans `archive/` pour respecter le principe source unique.
54. Pas de doc « Bouquetin » : déjà noté TODO #7 — `07` l'exploite (« pas encore trouvé de coupure, c'est celui que décrit Marcellin ») → la couverture par l'absence fonctionne ; la question devient : faut-il un troisième doc historique pour la symétrie ? (🔵 réponse actuelle : non nécessaire).
55. **Images WhatsApp datées 2026-10-18** (noms de fichiers) : si un horodatage visible dans l'image affiche une date **postérieure à oct. 2025**, elle ne peut pas être « une photo d'Ivan » → vérifier les timestamps en incrustation avant usage sur le site (🔵 à vérifier à la production).

### `ivan-beaulieu-photos` (PR séparée — jamais de push direct sur `main`)
56. `journal.ts` « Quinze ans » → « vingt ans » (point K).
57. `dossier.astro` « quinze ans d'affûts » → « vingt ans » (point K).
58. `sorties.astro` : dater la mention « Réservations closes » (point J).
59. `audio.astro` : « trois nuits » → « trois veilles » ; reformuler « compteur arrêté » (point L) ; aligner le carnet d'écoute sur la version détaillée de `joueurs/rituel/enigmes_dimanche.md`.
60. `disparitions.astro` : dépend de l'arbitrage A (1746 codé en dur).

### Terminologie transverse
61. « carnet d'Ivan » désigne partout la pochette/sacoche de feuilles volantes — pas un carnet. Le nom de dossier `joueurs/slow/pochette/` + `joueurs/slow/pochette/README.md` entretient l'ambiguïté. Recommandation 🔵 : parler de « pochette d'Ivan » (dossier → `joueurs/slow/pochette/` inchangé, mais renommer les mentions « carnet » en « pochette » dans les docs actifs où la précision compte : `design/enigmes.md`, `design/deroule.md`, `meta/timeline_lore.md`).
62. « Équipe tranquille » / « équipe statique » / « groupe Slow » cohabitent → normaliser sur **« équipe tranquille (Slow) »** dans les docs actifs (🔵).

---

## Points validés comme cohérents (pas d'action)

- Cycle 140 ans : 1606 / 1746 / 1886 / 2026 présent et cohérent dans `lore_precisions`, `timeline_lore`, `joueurs/slow/props/05_enigme_vieux_calendrier.md`, `02_releves` ✅
- 25 oct. 2026 = dernier dimanche d'octobre = jour du changement d'heure réel ✅
- Conférence ven. 17 oct. 2025 → mort nuit 18→19 oct. → article dim. 19 → email « il y a tout juste un an » 24 oct. 2026 : chaîne parfaitement cohérente partout (carnet, coupure, email, site, validation) ✅
- La coupure `06` sous l'élastique (ajoutée par les hôtes) : anachronisme résolu ✅
- 4 clés du gate : ordre et contenus identiques entre carnet `01`, page `/archives`, `keys.ts`, `.env.example` ✅
- Pièges n°2 @00:03 / n°4 @06:12 / n°1 @18:47 : cohérents entre `02_releves` et `pieges.astro` (et le piège n°1 = celui qu'Ivan allait relever le soir de sa mort 👌) ✅
- « Quatre ans de relevés nocturnes » (pièges depuis 2021) : cohérent affiche + conference + journal + `02` ✅
- Voyante : mercredi 8 oct. 2025 = vrai mercredi ; « quarante euros » + carte de visite de Die (pas de lieu au village) : cohérent avec la contrainte terrain ✅
- « Couvre-feu » oct. 2020 dans `02` : détail réel exact ✅
- Les douches → miroirs : déjà propagé dans `joueurs/rituel/` et `design/reperage.md` ; restent des traces dans `lore/lore.md`/`meta/timeline_lore.md`/`design/deroule.md` (listées ci-dessus)
- « Ma carte du triangle est dans le carnet que je garde sur moi » (`disparitions.astro`) : justifie élégamment l'absence de carte du triangle dans la pochette ✅
- Hannibal ~218 av. J.-C., procès « Automne 1466 vigile de la Toussaint », lettre « fin oct. 1886 » écrite 3 nov. 1931 : datations internes cohérentes ✅

## Reste en dehors du périmètre (volontaire)

- `archive/excalidraw/excalidraw*.md` : snapshots du brainstorm initial — **ne pas corriger**, c'est une archive (Niveau 5).
- `archive/` : idem.
- Les `<a_confirmer>` volontaires sur les arcs Seb/Rémi : ce ne sont pas des incohérences, c'est le périmètre de travail des autres.

---

## Suivi post-audit (21/10)

Réponses de Seb (chat) :

- ✅ Lancement 14h + email de Camille : OK pour lui.
- ✅ Son équipe ramène **toutes les tenues et masques** (+ probablement des cailloux peints) ; les clichés de pièges sont sur le trajet ou pointent vers un lieu du trajet (arrêt-espèce). → partie « Seb » du point C levée, **sauf réponse contraire de Rémi** sur « détruire vs purifier ».
- 🟠 Toujours ouvert : 1re amorce à 14h15, indice « détruire » dans sa cache, provenance/droits réels des photos de pièges.
- 🟢 Nouveau : `assets/sources/perchtenlauf_bouquetin.md` (upload 20/10) complète le trio → TODO #7 résolu. Reste : texte **non daté** ; apparition à la **Grande Moucherotte** (nord Vercors, ~60 km du jeu — le texte de 1944 est lui local, « nord de Vassieux ») ; placement des 3 textes à trancher (pochette `07` vs épinglés au gîte — cohabitation possible).
- Point E : la lecture « patrouilles ordinaires » tient — le trio confirme des apparitions hors-cycle espacées (1894, 1944, [Bouquetin à dater]).
