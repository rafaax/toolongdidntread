import re

def preprocess_and_expand(text, abbreviation_dict):
    text = re.sub(r'https?://\S+|www\.\S+', '', text) # Remove URLs
    
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # Emojis emotivos
        u"\U0001F300-\U0001F5FF"  # Símbolos e pictogramas
        u"\U0001F680-\U0001F6FF"  # Transporte e mapas
        u"\U0001F1E0-\U0001F1FF"  # Bandeiras
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)

    
    for abbrev, expansion in abbreviation_dict.items(): # Expande abreviações baseando se no dicionario criado, que está no data/abrev.json
        pattern = re.compile(rf'\b{re.escape(abbrev)}\b', flags=re.IGNORECASE)
        
        def replace(match):
            word = match.group(0)
            if word.isupper():
                return expansion.upper()
            elif word[0].isupper():
                return expansion.capitalize()
            else:
                return expansion.lower()
        
        text = pattern.sub(replace, text)

    return text.strip()
