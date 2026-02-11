from fastapi import APIRouter, UploadFile, File
from io import BytesIO

from app.ml.inference.embedder import extract_embedding
from app.ml.similarity.index_manager import faiss_index

router = APIRouter()

@router.post("/search")
async def search_item(image: UploadFile = File(...)):
    image_bytes = await image.read()

    embedding = extract_embedding(BytesIO(image_bytes))
    results = faiss_index.search(embedding, k=3)

    return results
