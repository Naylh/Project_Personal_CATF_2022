# -------------------------Stegoguess Introduction-------------------------

## Fichier donné : 
Christmas_MakHack.jpg

## Catégorie : 
Stéganographie

## Niveau : 
Facile

## Principe du chall : 
Introduire aux tools exiftool et steghide

## Auteur : 
Naylh

## Énoncé : 
Une mise en jambe pour la suite.

## Solve possible : 
Avec les tools installés ou avec aperisolve.com
- Utiliser le tool exiftool sur le jpg 

> exiftool Christmas_MakHack.jpg

- Regarder la partie "Comment" 

> steghide : w0wth4ts4n1c3p4ssw0rd

- Se renseigner sur le tool donné

> steghide

- Utiliser la passphrase donnée

> steghide extract -sf Christmas_MakHack.jpg

- Lire le fichier flag.txt

## Indices :
	1/ Quel est le nouveau nom de Facebook ? 
	2/ Une passphrase peut-être utile

## Flag : 
CATF{TH3S3_T001S_C4N_B3_US3FU1_1N_ST3G4N0}