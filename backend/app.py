from fastapi import FastAPI, UploadFile, File, HTTPException
from agents.classifier_agent import classify_and_route
from memory.memory import MemoryManager

app = FastAPI(title="Multi-Agent AI System")
memory = MemoryManager()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = classify_and_route(file.filename, contents, memory)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
