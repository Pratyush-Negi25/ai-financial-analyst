from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.rag.pipeline import process_pdf

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF financial report.
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    filename = f"{uuid4()}.pdf"

    destination = UPLOAD_DIR / filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process the uploaded PDF
    result = process_pdf(destination)

    return {
        "status": "success",
        "original_filename": file.filename,
        "stored_filename": filename,
        "chunks": result["chunks"],
        "vectors": result["vectors"],
    }