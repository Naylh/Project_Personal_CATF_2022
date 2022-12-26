# --------------------------Santa Has Time To Lose--------------------------

## Fichier donné : 
None

## Catégorie : 
Stéganographie

## Niveau : 
Hard

## Principe du chall : 
Un enchainement de blocage différent, du type poupée russe, il faut passer tous les locks pour réussir. Ça fait découvrir plusieurs types de fichiers que l'on peut rencontrer en stéganographie mp3, zip, image, texte. Il fait également découvrir la manipulation des bits des images (LSB).

## Auteur : 
Naylh

## Énoncé : 
Tu as été vilain(e) cette année mais le père Noël n'aime pas voir d'enfant sans cadeau. Pour te punir il a mis ton cadeau sous clé. À toi de réussir à le récuperer. Il ne te laisse que ceci :

> ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++.++++++++++++..----.+++.<------------.-----------..>+++.-------.---.+++++++++.--------.--------.+++++++++.<-.>+++++++.-------.-----.+++++++++++++.<-.>-.-------------------.+++++++++++++++++.<+.>-------------.++++++++++++.<+.>----------.++++.++++++++++++.<++.++++++.>+.-------.----.<.>-.

Si vous avez des problèmes pour la lecture du flag n'hésitez pas à contacter un des organisateurs.
 

## Solve possible : 
- Chercher l'origine de ce hash 

> Par exemple à l'aide de : https://www.dcode.fr/identification-chiffrement 

- Utiliser le lien pour télécharger la deuxième étape du challenge

> https://volumen.univ-ubs.fr/hlx17yrn7m

- Analyser l'image pour se rendre compte que le mot de passe à été cacher avec du LSB (voir coté gauche de l'image à l'aide de filtre)

> Avec https://www.aperisolve.com/ par exemple

- Extraire le mot de passe du zip avec un tool déjà fait ou faire le sien

> Avec https://github.com/adrg/lsbsteg ou https://gist.github.com/dhondta/d2151c82dcd9a610a7380df1c6a0272c (pas testé mais sûrement faisable)

> Pour un tool fait main : LSBSanta.py (Code fait par Fozl merci à lui pour l'autorisation de son code)

>Password : concealingwithLSBcanbemuchmorehardbutgg

- Extraire le fichier audio du zip et l'écouter jusqu'au bout pour se rendre compte d'un problème à la fin de l'audio

- Ouvrir le fichier audio et regarder son spectrogramme

> Utiliser audacity par exemple

## Indices :
1. Step 1 : Ce langage me détruit le cerveau
2. Step 2 : Il y a des pixels bizarre sur le coté gauche, il semblerait que leurs bits de poids faible soit modifié...
3. Step 2 : "adrg" a fait un tool plutôt pas mal
4. Step 3 : Cette étape est faisable avec audacity

## Flag : 
CATF{1T_W4S_FUN_R1GHT_P134S3_S4Y_Y3S}
