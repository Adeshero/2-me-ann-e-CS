import string 

def cesar1(chaine:str="Bonjour",decalage:int= 2):
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
    

def cesar2(chaine:str="Bonjour" , decalage:int=2):
    """_summary_

    Args:
        chaine (str, optional): _description_. Defaults to "Bonjour".
        decalage (int, optional): _description_. Defaults to 2.
        
        Ce code effectu un cryptage en cesar 
    """
    
    alphabet= string.printable
    
    list_cypher=[]
    
    for i in chaine:
        if i in alphabet:
            indexe=alphabet.index(i)
            new_decalage = (indexe + decalage) % len(alphabet)
            list_cypher.append(alphabet[new_decalage])
        else:
            list_cypher.append(i)
    cypher=''.join(list_cypher)
    return f"le texte initial est {chaine} et le texte chiffrer en Cesar est {cypher}"
    
            
    
if __name__ =="__main__":
    print(cesar2(" Je vais te manger", 6))
    