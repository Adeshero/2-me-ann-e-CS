**Algorithme de Vigenère**

Dans cet exercice je doit ecrire un code python pour réaliser un programme permettant de chiffrer/déchiffrer une chaîne de caractère selon l'algorithme de Vignère.Le message à chiffré <<mastercsuemf>>,la clé <<clefvigenere>>

pour ce faire je vais :
- creer une fonction qui prend en parametre le méssage à chiffrer et la clé de chiffrement et retourne le message chiffré  
  - pour ce faire:
    - repeter la clé jusqu'a atteindre la longueur du message à chiffrer 
    - fair une boucle qui parcoure en parallèle à la fois le méssage à chiffrer et la clé de chiffrement 
    - recuperer les positions de chaque caractère du message et de la clé 
    - calculer la nouvelle de chaque cryptogramme 
    - retourner le nouveau message chiffré
- creer une fonction de déchiffrement. Pour ce faire :
  - repéter le même processuce que le chiffrement à l'exception de calcule  du décalahge ou cette fois-ci il faut faire une soustration 
  - retourner le message chiffré 
