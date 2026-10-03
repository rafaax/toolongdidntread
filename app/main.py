import argparse
from app.interface import create_interface
from core.model_loader import load_models
from core.texts_loader import load_examples

def main():
    parser = argparse.ArgumentParser(description="Sumarizador de textos em português com PTT5")
    parser.add_argument("--share", action="store_true", help="cria um link público temporário do Gradio (por padrão, roda só localmente)")
    args = parser.parse_args()

    tokenizer, model = load_models()
    examples = load_examples()
    
    interface = create_interface(tokenizer, model, examples)
    interface.launch(share=args.share, debug=True)

if __name__ == "__main__":
    main()