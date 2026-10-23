# aimprimer — versions PDF économes en encre

Versions **fond blanc** des props, pour l'impression réelle. Les versions « écran » (fond vieilli, grain, plis) restent dans `assets/photos/site_ivan/` — elles servent de scans pour le site d'Ivan.

- Rendues depuis les mêmes pages prop que les versions écran, avec le paramètre `?blanc` (branche prop/almanach du repo du site, dossier de sortie `PROP_OUT` = ce dossier).
- `aimprimer/almanach_1886.pdf` : **recto seul** (paramètre `?recto`) — le verso quasi vide n'est pas imprimé.
- `aimprimer/livre_dor_2011.pdf` : **texte seul** (paramètre `?nu`) — sans le cadre réservé à la photo.
- `aimprimer/07_annexe_1894.pdf` : inclut la gravure du loup (comme la version écran).
- Absents volontairement : 05_carte_madame_solange (imprimée depuis la version écran, petit carton), tous les `.png`.

Rappel : le travail à la main après impression (découpe, annotations, déchirures) est décrit dans `checklist_mise_en_place.md`.
