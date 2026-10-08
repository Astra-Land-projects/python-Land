from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

files = list(Path("knowledge").glob("*.txt"))

documents = [
    f.read_text(encoding="utf-8")
    for f in files
]

vectorizer = TfidfVectorizer(stop_words="english")
matrix = vectorizer.fit_transform(documents)

while True:
    question = input("Question (exit): ")

    if question == "exit":
        break

    q = vectorizer.transform([question])
    scores = cosine_similarity(q, matrix)[0]

    best = scores.argsort()[::-1][:3]

    print("\nRelevant context:")

    for i in best:
        print("\n---")
        print(documents[i][:1000])