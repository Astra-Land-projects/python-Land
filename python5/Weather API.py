import requests

city = input("City: ")

url = (
    "https://wttr.in/"
    + city
    + "?format=j1"
)

data = requests.get(url).json()

current = data["current_condition"][0]

print("Temperature:", current["temp_C"])
print("Humidity:", current["humidity"])
print("Weather:", current["weatherDesc"][0]["value"])