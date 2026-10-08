import requests


class HeaderViewer:

    def show(self, url):
        response = requests.get(url)

        for key, value in response.headers.items():
            print(key, ":", value)