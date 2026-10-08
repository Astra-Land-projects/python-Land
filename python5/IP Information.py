import requests

data = requests.get(
    "https://ipinfo.io/json"
).json()

print("IP:", data.get("ip"))
print("City:", data.get("city"))
print("Country:", data.get("country"))
print("ISP:", data.get("org"))