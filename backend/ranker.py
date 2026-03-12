def rank_resumes(candidates):

    sorted_list = sorted(
        candidates,
        key=lambda x: x["final_score"],
        reverse=True
    )

    for i,c in enumerate(sorted_list):
        c["rank"] = i + 1

    return sorted_list
