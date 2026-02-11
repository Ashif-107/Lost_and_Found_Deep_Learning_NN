from fastapi import APIRouter, UploadFile, File
from app.ml.inference.embedder import extract_embedding
from app.ml.similarity.index_manager import faiss_index

router = APIRouter()

@router.post("/search")
async def search_item(image: UploadFile = File(...)):
    # 1. Extract embedding from query image
    embedding = extract_embedding(image.file)

    # 2. Search FAISS
    results = faiss_index.search(embedding, k=5)

    return results
