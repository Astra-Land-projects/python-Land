from pyzbar.pyzbar import decode
from PIL import Image
import os


class QRScanner:

    def scan(self, filename):
        if not os.path.exists(filename):
            print("File Not Found.")
            return

        try:
            image = Image.open(filename)
            result = decode(image)

            if not result:
                print("No QR Code Found.")
                return

            for item in result:
                print("QR Data:", item.data.decode("utf-8"))

        except Exception as e:
            print("Error:", e)