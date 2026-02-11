import torch
import torch.nn as nn
from torchvision import models

def get_resnet_model():
    model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)

    # Remove final classification layer
    model.fc = nn.Identity()

    model.eval()
    return model
