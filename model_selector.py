import torch

class model_generator:

    def __init__(self, model_type, model_name):
        self.model_type = model_type
        self.model_name = model_name

    def get_model(self):
        if self.model_type == 'ResNet':
            model = torch.hub.load(
                'pytorch/vision:v0.10.0',
                {self.model_name},
                pretrained=True,
                progress=True
            )
        
        if self.model_type == 'EfficientNet':
            model = torch.hub.load(
                'pytorch/vision',
                'efficientnet_b0',
                pretrained=True
            )

        if self.model_type == 'MobileNet':
            pass

        if self.model_type == 'YOLOv8':
            pass

        return model


