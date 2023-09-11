import gradio as gr
import os
import cv2
import model_selector
import argparse


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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--server_name',
        type=str
    )
    parser.add_argument(
        '--server_port',
        type=int
    )
    args=parser.parse_args()

    demo.launch(
        server_name=args.server_name,
        server_port=args.server_port
    )