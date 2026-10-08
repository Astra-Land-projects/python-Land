import re
import requests


class EmailExtractor:

    def extract(self, url):
        text = requests.get(url).text

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        for email in set(emails):
            print(email)