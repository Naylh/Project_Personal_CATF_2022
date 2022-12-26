# ------------------------Santa_Met_A_Weird_Object------------------------

## Fichier donné : 
Aucun

## Catégorie : 
Osint

## Niveau : 
Moyen

## Principe du chall : 
Trouver le nom de la ville de décollage d'un satellite

## Auteur : 
Naylh

## Énoncé : 
En 2019, au milieu de sa tournée de cadeau, le père Noël a été distrait par son téléphone et il n'a pas vu la fusée décollée. Heureusement que ce vol n'était pas habité, malgré son accident les rennes et le père Noël vont bien mais mes cadeaux sont tombés. Trouver la ville de son crash pour que j'aille récupérer les miens.

**Format du flag** : CATF{CITYOFTHECRASH} (*tout en majuscule, collé, sans accent et en français*)

## Solve possible : 
- Chercher ce que peux transporter des fusées non habitées

> Des satellites

- Chercher un tracker de satellite (décollage ou live) 

> exemple : https://www.n2yo.com/

- Chercher à la date du 24 décembre 2019

> https://www.n2yo.com/browse/?y=2019&m=12

- Tomber sur https://www.n2yo.com/satellite/?s=44904 ou https://www.n2yo.com/satellite/?s=44903

- Trouver le site de lancement : 

> TYURATAM MISSILE AND SPACE COMPLEX

- Trouver la ville du site

## Indices :
1. L'objet que transportait la fusée est du même type que les objets nommés "Spoutnik" 
2. Le père Noël fait sa tournée le 24 décembre

## Flag : 
CATF{BAIKONOUR}