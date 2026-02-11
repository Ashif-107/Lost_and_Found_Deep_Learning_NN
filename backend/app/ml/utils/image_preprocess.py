from torchvision import transforms
from PIL import Image

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def preprocess_image(image_file):
    image = Image.open(image_file).convert("RGB")
    image = transform(image)
    return image.unsqueeze(0)  # add batch dimension
