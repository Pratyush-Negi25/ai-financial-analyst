from app.rag.embedder import model
from app.rag.vector_store import (
    load_index,
    load_chunks,
)


def retrieve_chunks(
    question: str,
    top_k: int = 5,
) -> list[str]:
    """
    Retrieve the most relevant chunks for a question.
    """

    # Load persisted data
    index = load_index()
    chunks = load_chunks()

    # Generate embedding for the user's question
    question_embedding = model.encode(
        [question],
        convert_to_numpy=True
    ).astype("float32")

    # Search the FAISS index
    _, indices = index.search(question_embedding, top_k)

    # Retrieve matching chunks
    retrieved_chunks = [
        chunks[i]
        for i in indices[0]
    ]

    return retrieved_chunks