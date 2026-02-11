from app.ml.similarity.faiss_index import FaissIndex
import numpy as np # type: ignore

faiss_index = FaissIndex()

# fake embeddings (simulate ResNet output)
emb1 = np.random.rand(2048)
emb2 = emb1 + np.random.normal(0, 0.01, 2048)  # similar
emb3 = np.random.rand(2048)  # different

faiss_index.add(emb1, {"name": "image1"})
faiss_index.add(emb2, {"name": "image2"})
faiss_index.add(emb3, {"name": "image3"})

results = faiss_index.search(emb1, k=2)
print(results)
