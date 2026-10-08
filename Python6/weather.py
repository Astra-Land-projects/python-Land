import requests


class WeatherApp:

    API_KEY = "YOUR_API_KEY"

    def get_weather(self, city):
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={self.API_KEY}&units=metric"
        )

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Weather:", data["weather"][0]["description"])
        else:
            print("City Not Found")