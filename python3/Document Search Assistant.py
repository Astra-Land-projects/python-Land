import os
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DOCUMENTS_DIR = Path("documents")


def load_documents():
    documents = []

    DOCUMENTS_DIR.mkdir(
        exist_ok=True
    )

    for file in DOCUMENTS_DIR.glob("*.txt"):

        text = file.read_text(
            encoding="utf-8"
        )

        documents.append({
            "name": file.name,
            "text": text
        })

    return documents


documents = load_documents()

if not documents:
    print(
        "Put .txt files inside the "
        "'documents' folder."
    )

    raise SystemExit


texts = [
    document["text"]
    for document in documents
]


vectorizer = TfidfVectorizer(
    stop_words="english"
)

matrix = vectorizer.fit_transform(texts)


def search(query):
    query_vector = vectorizer.transform(
        [query]
    )

    scores = cosine_similarity(
        query_vector,
        matrix
    )[0]

    indexes = scores.argsort()[::-1]

    return [
        (
            documents[index]["name"],
            scores[index]
        )
        for index in indexes
        if scores[index] > 0
    ]


print("===== DOCUMENT SEARCH =====")
print("Type 'exit' to quit.")


while True:

    query = input("\nSearch: ")

    if query.lower() == "exit":
        break

    results = search(query)

    if not results:
        print("Nothing found.")
        continue

    for name, score in results:
        print(
            f"{name} -> {score:.3f}"
        )