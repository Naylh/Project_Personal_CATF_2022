# ----------------------------------Photos Souvenir----------------------------------

## Fichier donné : 
Aucun

## Catégorie : 
Osint

## Niveau : 
Moyen

## Principe du chall : 
Trouver le nom de toutes les villes où on été prise les photos.

## Auteur : 
Naylh

## Énoncé : 
Votre tante a fait un voyage autour du monde. Elle a pris des photos de toutes les villes qu'elle a visité. Elle a oublié de vous dire où elle a été. Vous trouvez les paysages joli et vous souhaitez visiter les mêmes pays. Retrouvez les pays qu'elle a visité.

Le flag est la concaténation en majuscule des noms des pays séparés par un underscore. Les pays avec un nom composé doivent être séparés par un tiret.

ex: CATF{FRANCE_ITALIE_ESPAGNE_ETATS-UNIS}

## Solve possible : 
- Faire des recherches inversé sur les photos avec Google Image, TinEye ou Yandex
- Pour la 5ème photo, regarder dans l'exif de la photo pour avoir les coorrdonnées GPS et les convertir en adresse
- Pour la dernière photo, faire un focus sur l'île dans le fond à droite ou sur le batiment juste en dessous de l'île

## Indices :
1. Utiliser les mêmes outils que pour les autres photos seront très probablement inefficaces, pensez à d'autre moyen de trouver la localisation.

## Flag : 
CATF{FINLANDE_LIECHTENSTEIN_ISLANDE_CANADA_FRANCE_NORVEGE}