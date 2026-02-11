from fastapi import APIRouter, UploadFile, File, Form
from app.services.s3_service import upload_image
from app.ml.inference.embedder import extract_embedding
from app.ml.similarity.index_manager import faiss_index

router = APIRouter()

@router.post("/upload")
async def upload_item(
    image: UploadFile = File(...),
    description: str = Form(...)
):
    # 1. Upload image to S3
    image_url = upload_image(image.file)

    # 2. Extract embedding
    embedding = extract_embedding(image.file)

    # 3. Store embedding in FAISS with metadata
    faiss_index.add(
        embedding,
        {
            "image_url": image_url,
            "description": description
        }
    )

    return {
        "message": "Item uploaded and indexed successfully",
        "image_url": image_url
    }
