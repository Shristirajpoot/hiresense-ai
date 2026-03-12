def compute_scores(resume_skills, job_skills, experience):

    skill_match = len(set(resume_skills) & set(job_skills))
    total = len(job_skills)

    skill_score = 0

    if total > 0:
        skill_score = skill_match / total

    experience_score = min(experience / 5, 1)

    final_score = (skill_score * 0.7 + experience_score * 0.3) * 100

    return {
        "skill_score": round(skill_score*100,2),
        "experience_score": round(experience_score*100,2),
        "final_score": round(final_score,2)
    }
