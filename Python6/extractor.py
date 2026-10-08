import zipfile


class Extractor:

    def extract(self, archive):
        with zipfile.ZipFile(archive, "r") as zipf:
            zipf.extractall("output")

        print("Extracted.")