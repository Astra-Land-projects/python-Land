from fastapi import FastAPI, File, UploadFile
from pathlib import Path

app = FastAPI()
up = Path("uploads")
up.mkdir(exist_ok=True)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    data = await file.read()
    (up / file.filename).write_bytes(data)
    return {"filename": file.filename, "size": len(data)}