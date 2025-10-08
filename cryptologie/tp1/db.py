import random
from enum import Enum
    

def get_randomly():
    liste_de_langues=[]
    for key in langues_unicode.keys():
        liste_de_langues.append(key)
    choix= random.choice(liste_de_langues)
    return choix






def choix_de_langue(langage :str ):
    for key,detail in langues_unicode.items():
        if key == langage:
            langue=random.choice(detail["plages"])
    return langue
            

langues_unicode = {
    # ========== LANGUES EUROPÉENNES (LATIN) ==========
    "Français": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Romane)",
        "locuteurs": "280 millions"
    },
    "Anglais": {
        "plages": [
            ("Latin de base", "0020", "007F"),
        ],
        "famille": "Indo-européenne (Germanique)",
        "locuteurs": "1,5 milliard"
    },
    "Espagnol": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Romane)",
        "locuteurs": "500 millions"
    },
    "Portugais": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Romane)",
        "locuteurs": "260 millions"
    },
    "Italien": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Romane)",
        "locuteurs": "85 millions"
    },
    "Allemand": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Germanique)",
        "locuteurs": "130 millions"
    },
    "Néerlandais": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Germanique)",
        "locuteurs": "25 millions"
    },
    "Polonais": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "45 millions"
    },
    "Tchèque": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "13 millions"
    },
    "Hongrois": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Ouralienne",
        "locuteurs": "13 millions"
    },
    "Roumain": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Romane)",
        "locuteurs": "24 millions"
    },
    "Turc": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Turcique",
        "locuteurs": "80 millions"
    },
    "Vietnamien": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
            ("Latin étendu-B", "0180", "024F"),
            ("Latin étendu additionnel", "1E00", "1EFF"),
        ],
        "famille": "Austroasiatique",
        "locuteurs": "95 millions"
    },
    "Suédois": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Germanique)",
        "locuteurs": "13 millions"
    },
    "Norvégien": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Germanique)",
        "locuteurs": "5 millions"
    },
    "Danois": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Germanique)",
        "locuteurs": "6 millions"
    },
    "Finnois": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Ouralienne",
        "locuteurs": "5 millions"
    },
    "Islandais": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Germanique)",
        "locuteurs": "350 000"
    },
    "Croate": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "7 millions"
    },
    "Slovène": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "2,5 millions"
    },
    "Albanais": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Albanaise)",
        "locuteurs": "8 millions"
    },
    "Estonien": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Ouralienne",
        "locuteurs": "1,1 million"
    },
    "Letton": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Balte)",
        "locuteurs": "1,7 million"
    },
    "Lituanien": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Balte)",
        "locuteurs": "3 millions"
    },
    "Slovaque": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "5 millions"
    },
    "Maltais": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Afro-asiatique (Sémitique)",
        "locuteurs": "520 000"
    },
    "Gallois": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Celtique)",
        "locuteurs": "900 000"
    },
    "Irlandais": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Indo-européenne (Celtique)",
        "locuteurs": "1,8 million"
    },
    "Basque": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Isolat",
        "locuteurs": "750 000"
    },
    "Catalan": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Romane)",
        "locuteurs": "10 millions"
    },
    "Galicien": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin-1 Supplément", "0080", "00FF"),
        ],
        "famille": "Indo-européenne (Romane)",
        "locuteurs": "2,4 millions"
    },

    # ========== LANGUES GRECQUES ==========
    "Grec": {
        "plages": [
            ("Grec et copte", "0370", "03FF"),
            ("Grec étendu", "1F00", "1FFF"),
        ],
        "famille": "Indo-européenne (Hellénique)",
        "locuteurs": "13 millions"
    },

    # ========== LANGUES CYRILLIQUES ==========
    "Russe": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
            ("Cyrillique supplément", "0500", "052F"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "258 millions"
    },
    "Ukrainien": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "40 millions"
    },
    "Biélorusse": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "7 millions"
    },
    "Bulgare": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "8 millions"
    },
    "Serbe": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "12 millions"
    },
    "Macédonien": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
        ],
        "famille": "Indo-européenne (Slave)",
        "locuteurs": "2 millions"
    },
    "Kazakh": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
            ("Cyrillique supplément", "0500", "052F"),
        ],
        "famille": "Turcique",
        "locuteurs": "13 millions"
    },
    "Kirghize": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
        ],
        "famille": "Turcique",
        "locuteurs": "4 millions"
    },
    "Tadjik": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
        ],
        "famille": "Indo-européenne (Iranienne)",
        "locuteurs": "8 millions"
    },
    "Mongol": {
        "plages": [
            ("Cyrillique", "0400", "04FF"),
            ("Mongol", "1800", "18AF"),
        ],
        "famille": "Mongole",
        "locuteurs": "5 millions"
    },

    # ========== LANGUES DU MOYEN-ORIENT ==========
    "Arabe": {
        "plages": [
            ("Arabe", "0600", "06FF"),
            ("Arabe supplément", "0750", "077F"),
            ("Arabe formes de présentation-A", "FB50", "FDFF"),
            ("Arabe formes de présentation-B", "FE70", "FEFF"),
        ],
        "famille": "Afro-asiatique (Sémitique)",
        "locuteurs": "420 millions"
    },
    "Persan": {
        "plages": [
            ("Arabe", "0600", "06FF"),
            ("Arabe supplément", "0750", "077F"),
        ],
        "famille": "Indo-européenne (Iranienne)",
        "locuteurs": "110 millions"
    },
    "Ourdou": {
        "plages": [
            ("Arabe", "0600", "06FF"),
            ("Arabe supplément", "0750", "077F"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "170 millions"
    },
    "Pachto": {
        "plages": [
            ("Arabe", "0600", "06FF"),
            ("Arabe supplément", "0750", "077F"),
        ],
        "famille": "Indo-européenne (Iranienne)",
        "locuteurs": "60 millions"
    },
    "Kurde": {
        "plages": [
            ("Arabe", "0600", "06FF"),
            ("Latin de base", "0020", "007F"),
        ],
        "famille": "Indo-européenne (Iranienne)",
        "locuteurs": "30 millions"
    },
    "Ouïghour": {
        "plages": [
            ("Arabe", "0600", "06FF"),
            ("Arabe supplément", "0750", "077F"),
        ],
        "famille": "Turcique",
        "locuteurs": "10 millions"
    },
    "Hébreu": {
        "plages": [
            ("Hébreu", "0590", "05FF"),
        ],
        "famille": "Afro-asiatique (Sémitique)",
        "locuteurs": "9 millions"
    },
    "Yiddish": {
        "plages": [
            ("Hébreu", "0590", "05FF"),
        ],
        "famille": "Indo-européenne (Germanique)",
        "locuteurs": "1,5 million"
    },
    "Arménien": {
        "plages": [
            ("Arménien", "0530", "058F"),
        ],
        "famille": "Indo-européenne (Arménienne)",
        "locuteurs": "7 millions"
    },
    "Géorgien": {
        "plages": [
            ("Géorgien", "10A0", "10FF"),
        ],
        "famille": "Kartvélienne",
        "locuteurs": "4 millions"
    },
    "Syriaque": {
        "plages": [
            ("Syriaque", "0700", "074F"),
        ],
        "famille": "Afro-asiatique (Sémitique)",
        "locuteurs": "100 000 (liturgique)"
    },

    # ========== LANGUES D'ASIE DE L'EST ==========
    "Chinois": {
        "plages": [
            ("CJK Idéographes unifiés", "4E00", "9FFF"),
            ("CJK Extension A", "3400", "4DBF"),
            ("CJK Extension B", "20000", "2A6DF"),
        ],
        "famille": "Sino-tibétaine",
        "locuteurs": "1,3 milliard"
    },
    "Japonais": {
        "plages": [
            ("Hiragana", "3040", "309F"),
            ("Katakana", "30A0", "30FF"),
            ("CJK Idéographes unifiés", "4E00", "9FFF"),
        ],
        "famille": "Japonique",
        "locuteurs": "125 millions"
    },
    "Coréen": {
        "plages": [
            ("Hangul Jamo", "1100", "11FF"),
            ("Hangul", "AC00", "D7AF"),
            ("Hangul Jamo étendu-A", "A960", "A97F"),
            ("Hangul Jamo étendu-B", "D7B0", "D7FF"),
        ],
        "famille": "Isolat (ou Koréanique)",
        "locuteurs": "80 millions"
    },

    # ========== LANGUES D'ASIE DU SUD-EST ==========
    "Thaï": {
        "plages": [
            ("Thaï", "0E00", "0E7F"),
        ],
        "famille": "Tai-kadai",
        "locuteurs": "60 millions"
    },
    "Lao": {
        "plages": [
            ("Lao", "0E80", "0EFF"),
        ],
        "famille": "Tai-kadai",
        "locuteurs": "30 millions"
    },
    "Khmer": {
        "plages": [
            ("Khmer", "1780", "17FF"),
        ],
        "famille": "Austroasiatique",
        "locuteurs": "16 millions"
    },
    "Birman": {
        "plages": [
            ("Birman (Myanmar)", "1000", "109F"),
            ("Myanmar étendu-A", "AA60", "AA7F"),
            ("Myanmar étendu-B", "A9E0", "A9FF"),
        ],
        "famille": "Sino-tibétaine",
        "locuteurs": "33 millions"
    },
    "Javanais": {
        "plages": [
            ("Javanais", "A980", "A9DF"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "82 millions"
    },
    "Balinais": {
        "plages": [
            ("Balinais", "1B00", "1B7F"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "3,5 millions"
    },
    "Soundanais": {
        "plages": [
            ("Soundanais", "1B80", "1BBF"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "42 millions"
    },
    "Buginais": {
        "plages": [
            ("Buginais", "1A00", "1A1F"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "5 millions"
    },
    "Tagalog": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Tagalog (Baybayin)", "1700", "171F"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "45 millions"
    },

    # ========== LANGUES D'ASIE DU SUD (INDE) ==========
    "Hindi": {
        "plages": [
            ("Devanagari", "0900", "097F"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "600 millions"
    },
    "Sanskrit": {
        "plages": [
            ("Devanagari", "0900", "097F"),
            ("Grantha", "11300", "1137F"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "25 000 (classique)"
    },
    "Marathi": {
        "plages": [
            ("Devanagari", "0900", "097F"),
            ("Modi", "11600", "1165F"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "83 millions"
    },
    "Népalais": {
        "plages": [
            ("Devanagari", "0900", "097F"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "16 millions"
    },
    "Bengali": {
        "plages": [
            ("Bengali", "0980", "09FF"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "265 millions"
    },
    "Assamais": {
        "plages": [
            ("Bengali", "0980", "09FF"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "15 millions"
    },
    "Pendjabi": {
        "plages": [
            ("Gurmukhi", "0A00", "0A7F"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "125 millions"
    },
    "Gujarati": {
        "plages": [
            ("Gujarati", "0A80", "0AFF"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "60 millions"
    },
    "Oriya": {
        "plages": [
            ("Oriya (Odia)", "0B00", "0B7F"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "45 millions"
    },
    "Tamoul": {
        "plages": [
            ("Tamoul", "0B80", "0BFF"),
        ],
        "famille": "Dravidienne",
        "locuteurs": "80 millions"
    },
    "Telugu": {
        "plages": [
            ("Telugu", "0C00", "0C7F"),
        ],
        "famille": "Dravidienne",
        "locuteurs": "93 millions"
    },
    "Kannada": {
        "plages": [
            ("Kannada", "0C80", "0CFF"),
        ],
        "famille": "Dravidienne",
        "locuteurs": "50 millions"
    },
    "Malayalam": {
        "plages": [
            ("Malayalam", "0D00", "0D7F"),
        ],
        "famille": "Dravidienne",
        "locuteurs": "38 millions"
    },
    "Cinghalais": {
        "plages": [
            ("Cinghalais", "0D80", "0DFF"),
        ],
        "famille": "Indo-européenne (Indo-aryenne)",
        "locuteurs": "17 millions"
    },
    "Tibétain": {
        "plages": [
            ("Tibétain", "0F00", "0FFF"),
        ],
        "famille": "Sino-tibétaine",
        "locuteurs": "6 millions"
    },

    # ========== LANGUES AFRICAINES ==========
    "Amharique": {
        "plages": [
            ("Éthiopien (Ge'ez)", "1200", "137F"),
            ("Éthiopien supplément", "1380", "139F"),
        ],
        "famille": "Afro-asiatique (Sémitique)",
        "locuteurs": "57 millions"
    },
    "Tigrigna": {
        "plages": [
            ("Éthiopien (Ge'ez)", "1200", "137F"),
        ],
        "famille": "Afro-asiatique (Sémitique)",
        "locuteurs": "9 millions"
    },
    "Berbère": {
        "plages": [
            ("Tifinagh", "2D30", "2D7F"),
        ],
        "famille": "Afro-asiatique (Berbère)",
        "locuteurs": "30 millions"
    },
    "Somali": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Osmanya", "10480", "104AF"),
        ],
        "famille": "Afro-asiatique (Couchitique)",
        "locuteurs": "21 millions"
    },
    "Swahili": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Niger-Congo (Bantoue)",
        "locuteurs": "200 millions"
    },
    "Haoussa": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Afro-asiatique (Tchadique)",
        "locuteurs": "80 millions"
    },
    "Yoruba": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Niger-Congo",
        "locuteurs": "45 millions"
    },
    "Zoulou": {
        "plages": [
            ("Latin de base", "0020", "007F"),
        ],
        "famille": "Niger-Congo (Bantoue)",
        "locuteurs": "27 millions"
    },

    # ========== LANGUES AMÉRINDIENNES ==========
    "Cherokee": {
        "plages": [
            ("Cherokee", "13A0", "13FF"),
        ],
        "famille": "Iroquoienne",
        "locuteurs": "2 000"
    },
    "Inuktitut": {
        "plages": [
            ("Syllabaire canadien autochtone", "1400", "167F"),
        ],
        "famille": "Eskimo-aléoute",
        "locuteurs": "40 000"
    },
    "Cri": {
        "plages": [
            ("Syllabaire canadien autochtone", "1400", "167F"),
        ],
        "famille": "Algonquienne",
        "locuteurs": "117 000"
    },
    "Ojibwé": {
        "plages": [
            ("Syllabaire canadien autochtone", "1400", "167F"),
        ],
        "famille": "Algonquienne",
        "locuteurs": "50 000"
    },

    # ========== LANGUES OCÉANIENNES ==========
    "Maori": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "185 000"
    },
    "Hawaïen": {
        "plages": [
            ("Latin de base", "0020", "007F"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "24 000"
    },
    "Samoan": {
        "plages": [
            ("Latin de base", "0020", "007F"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "510 000"
    },
    "Tongan": {
        "plages": [
            ("Latin de base", "0020", "007F"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "187 000"
    },

    # ========== AUTRES LANGUES ==========
    "Esperanto": {
        "plages": [
            ("Latin de base", "0020", "007F"),
            ("Latin étendu-A", "0100", "017F"),
        ],
        "famille": "Langue construite",
        "locuteurs": "2 millions (L2)"
    },
    "Malais-Indonésien": {
        "plages": [
            ("Latin de base", "0020", "007F"),
        ],
        "famille": "Austronésienne",
        "locuteurs": "290 millions"
    },
}