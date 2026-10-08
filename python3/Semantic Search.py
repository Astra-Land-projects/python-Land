from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    "Python is a programming language.",
    "Machine learning uses data to learn patterns.",
    "Deep learning uses neural networks.",
    "FastAPI is used to build Python APIs.",
    "Flutter is a framework for mobile applications.",
    "Git is used for version control.",
    "TensorFlow is a machine learning framework.",
    "Natural language processing works with human language."
]


vectorizer = TfidfVectorizer(
    stop_words="english"
)

document_vectors = vectorizer.fit_transform(
    documents
)


def search(query, top_k=5):
    query_vector = vectorizer.transform(
        [query]
    )

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    indexes = similarities.argsort()[::-1]

    results = []

    for index in indexes[:top_k]:
        if similarities[index] > 0:
            results.append(
                (
                    documents[index],
                    similarities[index]
                )
            )

    return results


print("===== SEMANTIC SEARCH =====")
print("Type 'exit' to quit.")

while True:
    query = input("\nSearch: ")

    if query.lower() == "exit":
        break

    results = search(query)

    if not results:
        print("No results.")
        continue

    print("\nResults:")

    for document, score in results:
        print(
            f"[{score:.3f}] {document}"
        )