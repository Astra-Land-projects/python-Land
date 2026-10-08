from PyPDF2 import PdfReader
import os


class PDFReader:

    def read_pdf(self, filename):
        if not os.path.exists(filename):
            print("File Not Found.")
            return

        try:
            pdf = PdfReader(filename)

            print(f"\nPages: {len(pdf.pages)}\n")

            for i, page in enumerate(pdf.pages, start=1):
                print(f"===== PAGE {i} =====")
                text = page.extract_text()
                print(text if text else "No text found.")
                print()

        except Exception as e:
            print("Error:", e)