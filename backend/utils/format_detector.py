def detect_format(filename, content):
    if filename.endswith(".pdf"):
        return "PDF"
    elif filename.endswith(".json"):
        return "JSON"
    elif filename.endswith(".txt") or "@" in content.decode(errors="ignore"):
        return "Email"
    else:
        return "Unknown"
