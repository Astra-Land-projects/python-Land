from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression

app = FastAPI()

X = [
    [50, 1],
    [70, 2],
    [90, 2],
    [120, 3],
    [150, 4]
]

y = [
    100000,
    150000,
    190000,
    260000,
    330000
]

model = LinearRegression()
model.fit(X, y)


class House(BaseModel):
    area: float
    rooms: int


@app.post("/predict")
def predict(house: House):

    price = model.predict([
        [house.area, house.rooms]
    ])[0]

    return {
        "predicted_price": round(float(price), 2)
    }