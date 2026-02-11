import faiss
import numpy as np # type: ignore
import os
import pickle

DIM = 2048

class FaissIndex:
    def __init__(self):
        self.index = faiss.IndexFlatL2(DIM)
        self.metadata = []  # stores image_url / item_id etc.

    def add(self, embedding, meta):
        """
        embedding: np.array (2048,)
        meta: dict (image_url, description, etc.)
        """
        embedding = np.array([embedding]).astype("float32")
        self.index.add(embedding)
        self.metadata.append(meta)

    def search(self, embedding, k=5):
        embedding = np.array([embedding]).astype("float32")
        distances, indices = self.index.search(embedding, k)

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx == -1:
                continue
            item = self.metadata[idx]
            item["distance"] = float(dist)
            results.append(item)

        return results

    def save(self, path="faiss.index"):
        faiss.write_index(self.index, path)
        with open("metadata.pkl", "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, path="faiss.index"):
        if os.path.exists(path):
            self.index = faiss.read_index(path)
            with open("metadata.pkl", "rb") as f:
                self.metadata = pickle.load(f)
