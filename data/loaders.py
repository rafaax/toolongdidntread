import json

def load_examples():
    with open('data/exemplos.json', 'r', encoding='utf-8') as f:
        return json.load(f)
    
def load_abbreviations():
    with open('data/exemplos.json', 'r', encoding='utf-8') as f:
        return json.load(f)