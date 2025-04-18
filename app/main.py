import gradio as gr
import json
from transformers import T5Tokenizer, T5ForConditionalGeneration

token_name = 'unicamp-dl/ptt5-base-portuguese-vocab'
model_name = 'phpaiola/ptt5-base-summ-xlsum'

tokenizer = T5Tokenizer.from_pretrained(token_name, legacy=False)
model_pt = T5ForConditionalGeneration.from_pretrained(model_name)

with open('exemplos.json', 'r', encoding='utf-8') as f: # carregar exemplos do arquivo JSON
    exemplos = json.load(f)


def sumarizar_texto(texto, complexidade):
    if len(texto.split()) < 30:
        return "Por favor, insira um texto mais longo (pelo menos 5-6 frases)" ## dependemos de um resumo relativamente ok para analisar e fazer a sumarização
    
    try:
        if complexidade == "Rápido":
            params = {
                'max_length': 150, # resposta mais curta ainda
                'min_length': 30, # resposta mais curta ainda
                'num_beams': 2, # 2 feixes para busca
                'no_repeat_ngram_size': 2, # evitar repetições
                'early_stopping': True # parar quando o resumo estiver completo
            }
        elif complexidade == "Balanceado":
            params = {
                'max_length': 200, # resposta mais curta
                'min_length': 50, # resposta mais curta
                'num_beams': 4, # 4 feixes para busca 
                'no_repeat_ngram_size': 3, # evitar repetições
                'early_stopping': True # mais feixes para busca
            }
        elif complexidade == "Detalhado":  
            params = {
                'max_length': 256, # resposta com uma extensão maior
                'min_length': 80, # resposta com uma extensão maior
                'num_beams': 6, # mais feixes para busca
                'no_repeat_ngram_size': 4, # evitar repetições
                'early_stopping': True, # parar quando o resumo estiver completo
                'length_penalty': 2.0 # penalizar resumos longos
            }
        
        inputs = tokenizer.encode(texto, max_length=512, truncation=True, return_tensors='pt')
        summary_ids = model_pt.generate(inputs, **params)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        return f"Erro ao sumarizar: {str(e)}"

def carregar_exemplo(exemplo):
    return exemplos[exemplo]

with gr.Blocks() as interface:
    gr.Markdown("## Sumarizador de texto em portugues com T5")
    gr.Markdown("### Insira o texto que deseja resumir e clique em 'Gerar Resumo'")
    gr.Markdown("### Ou selecione um exemplo pronto para carregar")

    with gr.Row():
        with gr.Column():
        
            exemplo_seletor = gr.Dropdown(
                label="Exemplos Prontos",
                choices=list(exemplos.keys()),
                value="Artigo Científico"
            )
            btn_carregar = gr.Button("Carregar Exemplo", variant="secondary")
            
        
            input_text = gr.Textbox(
                label="Texto para resumir",
                lines=10,
                placeholder="Digite seu texto aqui (mínimo 30 letras)"
            )
            
            
            with gr.Row():
                complexidade = gr.Radio(
                    label="Qualidade da Análise",
                    info="Tem influencia no tempo de resposta",
                    choices=["Rápido", "Balanceado", "Detalhado"],
                    value="Rápido"
                )
                btn = gr.Button("Gerar Resumo", variant="primary")
        
        with gr.Column():
            output_text = gr.Textbox(
                label="Resumo",
                lines=10,
                interactive=False
            )
    
    btn_carregar.click(
        fn=carregar_exemplo,
        inputs=exemplo_seletor,
        outputs=input_text
    )
    
    btn.click(
        fn=sumarizar_texto,
        inputs=[input_text, complexidade],
        outputs=output_text
    )

interface.launch(share=True, debug=True)