from pytubefix import YouTube


class AudioDownloader:

    def download_audio(self, url):
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()

        print("Audio Downloaded.")