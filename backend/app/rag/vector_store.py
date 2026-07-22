from pathlib import Path
import pickle

import faiss
import numpy as np


INDEX_PATH = Path("data/indexes/faiss_index.index")
CHUNKS_PATH = Path("data/metadata/chunks.pkl")


def create_vector_store(embeddings: list[list[float]]) -> faiss.IndexFlatL2:
    """
    Create a FAISS vector index from embeddings.
    """

    vectors = np.array(embeddings).astype("float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    return index


def save_index(index: faiss.IndexFlatL2):
    """
    Save FAISS index to disk.
    """

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)

    faiss.write_index(index, str(INDEX_PATH))


def load_index() -> faiss.IndexFlatL2:
    """
    Load FAISS index from disk.
    """

    return faiss.read_index(str(INDEX_PATH))


def save_chunks(chunks: list[str]):
    """
    Save document chunks to disk.
    """

    CHUNKS_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(CHUNKS_PATH, "wb") as file:
        pickle.dump(chunks, file)


def load_chunks() -> list[str]:
    """
    Load document chunks from disk.
    """

    with open(CHUNKS_PATH, "rb") as file:
        return pickle.load(file)