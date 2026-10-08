import PyPDF2

files = input("PDF files separated by comma: ").split(",")
out = input("Output PDF: ").strip()

merger = PyPDF2.PdfMerger()
for f in files:
    merger.append(f.strip())
merger.write(out)
merger.close()
print("Saved:", out)