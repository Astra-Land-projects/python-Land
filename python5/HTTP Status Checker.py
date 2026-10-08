import requests

url = input("URL: ")

response = requests.get(url)

print("Status:", response.status_code)

if response.status_code == 200:
    print("Website is online")
else:
    print("Status:", response.status_code)