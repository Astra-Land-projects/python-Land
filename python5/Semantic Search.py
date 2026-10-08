from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = ["Python for AI", "FastAPI for APIs", "Flutter for mobile", "Git for version control"]
v = TfidfVectorizer(stop_words="english")
m = v.fit_transform(docs)

while True:
    q = input("Search (exit): ")
    if q == "exit": break
    s = cosine_similarity(v.transform([q]), m)[0]
    for i in s.argsort()[::-1]:
        if s[i] > 0:
            print(f"{s[i]:.3f} -> {docs[i]}")