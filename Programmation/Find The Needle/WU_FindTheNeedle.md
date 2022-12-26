# --------------------------Find The Needle--------------------------

## Fichier donné : 
Arbre.zip

## Catégorie : 
Programmation

## Niveau : 
Hard

## Principe du chall : 
Essayer de forcer les joueurs à optimiser leur code et de leur faire faire du parallelisme.

## Auteur : 
Naylh

## Énoncé : 
Un de vos amis qui est très doué de ses mains a caché un message dans une aiguille du sapin de Noël. À vous de retrouver ce message.

Les caractères du flag ont été chiffré une première fois en vigenère avec la clé CATF puis chaque caractère de ce hash a été transformé en morse.

Des threads et une optimisation du code vous seront sûrement utiles...

Le flag est de la forme CATF{message}.
La taille de "message" est de 17 caractères.
Le décalage entre chaque caractère est régulier.

Ex : Si le premier caractère du flag est dans la branche1, leaf1, needle1 et que le deuxième caractère du flag est dans la branche2, leaf2, needle2 alors le troisième caractère du flag est dans la branche3, leaf3, needle3.

Bon courage !

Auteur : Naylh

## Solve possible : 
- À la main (très long) ou en programmant

> Voir SolveFindTheNeedle.py

- Récuperer les caractères du flag en morse

- Déchiffrer le morse

- Déchiffrer le vigenère avec la clé CATF

## Indices :
1. Le décalage des caractères est tel que :
Si le premier caractère du flag est dans la branche1, leaf2, needle3 alors le deuxième caractère du flag est dans la branche2, leaf3, needle4.

## Flag : 
CATF{4L0T0FW0RKF0RTH4T}
