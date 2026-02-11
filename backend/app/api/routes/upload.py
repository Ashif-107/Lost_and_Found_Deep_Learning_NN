from fastapi import APIRouter, UploadFile, File, Form
from io import BytesIO

from app.services.s3_service import upload_image
from app.ml.inference.embedder import extract_embedding
from app.ml.similarity.index_manager import faiss_index

router = APIRouter()

@router.post("/upload")
async def upload_item(
    image: UploadFile = File(...),
    description: str = Form(...)
):
    # 🔥 Read file ONCE
    image_bytes = await image.read()

    # 1. Upload to S3
    image_url = upload_image(BytesIO(image_bytes))

    # 2. Extract embedding
    embedding = extract_embedding(BytesIO(image_bytes))

    # 3. Add to FAISS
    faiss_index.add(
        embedding,
        {
            "image_url": image_url,
            "description": description
        }
    )

    return {
        "message": "Item uploaded & indexed successfully",
        "image_url": image_url
    }
