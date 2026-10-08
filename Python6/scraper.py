import requests
from bs4 import BeautifulSoup


class WebScraper:

    def scrape(self, url):
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        for title in soup.find_all("h1"):
            print(title.text.strip())