# 🧠 PTT5 Text Summarizer - Brazilian Portuguese

Uma aplicação interativa de **sumarização abstrativa** de textos em **Português Brasileiro**, baseada no modelo [PTT5-base-summ-xlsum](https://huggingface.co/recogna-nlp/ptt5-base-summ-xlsum) da Hugging Face.

---

## ✨ Funcionalidades

- 🔤 Interface com [Gradio](https://gradio.app/) para inserção e visualização dos resumos
- 📉 Sumarização com diferentes **níveis de complexidade** (escolhido via botão de rádio)
- 🧹 Pré-processamento com **regex** e um **dicionário de abreviações**
- 🧪 Exemplos de uso em **JSON** disponíveis na interface para testes rápidos
- 🤖 Modelo fine-tuned para sumarização em Português Brasileiro

---

## Referência do Modelo

@InProceedings{ptt5summ_bracis,
  author="Paiola, Pedro H.
    and de Rosa, Gustavo H.
    and Papa, Jo{\~a}o P.",
  editor="Xavier-Junior, Jo{\~a}o Carlos
    and Rios, Ricardo Ara{\'u}jo",
  title="Deep Learning-Based Abstractive Summarization for Brazilian Portuguese Texts",
  booktitle="BRACIS 2022: Intelligent Systems",
  year="2022",
  publisher="Springer International Publishing",
  address="Cham",
  pages="479--493",
  isbn="978-3-031-21689-3"
}