from fastapi import APIRouter, UploadFile, File
from app.pdf_utils import extract_text_from_pdf
from app.qa_model import get_answer
import os

router = APIRouter()
PDF_STORAGE = "uploads"
PDF_CONTENT = ""  # temporary in-memory store

# ✅ Make sure upload folder exists
os.makedirs(PDF_STORAGE, exist_ok=True)

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(PDF_STORAGE, file.filename)

    # ✅ Save PDF file to disk
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # ✅ Extract and store text from PDF
    global PDF_CONTENT
    PDF_CONTENT = extract_text_from_pdf(file_path)

    return {"message": "PDF uploaded successfully", "file": file.filename}

@router.get("/ask")
def ask_question(question: str):
    global PDF_CONTENT
    if not PDF_CONTENT:
        return {"answer": "No PDF uploaded yet."}
    answer = get_answer(question, PDF_CONTENT)
    return {"answer": answer}
