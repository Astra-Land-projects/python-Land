import requests
import json

url = input("API URL: ")

response = requests.get(url)

data = response.json()

print(json.dumps(
    data,
    indent=2,
    ensure_ascii=False
))