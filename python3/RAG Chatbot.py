from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    """
    Python is a high-level programming language.
    It is popular for web development and artificial intelligence.
    """,

    """
    Machine learning allows computers to learn patterns
    from data without being explicitly programmed.
    """,

    """
    Deep learning is a branch of machine learning
    based on neural networks with multiple layers.
    """,

    """
    FastAPI is a modern Python framework for building APIs.
    """,

    """
    Git is a version control system used to track changes
    in software projects.
    """
]


vectorizer = TfidfVectorizer(
    stop_words="english"
)

matrix = vectorizer.fit_transform(documents)


def retrieve(question, top_k=2):
    question_vector = vectorizer.transform(
        [question]
    )

    scores = cosine_similarity(
        question_vector,
        matrix
    )[0]

    indexes = scores.argsort()[::-1][:top_k]

    return [
        documents[index]
        for index in indexes
        if scores[index] > 0
    ]


print("===== RAG CHATBOT =====")
print("Type 'exit' to quit.")


while True:
    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    results = retrieve(question)

    if not results:
        print("I couldn't find relevant information.")
        continue

    print("\nRetrieved context:")

    for document in results:
        print("\n---")
        print(document.strip())