import requests
from bs4 import BeautifulSoup


class WebsiteTitle:

    def get_title(self, url):
        html = requests.get(url).text

        soup = BeautifulSoup(html, "html.parser")

        print(soup.title.text)