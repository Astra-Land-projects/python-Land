import barcode
from barcode.writer import ImageWriter


class BarcodeGenerator:

    def generate(self, code, filename):
        try:
            barcode_class = barcode.get_barcode_class("code128")
            barcode_image = barcode_class(code, writer=ImageWriter())
            barcode_image.save(filename)
            print("Barcode Generated Successfully.")
        except Exception as e:
            print("Error:", e)