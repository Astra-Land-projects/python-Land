import pytesseract
from PIL import Image

path = input("Image: ")

image = Image.open(path)

text = pytesseract.image_to_string(
    image
)

print("\n===== OCR RESULT =====\n")
print(text)

with open(
    "ocr_result.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(text)

print("Saved.")