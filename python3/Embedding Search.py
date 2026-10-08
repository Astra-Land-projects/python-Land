from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    "Python is a programming language.",
    "Machine learning is a branch of artificial intelligence.",
    "Deep learning uses neural networks.",
    "FastAPI is a Python web framework.",
    "Git is a version control system.",
    "Flutter is used to build mobile applications.",
    "Natural language processing works with text.",
    "Computer vision works with images."
]


vectorizer = TfidfVectorizer(
    stop_words="english"
)

embeddings = vectorizer.fit_transform(documents)


def search(query, top_k=5):
    query_embedding = vectorizer.transform(
        [query]
    )

    scores = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    indexes = scores.argsort()[::-1][:top_k]

    return [
        (documents[i], scores[i])
        for i in indexes
        if scores[i] > 0
    ]


print("===== EMBEDDING SEARCH =====")
print("Type 'exit' to quit.")

while True:
    query = input("\nQuery: ")

    if query.lower() == "exit":
        break

    results = search(query)

    if not results:
        print("No results.")
        continue

    for document, score in results:
        print(f"\n[{score:.3f}] {document}")