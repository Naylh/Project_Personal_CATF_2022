# --------------------------Packaging--------------------------

## Fichier donné : 
Present.bin

## Catégorie : 
Stéganographie

## Niveau : 
Moyen+

## Principe du chall : 
Faire découvrir les fichiers binaires en stéganographie

## Auteur : 
Naylh

## Énoncé : 
L'emballage compte aussi dans un cadeau.

Mettre le flag avec la format CATF{flag} avec le flag en minuscule tout attaché sans accent.

## Solve possible :
- Utiliser un héditeur hexadécimal pour voir le contenu du fichier

> HxD par exemple

- Remplacer le headers modifié par ceux d'un PNG

> %CPT....CHEF par %PNG....IHDR

- Enregistrer le résultat dans un fichier PNG et aller sur le lien

> https://cyberavent.ctfd.io/files/64d8006874b800a2ce0ba7617ff62838/Smaller_Present

- Changer l'extension par mp3

- Utiliser un téléphone pour récupérer les lettres qui sont en finlandais (si vous avez du mal à les récupérer vous pouvez découper l'audio sur chaque lettre et faire une liste de possibilité pour chaque lettre) mais normalement juste en découpant vous devriez avoir les lettres

- C'est la fin de l'url d'une vidéo youtube

- Aller sur le lien

> https://youtu.be/LSx7LIZ1Ezo

- Le morse a été converti en image, il suffit d'écrire sur un papier les . et les - pour avoir le flag

## Indices : 
1. Un éditeur héxadécimal peut être utile
2. Je sais que je suis ton youtubeur favori

## Flag : 
CATF{itakefunasican}