import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Dicionário de abreviações (personalizável)
abreviacoes = {
    r'\bqdo\b': 'quando',
    r'\bblz\b': 'beleza',
    r'\bvc\b': 'você',
    r'\btb\b': 'também',
    r'\bpq\b': 'porque',
    r'\bcmg\b': 'comigo',
    r'\bflw\b': 'falou',
    r'\bvdd\b': 'verdade',
    r'\bmds\b': 'meu deus',
    r'\bpdc\b': 'pode crer'
}

# Função para expandir abreviações usando regex + dicionário
def expandir_abreviacoes(texto):
    for abbrev, expansao in abreviacoes.items():
        texto = re.sub(abbrev, expansao, texto, flags=re.IGNORECASE)
    return texto

# Exemplo de uso
texto_original = "vc sabe qdo ela vem? blz, tb vou cmg. flw!"
texto_expandido = expandir_abreviacoes(texto_original)

print("Original:", texto_original)
print("Expandido:", texto_expandido)
