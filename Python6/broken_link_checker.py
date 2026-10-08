import requests
from bs4 import BeautifulSoup


class BrokenLinkChecker:

    def check(self, url):
        soup = BeautifulSoup(requests.get(url).text, "html.parser")

        for link in soup.find_all("a", href=True):
            href = link["href"]

            try:
                status = requests.get(href, timeout=5).status_code
                print(href, status)
            except Exception:
                print(href, "Broken")