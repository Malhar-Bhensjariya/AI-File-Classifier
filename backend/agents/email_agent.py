import json

def handle_email(content, memory):
    text = content.decode() if isinstance(content, bytes) else content
    sender = "example@example.com"  # stub
    urgency = "high" if "urgent" in text.lower() else "normal"
    memory.store_data("email", {"sender": sender, "urgency": urgency})
    
    return {"sender": sender, "urgency": urgency, "formatted": True}
