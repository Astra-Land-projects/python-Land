import requests
from bs4 import BeautifulSoup

url = input("URL: ")

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all("a", href=True):
    print(link["href"])