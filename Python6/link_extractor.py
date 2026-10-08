import requests
from bs4 import BeautifulSoup


class LinkExtractor:

    def extract(self, url):
        soup = BeautifulSoup(requests.get(url).text, "html.parser")

        for link in soup.find_all("a"):
            print(link.get("href"))