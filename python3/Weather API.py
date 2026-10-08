from fastapi import FastAPI


app = FastAPI(title="Weather API")


weather = {
    "Frankfurt": {
        "temperature": 22,
        "condition": "Cloudy"
    },
    "Berlin": {
        "temperature": 24,
        "condition": "Sunny"
    },
    "London": {
        "temperature": 18,
        "condition": "Rainy"
    }
}


@app.get("/weather/{city}")
def get_weather(city: str):

    data = weather.get(city)

    if data is None:
        return {
            "error": "City not found"
        }

    return {
        "city": city,
        **data
    }