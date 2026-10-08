import requests


class StatusChecker:

    def check(self, url):
        response = requests.get(url)

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            print("Website is Online")
        else:
            print("Website may be Offline")