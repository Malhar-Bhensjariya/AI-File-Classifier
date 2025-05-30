from utils.format_detector import detect_format
from utils.intent_classifier import classify_intent
from agents.email_agent import handle_email
from agents.json_agent import handle_json
from agents.pdf_agent import handle_pdf

def classify_and_route(filename, content, memory):
    file_format = detect_format(filename, content)
    intent = classify_intent(content)

    memory.log_metadata(filename, file_format, intent)

    if file_format == "Email":
        return handle_email(content, memory)
    elif file_format == "JSON":
        return handle_json(content, memory)
    elif file_format == "PDF":
        return handle_pdf(content, memory)
    else:
        return {"error": "Unsupported format"}
