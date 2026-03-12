import re

def extract_experience(text):

    years = re.findall(r"\d+\+?\s+years", text)

    if years:
        return int(years[0].split()[0])

    return 0
