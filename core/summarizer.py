from core.abbreviations_loader import load_abbreviations
from core.abbreviation_expander import expand_abbreviations

abrev = load_abbreviations()
# informações do select de complexidades
def get_summary_params(complexidade): 
    params_map = {
        "Rápido": {
            'max_length': 150,
            'min_length': 30,
            'num_beams': 2,
            'no_repeat_ngram_size': 2,
            'early_stopping': True
        },
        "Balanceado": {
            'max_length': 200,
            'min_length': 50,
            'num_beams': 4,
            'no_repeat_ngram_size': 3,
            'early_stopping': True
        },
        "Detalhado": {
            'max_length': 256,
            'min_length': 80,
            'num_beams': 6,
            'no_repeat_ngram_size': 4,
            'early_stopping': True,
            'length_penalty': 2.0
        }
    }
    return params_map.get(complexidade, params_map["Rápido"])

# função que faz o sumarizador através do modelo
def summarize_text(texto, complexidade, tokenizer, model):
    if len(texto.split()) < 30:
        return "Por favor, insira um texto mais longo (pelo menos 5-6 frases)"
    
    texto = expand_abbreviations(texto, abrev)
    
    try:
        params = get_summary_params(complexidade)
        inputs = tokenizer.encode(texto, max_length=512, truncation=True, return_tensors='pt')
        summary_ids = model.generate(inputs, **params)
        return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        return f"Erro ao sumarizar: {str(e)}"