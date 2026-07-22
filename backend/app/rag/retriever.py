from app.rag.embedder import model


def retrieve_chunks(
    question: str,
    index,
    chunks: list[str],
    top_k: int = 5,
) -> list[str]:
    """
    Retrieve the most relevant chunks for a question.
    """

    question_embedding = model.encode(
        [question],
        convert_to_numpy=True
    ).astype("float32")

    _, indices = index.search(question_embedding, top_k)

    retrieved_chunks = [
        chunks[i]
        for i in indices[0]
    ]

    return retrieved_chunks