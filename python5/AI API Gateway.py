from fastapi import FastAPI
import requests

app = FastAPI()

SERVICES = {
    "sentiment":
        "http://localhost:8001/predict",

    "classifier":
        "http://localhost:8002/predict"
}


@app.post("/ai/{service}")
def ai(service: str, data: dict):

    if service not in SERVICES:

        return {
            "error":
            "Unknown AI service"
        }

    response = requests.post(
        SERVICES[service],
        json=data
    )

    return response.json()