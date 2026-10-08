import PyPDF2

path = input("PDF file: ").strip()
with open(path, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    for i, page in enumerate(reader.pages, start=1):
        print(f"\n--- Page {i} ---\n")
        print(page.extract_text() or "")