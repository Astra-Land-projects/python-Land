from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

files = list(Path("documents").glob("*.txt"))

texts = [
    f.read_text(encoding="utf-8")
    for f in files
]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(texts)

while True:
    query = input("Search (exit): ")

    if query == "exit":
        break

    q = vectorizer.transform([query])
    scores = cosine_similarity(q, matrix)[0]

    for i in scores.argsort()[::-1][:5]:
        print(
            f"{files[i].name} "
            f"({scores[i]:.3f})"
        )