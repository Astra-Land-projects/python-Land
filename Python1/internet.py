import requests

try:
    response = requests.get("https://www.google.com", timeout=5)
    if response.status_code == 200:
        print("Internet connection is active.")
    else:
        print("Internet connection seems to have issues.")
except requests.ConnectionError:
    print("No internet connection.")
except requests.Timeout:
    print("Request timed out. Check your internet connection.")