import pdf2image
import pytesseract
from PIL import Image

def pdf_to_text(pdf_path, output_txt="output.txt"):
    """Converts a PDF file to text using OCR."""
    images = pdf2image.convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    pdf_file = "example.pdf"  # Replace with your PDF file
    pdf_to_text(pdf_file, "extracted_text.txt")
    print("PDF converted to text and saved as extracted_text.txt")