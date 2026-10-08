import requests


class ImageDownloader:

    def download(self, url):
        image = requests.get(url)

        with open("image.jpg", "wb") as file:
            file.write(image.content)

        print("Downloaded.")