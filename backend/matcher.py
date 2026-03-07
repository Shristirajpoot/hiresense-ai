# matcher.py

JOB_ROLES = {
    "backend developer": [
        "python",
        "sql",
        "docker",
        "fastapi",
        "git"
    ],
    "frontend developer": [
        "javascript",
        "react",
        "html",
        "css",
        "git"
    ],
    "data scientist": [
        "python",
        "machine learning",
        "pandas",
        "numpy",
        "sql"
    ]
}


def match_skills(user_skills, job_role):
    job_role = job_role.lower()

    if job_role not in JOB_ROLES:
        return {
            "error": "Job role not found"
        }

    required_skills = JOB_ROLES[job_role]

    matched = []
    missing = []

    for skill in required_skills:
        if skill in user_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(required_skills)) * 100)

    return {
        "job_role": job_role,
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }
