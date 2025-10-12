import string 


def vigenere (message:str, key:str ):
    
    alphabet =[ chr(i) for i in range(ord('A'),ord('z') +1)  if i not in range(91,97)  ]
    alphabet.append(' ')
    
    cypher_list= []
    
    key_repeated =(key * (len(message) // len(key) + 1))[:len(message)]
    
    for caractere_message,caractere_key in zip ( message,key_repeated) :
        
        #position du caractere dans l'alphabet 
        pos_message = alphabet.index(caractere_message)
        pos_key = alphabet.index(caractere_key)
        
        #Calcul du décalage et du nouveau caractère 
        nouvelle_position = (pos_message + pos_key) % len(alphabet)
        cypher_caractere = alphabet[nouvelle_position]
        
        cypher_list.append(cypher_caractere)
        
    
    cypher=''.join(cypher_list)
    
    return cypher


def vigenere_dechiffrer(message_chiffre: str, key: str):
    alphabet = [chr(i) for i in range(ord('A'), ord('z') + 1) if i not in range(91, 97)]
    alphabet.append(' ')
    
    message_clair_list = []
    
    key_repeated = (key * (len(message_chiffre) // len(key) + 1))[:len(message_chiffre)]
    
    for caractere_chiffre, caractere_key in zip(message_chiffre, key_repeated):
        
        # Position du caractere dans l'alphabet 
        pos_chiffre = alphabet.index(caractere_chiffre)
        pos_key = alphabet.index(caractere_key)
        
        # Calcul inverse : on soustrait au lieu d'additionner
        position_originale = (pos_chiffre - pos_key) % len(alphabet)
        caractere_clair = alphabet[position_originale]
        
        message_clair_list.append(caractere_clair)
    
    message_clair = ''.join(message_clair_list)
    return message_clair
if __name__ == "__main__":
    print("-" * 60)
    message1 = "mastercsuemf"
    cle1 = "clefvigenere"
    print(f"Message original  : {message1}")
    print(f"Clé utilisée      : {cle1}")
    
    chiffre1 = vigenere(message1, cle1)
    print(f"Message chiffré   : {chiffre1}")
    
    dechiffre1 = vigenere_dechiffrer(chiffre1, cle1)
    print(f"Message déchiffré : {dechiffre1}")
    print(f"Vérification      : {' SUCCÈS' if dechiffre1 == message1 else ' ÉCHEC'}")
    print()
    
    
