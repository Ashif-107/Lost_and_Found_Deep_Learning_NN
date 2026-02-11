import torch
from app.ml.models.resnet import get_resnet_model
from app.ml.utils.image_preprocess import preprocess_image

model = get_resnet_model()

def extract_embedding(image_file):
    image_tensor = preprocess_image(image_file)

    with torch.no_grad():
        embedding = model(image_tensor)

    # Convert to numpy
    embedding = embedding.squeeze().numpy()

    # Normalize vector (VERY IMPORTANT for similarity)
    embedding = embedding / (embedding.sum() ** 0.5)

    return embedding
    