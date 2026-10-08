import qrcode

def generate_qr_code(data, filename="qr.png"):
    """Generates a QR code image from the given data and saves it to a file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    data = "https://www.example.com"  # Replace with your desired data
    generate_qr_code(data, "example_qr.png")
    print("QR code generated and saved as example_qr.png")