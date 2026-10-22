# `joueurs/batiste/props/05_enigme_vieux_calendrier.md` — L'énigme du Vieux Calendrier (Samedi 16h30 au gîte)

## Rôle dans le jeu
- **Quand** : Trouvé à 14h45 dans la pochette d'Ivan (en même temps que la loupe), mais résolu tranquillement au chaud au gîte vers **16h30** (pendant ou juste après l'exploration du site web), ou le dimanche matin à 10h00.
- **Ce que ça résout dans le déroulé (`design/deroule.md` l. 42 & `lore/lore_precisions.md` #11)** :
  - Il fallait une énigme **100 % auto-portante** (le document contient toutes les règles nécessaires à sa propre résolution) qui explique **pourquoi le rituel a lieu au changement d'heure d'octobre** et qui fait calculer aux joueurs **l'heure limite du dimanche matin (11h30)**.
  - Elle donne aussi un vrai rôle aux **dates gravées sur la fontaine** ou aux **cycles de 140 ans** (1606 — 1746 — 1886 — 2026).

---

## La mécanique de l'énigme (simple, élégante et vraie historiquement !)

Pourquoi les anciens faisaient-ils le rituel « à la dixième heure du soleil » fin octobre, et pourquoi cela tombe-t-il **à 11h30 aujourd'hui** ?
Parce qu'entre le cycle de 1886 et celui de 2026, les humains ont déréglé leurs montres deux fois :
1. **En 1891 / 1911** : la France abandonne l'**heure solaire locale** (le méridien de La Chapelle-en-Vercors est à ~5°30' Est, soit **+22 minutes** d'avance sur Greenwich) pour s'aligner sur le fuseau horaire.
2. **En 1916 / 1976** : on instaure le **changement d'heure** (en hiver, la France est à **UTC+1**, soit **+60 minutes** sur le soleil de Greenwich).
3. Et Ivan y ajoute la **dérive du cycle de 140 ans** !

Mais pour que le calcul soit un plaisir ludique faisable en 5 minutes par toute la famille (sans trigonométrie !), tout est donné sous forme de **3 règles d'horloger** écrites noir sur blanc sur l'Almanach.

---

## Texte du document à imprimer (Recto : page d'Almanach ancien / Verso : note de calcul d'Ivan)

### RECTO — Feuillet d'Almanach dauphinois de 1886

> **ALMANACH PASTORAL DU ROYANS & DU VERCORS — ANNÉE 1886**
> *Pour la conduite des troupeaux, des foires et des veilles d'automne*
>
> ---
>
> **Des Grandes Veilles séculaires (dites *Rondes des Trois*) :**
>
> « Qu'on s'en souvienne de père en fils : la Grande Veille qui apaise les brumes de la montagne ne se tient qu'une fois tous les **cent quarante ans**, le **dernier dimanche d'octobre**.
>
> Elle fut tenue par nos aïeux en l'an **1606**, puis en l'an **1746**, et se tiendra de nouveau en cette année **1886**.
>
> **De l'heure juste où le cercle doit être refermé :**
> Les Trois Veilleurs doivent avoir achevé leur ronde **au dixième coup du cadran des anciens (10 h 00, heure du soleil)** — ni après, car l'ombre du roc aurait tourné et la brèche demeurerait ouverte jusqu'à la prochaine Veille. »
>
> ---
>
> **Table de concordance des horloges modernes (ajoutée par l'horloger de Die, 1976) :**
>
> *Attention ! Nos montres modernes ne marquent plus l'heure du soleil de 1886. Pour convertir une heure du soleil des anciens en heure de votre montre un dimanche de passage à l'heure d'hiver :*
>
> 1. **Règle du Fuseau de Paris (+ 1 heure) :** Depuis l'adoption de l'heure légale d'hiver (UTC+1), nos montres avancent d'**1 heure pleine (60 minutes)** sur le méridien.
> 2. **Règle de la Reculée d'Octobre (+ 1 heure la veille, − 1 heure dans la nuit) :** Dans la nuit du samedi au dimanche d'octobre, les montres reculent d'une heure à 3 heures du matin — on est donc bien en **heure d'hiver** le dimanche matin.
> 3. **Règle du Retard séculaire des Crêtes (+ 30 minutes par cycle de 140 ans depuis 1886) :** À chaque cycle de 140 ans écoulé depuis 1886, le lever du soleil derrière la crête de Ferrières prend **30 minutes** de retard sur l'ancien repère de pierre.

---

### VERSO — Note manuscrite d'Ivan au crayon

> *« J'ai retrouvé ce feuillet d'almanach de 1886 plié dans un vieux paroissien de La Chapelle.*
>
> *Si quelqu'un lit cet almanach à l'automne de la prochaine Grande Veille : faites le calcul avec les 3 règles du recto pour savoir **avant quelle heure précise à votre montre** tout doit être accompli le dimanche matin. Ne vous trompez pas d'une demi-heure ! »*

---

## Version retenue (21/10) : les joueurs font le calcul

Le verso ne donne **pas** le résultat : les joueurs font eux-mêmes `1886 + 140 = 2026` (1 cycle) → `10h00 (soleil) + 1h00 (Règle 1) + 0h30 (Règle 3, 1 cycle) = 11h30`. C'est un vrai moment d'énigme pour l'équipe — et la note d'Ivan prévient déjà : « ne vous trompez pas d'une demi-heure ».

*Version de secours (non retenue) : le verso d'Ivan donnait directement `11h30` — à réintroduire si l'équipe bloque.*

---

## Prompt visuel (à fournir à l'IA avec le texte du feuillet)

> Rends le document suivant sous forme d'une **page d'almanach rural français du XIXe siècle**, feuillet A4 vieilli (le VERSO sera imprimé quasi vierge — la note d'Ivan est écrite au crayon à la main après impression).
>
> - **Mise en page d'almanach** : cadre à filets ornementés, titre en lettres ornementales « ALMANACH PASTORAL DU ROYANS & DU VERCORS — ANNÉE 1886 », sous-titre italique, filets de séparation, quelques petites vignettes gravées rustiques en coins ou en têtes (lune, soleil, faucille, branche — pas plus).
> - **Deux registres typographiques** : le texte de 1886 en caractères anciens ; la « Table de concordance des horloges modernes (ajoutée par l'horloger de Die, 1976) » dans une typographie volontairement **plus moderne** (machine à écrire ou casse sobre) — c'est un ajout tardif au feuillet.
> - **Papier** : jauni, taches d'humidité en coins, une pliure médiane ancienne, bords un peu effrangés.
> - **Interdit** : aucune apparition du résultat (`2026`, `11h30`, `11 h 30`) nulle part dans le visuel — les joueurs doivent le calculer.
