import re

def expand(text, dict):
    for abbrev, expansao in dict.items():
        text = re.sub(abbrev, expansao, text, flags=re.IGNORECASE)
    return text

# texto_original = "vc sabe qdo ela vem? blz, tb vou cmg. flw!"
# texto_expandido = expandir_abreviacoes(texto_original)

# print("Original:", texto_original)
# print("Expandido:", texto_expandido)
