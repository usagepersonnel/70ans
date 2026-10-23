# Solutions — les 5 clés du site d'Ivan

Aide-mémoire organisateur pour débloquer `/archives` (onglet « 🔒 Dossier ») si l'équipe Batiste bloque le samedi. **À ne pas laisser traîner au gîte.**

L'ordre suit le circuit du village. La saisie est tolérante : minuscules/majuscules, accents et espaces ignorés.

| # | Lieu | Indice affiché sur le site | Réponse attendue | Autres réponses acceptées |
|---|---|---|---|---|
| 1 | Office du tourisme | Le mot caché dans le coin du tableau du chasseur | `VEILLE` (à la loupe) | `VEILLENT`, `LA VEILLE` |
| 2 | Fontaine à l'ours | L'année gravée sur la fontaine | `1894` ou `1994` (plaque émaillée bleue sous le bassin) | `1894 1994`, `1994 1894` |
| 3 | Étiquette botanique, côté monument aux fusillés | La plante du bourg dont le nom évoque la bête cornue | `Barbe de bouc` | `barbe a bouc`, `barbedebouc`, `aruncus`, `aruncus dioicus`, `dioicus`, `kneiffii`, `rosaceae`, `fernald`, `094 2010` (la référence de l'étiquette) |
| 4 | Église, vitrail de saint Pierre | Ce que le vitrail promet de donner | `les clefs du royaume du ciel` | Toute réponse contenant `clef`, `cles`, `cle`, `royaume`, `royaume du ciel`, `royaume des cieux`, `ciel`, `cieux` (ex. « des clés », « le royaume des cieux » passent) |
| 5 | Cimetière, tombe de pierre grise | Ce qui est inscrit sur la tombe du notable innocent | `SOUVENIR — À NOS CHERS DISPARUS` (plaque posée dessus) **ou** « rien » (la pierre est nue) | `a nos chers disparus`, `chers disparus`, `souvenir`, `rien`, `aucun`, `vide`, `effacée`, `rasurée`, `anonyme`, `sans nom`, `pas de nom`, `pas d'inscription` |

## En pratique

- Chaque champ valide indépendamment (✅ vert par champ) : si un seul est faux, les autres restent validés.
- La clé 4 est la plus permissive : « clefs » ou « ciel » seuls suffisent. Si un joueur écrit une formulation complète un peu différente (« les clés du ciel »), ça passe aussi.
- La clé 5 accepte les deux lectures : la plaque (« à nos chers disparus ») et la pierre nue (« rien », « sans nom »).
- En dernier recours : taper les réponses soi-même pour eux, ou leur souffler une formulation courte (« clés », « souvenir »).
- ⚠️ Les réponses exactes en production vivent dans les variables d'env Vercel (`KEY_PAINTING`, `KEY_FOUNTAIN`, `KEY_PLANT`, `KEY_GLASS`, `KEY_TOMB`). Ce fichier reflète les valeurs prévues ; si une réponse de cette liste est refusée en prod, c'est la variable d'env qui fait foi (à vérifier dans le dashboard Vercel ou avec Devin).
