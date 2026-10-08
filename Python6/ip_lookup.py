import requests


class IPLookup:

    def lookup(self, ip):
        response = requests.get(f"http://ip-api.com/json/{ip}")

        print(response.json())