import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration

token_name = 'unicamp-dl/ptt5-base-portuguese-vocab'
model_name = 'phpaiola/ptt5-base-summ-xlsum'

tokenizer = T5Tokenizer.from_pretrained(token_name)
model_pt = T5ForConditionalGeneration.from_pretrained(model_name)

exemplos = {
    "Artigo Científico": """
A inteligência artificial (IA) tem revolucionado diversos setores, desde a medicina até o entretenimento. 
Com algoritmos cada vez mais avançados, máquinas são capazes de aprender padrões, tomar decisões e até 
mesmo simular emoções humanas. Na área da saúde, por exemplo, sistemas de IA ajudam no diagnóstico de 
doenças com precisão superior à de muitos profissionais. Empresas também utilizam chatbots para 
atendimento ao cliente, reduzindo custos e aumentando a eficiência. Por outro lado, o avanço da IA 
levanta questões éticas e preocupações. Muitos temem que a automação substitua empregos tradicionais, 
aumentando o desemprego. Além disso, há debates sobre privacidade, já que sistemas de reconhecimento 
facial e análise de dados podem ser usados para vigilância em massa. Especialistas argumentam que é 
necessário regulamentar o uso da IA para garantir que os benefícios superem os riscos.
""",
    "Notícia Política": """
O presidente anunciou hoje um novo pacote de medidas econômicas para estimular o crescimento do país. 
Entre as principais iniciativas estão a redução de impostos para pequenas empresas e o aumento do 
investimento em infraestrutura. A oposição, no entanto, critica as medidas, alegando que beneficiam 
apenas setores específicos da economia e não resolvem os problemas estruturais. Analistas econômicos 
dividem-se sobre o impacto real das medidas, com alguns prevendo um crescimento moderado e outros 
alertando para o risco de aumento da inflação. O pacote será votado no congresso na próxima semana.
""",
    "Resenha Literária": """
O novo romance do autor consagrado mistura elementos de ficção científica com uma profunda reflexão 
sobre a condição humana. A narrativa segue três personagens em tempos distintos cujas vidas se 
entrelaçam de maneira surpreendente. A prosa poética e as descrições vívidas transportam o leitor para 
mundos alternativos enquanto exploram temas universais como amor, perda e redenção. Embora alguns 
críticos considerem o ritmo lento em certos momentos, a maioria concorda que se trata de uma obra 
madura e emocionante, possivelmente a melhor do autor até agora.
"""
}

def sumarizar_texto(texto, complexidade):
    if len(texto.split()) < 30:
        return "Por favor, insira um texto mais longo (pelo menos 5-6 frases)"
    
    try:
        if complexidade == "Rápido":
            params = {
                'max_length': 150,
                'min_length': 30,
                'num_beams': 2,
                'no_repeat_ngram_size': 2,
                'early_stopping': True
            }
        elif complexidade == "Balanceado":
            params = {
                'max_length': 200,
                'min_length': 50,
                'num_beams': 4,
                'no_repeat_ngram_size': 3,
                'early_stopping': True
            }
        else:  # "Detalhado"
            params = {
                'max_length': 256,
                'min_length': 80,
                'num_beams': 6,
                'no_repeat_ngram_size': 4,
                'early_stopping': True,
                'length_penalty': 2.0
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
    gr.Markdown("## ✂️ Sumarizador Avançado de Texto em Português (T5)")
    
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
                placeholder="Digite ou cole seu texto aqui (mínimo 5-6 frases)..."
            )
            
            
            with gr.Row():
                complexidade = gr.Radio(
                    label="Nível de Análise",
                    choices=["Rápido", "Balanceado", "Detalhado"],
                    value="Balanceado"
                )
                btn = gr.Button("Gerar Resumo", variant="primary")
        
        with gr.Column():
            output_text = gr.Textbox(
                label="Resumo",
                lines=10,
                interactive=False
            )
    
    # Ações
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

interface.launch()