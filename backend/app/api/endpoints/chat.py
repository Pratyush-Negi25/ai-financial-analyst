"""
Chat endpoint for asking questions about the uploaded financial document.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.llm.chatbot import generate_answer
from app.rag.retriever import retrieve_chunks

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    question: str


@router.post("/")
async def chat(request: ChatRequest):
    """
    Answer a user's question using Retrieval-Augmented Generation (RAG).
    """

    # Retrieve relevant chunks from the uploaded document
    context = retrieve_chunks(request.question)

    # Generate answer using Gemini
    answer = generate_answer(
        question=request.question,
        context=context,
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": len(context),
    }