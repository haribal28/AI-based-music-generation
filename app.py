import gradio as gr
from model import generate_music

def run(seed):

    file = generate_music(seed)

    return file

demo = gr.Interface(
    fn=run,
    inputs=gr.Textbox(label="Enter starting notes"),
    outputs=gr.File(),
    title="AI Music Generator"
)

demo.launch()