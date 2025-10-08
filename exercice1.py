import string 
from enum import Enum
from db import get_randomly,choix_de_langue

class base(Enum):
    FRANCAIS="francais"
    ANGLAIS ="anglais"
    

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

def cesar3(chaine: str = "Bonjour", decalage: int = 2, langue: str = None):
    """
    Chiffre une chaîne avec le chiffrement César en utilisant les plages Unicode.
    
    Args:
        chaine: La chaîne à chiffrer
        decalage: Le décalage à appliquer (peut être négatif pour déchiffrer)
        langue: La langue à utiliser (ex: "Français", "Arabe", etc.). 
                Si None, utilise une langue aléatoire
    
    Returns:
        str: La chaîne chiffrée
    """
    # Si pas de langue spécifiée, en choisir une aléatoirement
    if langue is None:
        langue = get_randomly()
    
    # Obtenir la plage Unicode pour cette langue
    plage_info = choix_de_langue(langue)
    nom_plage, debut_hex, fin_hex = plage_info
    
    # Convertir les codes hexadécimaux en entiers
    debut = int(debut_hex, 16)
    fin = int(fin_hex, 16)
    taille_plage = fin - debut + 1
    
    resultat = []
    
    for caractere in chaine:
        code = ord(caractere)
        
        # Vérifier si le caractère est dans la plage Unicode choisie
        if debut <= code <= fin:
            # Appliquer le décalage avec wrapping dans la plage
            nouveau_code = debut + ((code - debut + decalage) % taille_plage)
            resultat.append(chr(nouveau_code))
        else:
            # Si le caractère n'est pas dans la plage, le laisser tel quel
            resultat.append(caractere)
    
    return ''.join(resultat)


# Fonction utilitaire pour déchiffrer
def dechiffrer_cesar(chaine: str, decalage: int, version: int = 3, langue: str = None):
    """
    Fonction universelle pour déchiffrer une chaîne chiffrée avec n'importe quelle version de César.
    
    Args:
        chaine: La chaîne chiffrée à déchiffrer
        decalage: Le décalage utilisé lors du chiffrement
        version: La version de César à utiliser (1, 2 ou 3). Défaut: 3
        langue: La langue pour cesar3 uniquement (ex: "Français", "Arabe", etc.)
    
    Returns:
        str: La chaîne déchiffrée (pour cesar3) ou le message complet (pour cesar1 et cesar2)
    """
    if version == 1:
        # Déchiffrer avec cesar1 (alphabet A-Z + a-z + espace)
        alphabet = [chr(i) for i in range(ord('A'), ord('z') + 1) if i not in range(91, 97)]
        alphabet.append(' ')
        decypher = []
        
        for i in chaine:
            if i in alphabet:
                j = alphabet.index(i)
                nouv_decalage = (j - decalage) % (len(alphabet))
                decypher.append(alphabet[nouv_decalage])
        
        text_dechiffre = ''.join(decypher)
        return f"le texte chiffré est {chaine} \n le texte déchiffré en Cesar est {text_dechiffre}"
    
    elif version == 2:
        # Déchiffrer avec cesar2 (string.printable)
        alphabet = string.printable
        list_decypher = []
        
        for i in chaine:
            if i in alphabet:
                indexe = alphabet.index(i)
                new_decalage = (indexe - decalage) % len(alphabet)
                list_decypher.append(alphabet[new_decalage])
            else:
                list_decypher.append(i)
        
        decypher = ''.join(list_decypher)
        return f"le texte chiffré est {chaine} et le texte déchiffré en Cesar est {decypher}"
    
    elif version == 3:
        # Déchiffrer avec cesar3 (plages Unicode)
        return cesar3(chaine, -decalage, langue)
    
    else:
        raise ValueError("La version doit être 1, 2 ou 3")


# Exemple d'utilisation
if __name__ == "__main__":
    print("=" * 60)
    print("TEST CESAR1")
    print("=" * 60)
    message1 = "Bonjour"
    print(cesar1(message1, 3))
    chiffre1 = "Erqmrxu"  # Résultat du chiffrement
    print(dechiffrer_cesar(chiffre1, 3, version=1))
    
    print("\n" + "=" * 60)
    print("TEST CESAR2")
    print("=" * 60)
    message2 = "Hello World"
    print(cesar2(message2, 5))
    chiffre2 = "Mjqqt%\\twqi"  # Résultat du chiffrement
    print(dechiffrer_cesar(chiffre2, 5, version=2))
    
    print("\n" + "=" * 60)
    print("TEST CESAR3")
    print("=" * 60)
    message3 = "Bonjour le monde!"
    print(f"Message original: {message3}")
    
    chiffre3 = cesar3(message3, 3, "Français")
    print(f"Message chiffré (décalage +3): {chiffre3}")
    
    dechiffre3 = dechiffrer_cesar(chiffre3, 3, version=3, langue="Français")
    print(f"Message déchiffré: {dechiffre3}")
    
    print("\n" + "=" * 60)
    print("TEST CESAR3 - Langue aléatoire")
    print("=" * 60)
    message4 = "Test"
    langue_choisie = get_randomly()
    print(f"Langue choisie aléatoirement: {langue_choisie}")
    
    chiffre4 = cesar3(message4, 7, langue_choisie)
    print(f"Message original: {message4}")
    print(f"Message chiffré: {chiffre4}")
    
    dechiffre4 = dechiffrer_cesar(chiffre4, 7, version=3, langue=langue_choisie)
    print(f"Message déchiffré: {dechiffre4}")