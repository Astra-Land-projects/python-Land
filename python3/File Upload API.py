from pathlib import Path

from fastapi import FastAPI, File, UploadFile


app = FastAPI(title="File Upload API")


UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(
    exist_ok=True
)


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    destination = (
        UPLOAD_DIR / file.filename
    )

    content = await file.read()

    destination.write_bytes(content)

    return {
        "filename": file.filename,
        "size": len(content),
        "message": "Upload successful"
    }