import qrcode


class QRGenerator:

    def generate(self, data, filename):
        try:
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=4
            )

            qr.add_data(data)
            qr.make(fit=True)

            image = qr.make_image(fill_color="black", back_color="white")
            image.save(filename)

            print("QR Code Generated Successfully.")

        except Exception as e:
            print("Error:", e)