from fastapi import FastAPI, File, UploadFile, Form
import shutil
import os

from resume_parser import extract_text_from_pdf
from skills import extract_skills
from matcher import match_skills

app = FastAPI()

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.get("/")
def home():
    return {"message": "HireSense AI backend running"}


@app.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    job_role: str = Form(...)
):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

    detected_skills = extract_skills(extracted_text)

    job_analysis = match_skills(detected_skills, job_role)

    return {
        "filename": file.filename,
        "detected_skills": detected_skills,
        "job_analysis": job_analysis,
        "text_preview": extracted_text[:300]
    }
