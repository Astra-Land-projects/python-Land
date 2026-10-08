import zipfile


class Zipper:

    def compress(self, filename):
        with zipfile.ZipFile("archive.zip", "w") as zipf:
            zipf.write(filename)

        print("Compressed.")