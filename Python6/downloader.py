from pytubefix import YouTube


class Downloader:

    def download(self, url):
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()

        print("Download Complete.")