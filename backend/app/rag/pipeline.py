from pathlib import Path

from app.services.pdf_service import extract_text
from app.rag.chunker import chunk_text
from app.rag.embedder import embed_chunks
from app.rag.vector_store import (
    create_vector_store,
    save_index,
    save_chunks,
)


def process_pdf(pdf_path: Path):
    """
    Process a PDF and save its FAISS index and chunks.
    """

    # Extract text
    text = extract_text(pdf_path)

    # Split into chunks
    chunks = chunk_text(text)

    # Generate embeddings
    embeddings = embed_chunks(chunks)

    # Create FAISS index
    index = create_vector_store(embeddings)

    # Persist to disk
    save_index(index)
    save_chunks(chunks)

    return {
        "chunks": len(chunks),
        "vectors": index.ntotal,
    }