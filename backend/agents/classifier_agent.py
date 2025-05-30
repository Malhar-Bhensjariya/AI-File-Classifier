from utils.format_detector import detect_format
from utils.intent_classifier import classify_intent
from agents.email_agent import handle_email
from agents.json_agent import handle_json
from agents.pdf_agent import handle_pdf

def classify_and_route(filename, content, memory):
    fmt = detect_format(filename)
    intent = classify_intent(content)

    memory.log({
        "source": filename,
        "type": fmt,
        "intent": intent
    })

    if fmt == "email":
        return handle_email(content, memory)
    elif fmt == "json":
        return handle_json(content, memory)
    elif fmt == "pdf":
        return handle_pdf(content, memory)
    else:
        raise ValueError("Unsupported format.")
