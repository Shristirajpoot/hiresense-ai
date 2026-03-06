from fastapi import FastAPI, File, UploadFile
import shutil
import os
import fitz  # PyMuPDF

# Import skill detection
from skills import extract_skills

app = FastAPI()

UPLOAD_FOLDER = "uploads"

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file using PyMuPDF
    """
    text = ""

    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()

    except Exception as e:
        return f"Error reading PDF: {str(e)}"

    return text


@app.get("/")
def home():
    return {"message": "HireSense AI backend running"}


@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload resume, extract text, and detect skills
    """

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from resume
    extracted_text = extract_text_from_pdf(file_path)

    # Detect skills from resume text
    detected_skills = extract_skills(extracted_text)

    return {
        "filename": file.filename,
        "status": "uploaded successfully",
        "detected_skills": detected_skills,
        "text_preview": extracted_text[:500]  # preview first 500 chars
    }
