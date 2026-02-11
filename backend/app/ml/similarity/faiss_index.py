import os
import faiss
import numpy as np # type: ignore
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

INDEX_PATH = os.path.join(DATA_DIR, "faiss.index")
META_PATH = os.path.join(DATA_DIR, "metadata.pkl")

DIM = 2048

class FaissIndex:
    def __init__(self):
        self.index = faiss.IndexFlatL2(DIM)
        self.metadata = []

        if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
            self.index = faiss.read_index(INDEX_PATH)
            with open(META_PATH, "rb") as f:
                self.metadata = pickle.load(f)

            print(f"✅ FAISS loaded: {self.index.ntotal} vectors")
        else:
            print("⚠️ No FAISS index found, starting fresh")

    def add(self, embedding, meta):
        embedding = np.array([embedding]).astype("float32")
        self.index.add(embedding)
        self.metadata.append(meta)
        self.save()

    def search(self, embedding, k=3):
        if self.index.ntotal == 0:
            return []

        embedding = np.array([embedding]).astype("float32")
        distances, indices = self.index.search(embedding, k)

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx == -1:
                continue

            similarity = float(1 / (1 + float(dist)))
            item = self.metadata[idx].copy()
            item["similarity"] = similarity
            results.append(item)

        return results

    def save(self):
        faiss.write_index(self.index, INDEX_PATH)
        with open(META_PATH, "wb") as f:
            pickle.dump(self.metadata, f)
