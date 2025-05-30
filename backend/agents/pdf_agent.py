from utils.pdf_parser import extract_pdf_text

def handle_pdf(content, memory):
    text = extract_pdf_text(content)
    memory.store_data("pdf", {"text": text[:100]})
    return {"text_preview": text[:200]}
