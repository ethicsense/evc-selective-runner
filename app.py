import gradio as gr
import os
import cv2
import model_selector


def print_model(model_type, model_name):
    mg =  model_selector.model_generator(model_type, model_name)
    model = mg.get_model()
    if model:
        out = "Success"
    else:
        out = "Fail"

    return out, model



def run_model():
    pass


demo = gr.Interface(
    fn=print_model,
    inputs=["text", "text"],
    outputs=[
        gr.Textbox(label="Done or Not", lines=1),
        gr.Textbox(label="Model Architecture", lines=1)
    ]
)

if __name__ == "__main__":
    demo.launch()