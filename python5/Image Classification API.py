from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()

@app.post("/classify")
async def classify(file: UploadFile = File(...)):

    data = await file.read()

    image = Image.open(
        io.BytesIO(data)
    )

    return {
        "filename": file.filename,
        "width": image.width,
        "height": image.height,
        "format": image.format
    }