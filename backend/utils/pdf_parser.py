import io
import pdfplumber

def extract_pdf_text(content):
    with pdfplumber.open(io.BytesIO(content)) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)
