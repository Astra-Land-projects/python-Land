import os
from PyPDF2 import PdfReader, PdfWriter


class PDFSplitter:

    def split(self, filename):
        if not os.path.exists(filename):
            print("File Not Found.")
            return

        try:
            reader = PdfReader(filename)

            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)

                output = f"page_{i + 1}.pdf"

                with open(output, "wb") as file:
                    writer.write(file)

            print(f"Done! {len(reader.pages)} pages created.")

        except Exception as e:
            print("Error:", e)