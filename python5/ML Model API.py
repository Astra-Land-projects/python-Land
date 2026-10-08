import joblib

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load(
    "model.pkl"
)


class InputData(BaseModel):
    features: list[float]


@app.post("/predict")
def predict(data: InputData):

    prediction = model.predict(
        [data.features]
    )

    return {
        "prediction":
        prediction.tolist()
    }