import gradio as gr
from AI_response import ai_response
from metadata import get_available_pdfs
from vectordb import clear_database
from ingestion import download_documents, ingest_pipeline

import os
from dotenv import load_dotenv
from huggingface_hub import login

load_dotenv()

token = os.getenv("HF_TOKEN")
login(token=token)

download_documents()
clear_database()
ingest_pipeline()


def chat_fn(message, history):
    return ai_response(message)


pdf_list = get_available_pdfs()

with gr.Blocks(
    theme=gr.themes.Base(
        primary_hue="blue",
        neutral_hue="slate",
    ),
    title="MyScholar AI",
    css="""
    body, .gradio-container { background-color: #0f172a !important; }
    .contain { background-color: #0f172a !important; }
    .panel, .form { background-color: #1e293b !important; }
    .message.user > div { background-color: #2563eb !important; color: white !important; }
    .message.bot > div { background-color: #334155 !important; color: white !important; }
    .svelte-button, button.primary { background-color: #38bdf8 !important; color: #0f172a !important; }
    textarea, input { background-color: #1e293b !important; color: white !important; border-color: #334155 !important; }
    """
) as demo:

    gr.Markdown("## 📘 MyScholar AI")

    with gr.Accordion("📂 Available Documents (Click to expand)", open=False):
        gr.Markdown("\n".join([f"- {pdf}" for pdf in pdf_list]))

    gr.Markdown("---")

    chatbot = gr.Chatbot(height=450, show_label=False)

    def respond(message, history):
        answer = chat_fn(message, history)
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": answer})
        return "", history

    with gr.Row():
        msg = gr.Textbox(
            show_label=False,
            placeholder="Ask your question...",
            scale=4
        )
        btn = gr.Button("Send", scale=1, variant="primary")

    btn.click(respond, [msg, chatbot], [msg, chatbot])
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch(server_name="0.0.0.0", server_port=7860)
