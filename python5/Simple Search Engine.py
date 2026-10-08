documents = {
    1: "Python is a programming language",
    2: "Flutter builds mobile applications",
    3: "Machine learning uses data",
    4: "FastAPI creates APIs"
}

query = input("Search: ").lower()

for doc_id, text in documents.items():
    if query in text.lower():
        print(doc_id, "->", text)