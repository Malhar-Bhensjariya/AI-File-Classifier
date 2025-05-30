import json

def handle_json(content, memory):
    try:
        data = json.loads(content)
        missing = [k for k in ["id", "amount", "date"] if k not in data]
        memory.store_data("json", data)
        return {"parsed": data, "missing_fields": missing}
    except Exception as e:
        return {"error": str(e)}
