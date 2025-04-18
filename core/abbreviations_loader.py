import json

def load_abbreviations():
    with open('data/abrev.json', 'r', encoding='utf-8') as f:
        return json.load(f)