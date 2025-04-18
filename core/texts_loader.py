import json

def load_examples():
    with open('data/exemplos.json', 'r', encoding='utf-8') as f:
        return json.load(f)