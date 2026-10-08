import requests

url = input("Long URL: ")

api = "https://tinyurl.com/api-create.php"

response = requests.get(
    api,
    params={"url": url}
)

print("Short URL:", response.text)