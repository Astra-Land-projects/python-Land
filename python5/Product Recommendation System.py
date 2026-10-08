from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

products = [
    "gaming laptop computer",
    "office laptop computer",
    "wireless gaming mouse",
    "mechanical gaming keyboard",
    "smartphone android",
    "wireless headphones"
]

vectorizer = TfidfVectorizer()

matrix = vectorizer.fit_transform(products)

similarity = cosine_similarity(matrix)

query = input("What product do you want? ")

q = vectorizer.transform([query])

scores = cosine_similarity(q, matrix)[0]

for index in scores.argsort()[::-1][:3]:
    print(
        f"{products[index]} -> "
        f"{scores[index]:.2f}"
    )