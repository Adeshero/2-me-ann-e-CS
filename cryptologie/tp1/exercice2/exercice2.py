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
    
    return f" le message chiffré est:{cypher}"

print(vigenere("mastercsuemf", "clefvigenere"))