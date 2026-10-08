import pyshorteners


class URLShortener:

    def __init__(self):
        self.shortener = pyshorteners.Shortener()

    def shorten(self, url):
        try:
            return self.shortener.tinyurl.short(url)
        except Exception as e:
            return f"Error: {e}"