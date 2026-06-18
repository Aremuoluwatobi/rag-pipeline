import gradio as gr
from AI_response import ai_response
from metadata import get_available_pdfs
from ingestion import ingest_pipeline
from retrieval import retrieve_data

try:
    retrieve_data("test")
except Exception:
    ingest_pipeline()


def chat_fn(message, history):
    return ai_response(message)


pdf_list = get_available_pdfs()


with gr.Blocks() as demo:

    gr.Markdown("## 📘 MyScholar AI")

    with gr.Accordion("📂 Available Documents (Click to expand)", open=False):
        gr.Markdown("\n".join([f"- {pdf}" for pdf in pdf_list]))

    gr.Markdown("---")

    chatbot = gr.Chatbot()

    def respond(message, history):
        answer = chat_fn(message, history)
        history.append((message, answer))
        return "", history

    with gr.Row():
        msg = gr.Textbox(
            show_label=False,
            placeholder="Ask your question..."
        )
        btn = gr.Button("Send")

    btn.click(respond, [msg, chatbot], [msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch(server_name="0.0.0.0", server_port=7860)
