import fitz  # PyMuPDF
import docx
from typing import Union
from io import BytesIO

def extract_text_from_pdf(file: BytesIO) -> str:
    try:
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"PDF extraction error: {e}")
        return ""

def extract_text_from_docx(file: BytesIO) -> str:
    try:
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        print(f"DOCX extraction error: {e}")
        return ""

def extract_text_from_resume(resume_file: Union[BytesIO, None]) -> str:
    if resume_file is None:
        return ""
    
    filename = resume_file.name.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(resume_file)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(resume_file)
    else:
        return ""

