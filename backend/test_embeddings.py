from app.ml.inference.embedder import extract_embedding

with open("test.jpg", "rb") as f:
    emb = extract_embedding(f)

print(emb)
