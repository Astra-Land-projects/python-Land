from PyPDF2 import PdfMerger


class PDFMerger:

    def merge(self, files, output):
        merger = PdfMerger()

        try:
            for file in files:
                merger.append(file.strip())

            merger.write(output)
            merger.close()

            print("PDFs merged successfully.")

        except Exception as e:
            print("Error:", e)