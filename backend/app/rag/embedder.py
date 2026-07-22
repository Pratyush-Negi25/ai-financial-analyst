from sentence_transformers import SentenceTransformer


# Load the embedding model once when the application starts
model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def embed_chunks(chunks: list[str]) -> list[list[float]]:
    """
    Convert text chunks into embedding vectors.
    """

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings.tolist()