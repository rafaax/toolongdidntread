import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess_and_expand(text, abbreviation_dict):
    
    tokens = word_tokenize(text, language='portuguese') # Tokeniza o texto
    stop_words = set(stopwords.words('portuguese'))

    processed_tokens = []

    for token in tokens:
        token_lower = token.lower()

        
        if token_lower in abbreviation_dict: # Expande abreviações
            expansion = abbreviation_dict[token_lower]

            if token.istitle():
                expansion = expansion.capitalize()
            elif token.isupper():
                expansion = expansion.upper()

            processed_tokens.append(expansion)
        else:  # Mantém a palavra se não for uma stopword ou for pontuação
            if token_lower not in stop_words or not token.isalpha():
                processed_tokens.append(token)

    return ' '.join(processed_tokens)