# project_188_qr_generator.py

import qrcode

text = input("Text or URL: ").strip()
name = input("File name (without extension): ").strip() or "qr"

img = qrcode.make(text)
img.save(f"{name}.png")

print("Saved:", f"{name}.png")