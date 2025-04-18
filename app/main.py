from app.interface import create_interface
from core.model_loader import load_models
from core.texts_loader import load_examples
from core.abbreviations_loader import load_abbreviations

def main():
    tokenizer, model = load_models()
    examples = load_examples()
    
    interface = create_interface(tokenizer, model, examples)
    interface.launch(share=True, debug=True)

if __name__ == "__main__":
    main()