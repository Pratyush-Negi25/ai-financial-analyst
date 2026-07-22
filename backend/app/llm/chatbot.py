import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash",
)


def generate_answer(question: str, context: list[str]) -> str:
    """
    Generate an answer from Gemini using retrieved context.
    """

    prompt = f"""
You are an AI Financial Analyst.

Answer ONLY using the provided context.

If the answer cannot be found inside the context, reply exactly:

"I could not find that information in the uploaded document."

================ CONTEXT ================

{chr(10).join(context)}

=========================================

Question:

{question}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        return response.text

    except ServerError:
        return (
            "The AI service is temporarily unavailable due to high demand. "
            "Please try again in a few moments."
        )