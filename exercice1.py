def cesar(chaine:str="Bonjour",decalage:int= 2):
    '''
        Le but de cet exercice est de réaliser un programme permettant de chiffrer/ déchiffrer une chaîne de caractère
selon la méthode de césar. Le décalage est un paramètre du programme.
    '''
    alphabet =[ chr(i) for i in range(ord('A'),ord('z') +1)  if i not in range(91,97)  ]
    alphabet.append(' ')
    cypher=[]
    
    for i in chaine :
        if i in alphabet:
            j = alphabet.index(i)
            nouv_decalage = (j+decalage) % (len(alphabet))
            cypher.append(alphabet[nouv_decalage]) 
    
    text_chiffre= ''.join(cypher)
    
    return f"le texte initial est {chaine} \n le texte chiffrer en Cesar est {text_chiffre}"
    

if __name__ =="__main__":
    print(cesar(" Bonjour tout le monde ", 3))
    