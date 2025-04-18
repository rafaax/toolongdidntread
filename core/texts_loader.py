import json

def load_examples():
    with open('data/texts.json', 'r', encoding='utf-8') as f:
        return json.load(f)