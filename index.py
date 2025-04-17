import gradio as gr
from transformers import pipeline
import unicodedata


summarization = pipeline("summarization", model="t5-large", tokenizer="t5-large")

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def processar_texto(texto):
    return f"Você digitou: {texto}"

def sumarizarTexto(texto):
    texto = remover_acentos(texto)
    prompt = f"sumarize: {texto}"
    output = summarization(prompt, do_sample=False)
    return output[0]['summary_text'] 


with gr.Blocks() as interface:
    with gr.Row():
        with gr.Column():
            entrada = gr.Textbox(label="Digite algo que iremos simplificar!")
            botao = gr.Button("Processar o texto")
        with gr.Column():
            saida = gr.Textbox(label="Texto simplificado")

    
    botao.click(fn=sumarizarTexto, inputs=entrada, outputs=saida)

interface.launch()