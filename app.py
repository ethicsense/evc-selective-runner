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



def get_weights(f):

    return f


def run_model():
    pass



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--server_name',
        type=str,
        default='0.0.0.0'
    )
    parser.add_argument(
        '--server_port',
        type=int,
        default=7860
    )
    args=parser.parse_args()


    with gr.Blocks() as demo:
        radio = gr.Radio(label="Model Class", choices=["ResNet", "EfficientNet", "MobileNet", "YOLOv8"])
        model_list = gr.Dropdown(label="Models Available", choices=[], interactive=True)
        model_map = {
            "ResNet" : [
                "resnet18",
                "resnet34",
                "resnet50",
                "resnet101",
                "resnet152"
            ],
            "EfficientNet" : [
                "efficientnet_b0",
                "efficientnet_b1",
                "efficientnet_b2",
                "efficientnet_b3",
                "efficientnet_b4",
                "efficientnet_b5",
                "efficientnet_b6",
                "efficientnet_b7"
            ],
            "MobileNet" : [
                "mobilenet_v3_small",
                "mobilenet_v3_large"
            ],
            "YOLOv8" : [
                "yolov8n",
                "yolov8s",
                "yolov8m",
                "yolov8l",
                "yolov8x"
            ]
        }

        def filter_models(choice):
            if choice in model_map.keys():
                return gr.Dropdown.update(
                    choices=model_map[choice], value=model_map[choice][1]
                )
            else:
                return gr.Dropdown.update(visible=False)
        
        radio.change(filter_models, inputs=radio, outputs=model_list)



    demo.launch(
        server_name=args.server_name,
        server_port=args.server_port,
        debug=True
    )