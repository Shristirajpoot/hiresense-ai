# skills.py

SKILLS_DB = [
    "python",
    "java",
    "c++",
    "c",
    "javascript",
    "react",
    "node.js",
    "mongodb",
    "sql",
    "mysql",
    "machine learning",
    "deep learning",
    "fastapi",
    "django",
    "flask",
    "docker",
    "kubernetes",
    "aws",
    "git",
    "html",
    "css",
]

def extract_skills(resume_text):
    detected_skills = []

    resume_text = resume_text.lower()

    for skill in SKILLS_DB:
        if skill in resume_text:
            detected_skills.append(skill)

    return detected_skills
