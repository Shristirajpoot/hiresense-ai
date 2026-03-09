import fitz

def extract_text_from_pdf(file_path):
    text = ""

    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()

    except Exception as e:
        return f"Error reading PDF: {str(e)}"

    return text
