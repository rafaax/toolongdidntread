import gradio as gr
from core.summarizer import summarize_text, get_summary_params

def create_interface(tokenizer, model, examples):
    with gr.Blocks() as interface:
        gr.Markdown("## Sumarizador de texto em portugues com T5")
        gr.Markdown("### Insira o texto que deseja resumir e clique em 'Gerar Resumo'")
        gr.Markdown("### Ou selecione um exemplo pronto para carregar")

        with gr.Row():
            with gr.Column():
                exemplo_seletor = gr.Dropdown(
                    label="Exemplos Prontos",
                    choices=list(examples.keys()),
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
            fn=lambda x: examples[x],
            inputs=exemplo_seletor,
            outputs=input_text
        )
        
        btn.click(
            fn=lambda text, comp: summarize_text(text, comp, tokenizer, model),
            inputs=[input_text, complexidade],
            outputs=output_text
        )
    
    return interface