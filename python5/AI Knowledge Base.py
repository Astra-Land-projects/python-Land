from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = []

for file in Path("knowledge").glob("*.txt"):

    text = file.read_text(
        encoding="utf-8"
    )

    documents.append({
        "name": file.name,
        "text": text
    })

if not documents:
    raise SystemExit(
        "Put .txt files inside knowledge/"
    )

texts = [
    doc["text"]
    for doc in documents
]

vectorizer = TfidfVectorizer(
    stop_words="english"
)

matrix = vectorizer.fit_transform(
    texts
)


def search(query, top_k=3):

    query_vector = vectorizer.transform(
        [query]
    )

    scores = cosine_similarity(
        query_vector,
        matrix
    )[0]

    indexes = scores.argsort()[::-1]

    results = []

    for index in indexes[:top_k]:

        results.append({
            "file": documents[index]["name"],
            "score": float(scores[index]),
            "text": documents[index]["text"]
        })

    return results


while True:

    query = input(
        "\nAsk (exit): "
    )

    if query == "exit":
        break

    results = search(query)

    print("\n===== KNOWLEDGE BASE =====")

    for result in results:

        print(
            f"\n[{result['file']}] "
            f"score={result['score']:.3f}"
        )

        print(
            result["text"][:500]
        )