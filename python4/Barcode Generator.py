# project_189_barcode_generator.py

from barcode import Code128
from barcode.writer import ImageWriter

data = input("Barcode data: ").strip()
name = input("File name: ").strip() or "barcode"

barcode = Code128(data, writer=ImageWriter())
barcode.save(name)

print("Saved:", f"{name}.png")