import requests


class CurrencyConverter:

    def convert(self, base, target, amount):
        url = f"https://open.er-api.com/v6/latest/{base}"

        response = requests.get(url).json()

        if "rates" in response:
            result = amount * response["rates"][target]
            print("Converted:", result)
        else:
            print("Error")