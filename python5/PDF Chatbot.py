import re, sys, PyPDF2

def read_pdf(path):
    text = ""
    with open(path, "rb") as f:
        r = PyPDF2.PdfReader(f)
        for p in r.pages:
            text += (p.extract_text() or "") + "\n"
    return text

def search(text, q):
    q_words = set(re.findall(r"\w+", q.lower()))
    out = []
    for s in re.split(r"(?<=[.!?])\s+", text):
        score = len(q_words & set(re.findall(r"\w+", s.lower())))
        if score:
            out.append((score, s.strip()))
    return [s for _, s in sorted(out, reverse=True)[:5]]

pdf = sys.argv[1]
doc = read_pdf(pdf)
while True:
    q = input("Question (exit): ")
    if q == "exit": break
    for s in search(doc, q):
        print("-", s)