from pathlib import Path
import fitz  # PyMuPDF


def extract_text(pdf_path: Path) -> str:
    """
    Extract all text from a PDF file.
    """

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text