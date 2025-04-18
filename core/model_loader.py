from transformers import T5Tokenizer, T5ForConditionalGeneration

def load_models():
    token_name = 'unicamp-dl/ptt5-base-portuguese-vocab'
    model_name = 'phpaiola/ptt5-base-summ-xlsum'
    
    tokenizer = T5Tokenizer.from_pretrained(token_name, legacy=False)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    
    return tokenizer, model