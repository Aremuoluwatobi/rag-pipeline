import gradio as gr
import sys
import platform
import pkg_resources
from AI_response import ai_response
from metadata import get_available_pdfs
from ingestion import ingest_pipeline
from retrieval import retrieve_data


print("=" * 60)
print("PYTHON VERSION:", sys.version)
print("PLATFORM:", platform.platform())
print("IMPORTED GRADIO VERSION:", gr.__version__)
print("INSTALLED GRADIO VERSION:",
      pkg_resources.get_distribution("gradio").version)
print("GRADIO LOCATION:", gr.__file__)
print("=" * 60)

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

    chatbot = gr.Chatbot(
        type="messages",
        height=500
    )

    def respond(message, history):
        answer = chat_fn(message, history)

        history.append(
            {
                "role": "user",
                "content": message
            }
        )

        history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

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
