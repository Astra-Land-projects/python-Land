import PyPDF2

path = input("PDF file: ").strip()
with open(path, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    for i, page in enumerate(reader.pages, start=1):
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)
        out = f"page_{i}.pdf"
        with open(out, "wb") as o:
            writer.write(o)
        print("Saved:", out)