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


def show_models(model_type):
    if model_type == "ResNet":
        lst = [
            "resnet18",
            "resnet34",
            "resnet50",
            "resnet101",
            "resnet152"
        ]
    elif model_type == "EfficientNet":
        lst = [
            "efficientnet_b0",
            "efficientnet_b1",
            "efficientnet_b2",
            "efficientnet_b3",
            "efficientnet_b4",
            "efficientnet_b5",
            "efficientnet_b6",
            "efficientnet_b7"
        ]
    elif model_type == "MobileNet":
        lst = [
            "mobilenet_v3_small",
            "mobilenet_v3_large"
        ]
    elif model_type == "YOLOv8":
        lst = [
            "yolov8"
        ]
    
    return lst


def get_weights(f):

    return f


def run_model():
    pass


def run_gradio():
    with gr.Blocks() as demo:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--server_name',
        type=str,
        defualt='0.0.0.0'
    )
    parser.add_argument(
        '--server_port',
        type=int,
        default=7860
    )
    args=parser.parse_args()

    demo.launch(
        server_name=args.server_name,
        server_port=args.server_port
    )