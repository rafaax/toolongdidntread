import re

def expand_abbreviations(text, abbreviation_dict):
    for abbrev, expansion in abbreviation_dict.items():
        try:
            pattern = re.compile(abbrev, flags=re.IGNORECASE)
            text = pattern.sub(expansion, text)
        except re.error as e:
            print(f"Erro no padrão regex '{abbrev}': {str(e)}")
            continue  # Pula padrões inválidos
            
    return text