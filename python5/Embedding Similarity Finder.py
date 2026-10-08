from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

items = ["learn python", "build api", "train model", "write app"]
v = TfidfVectorizer()
m = v.fit_transform(items)

q = input("Query: ")
scores = cosine_similarity(v.transform([q]), m)[0]
for i in scores.argsort()[::-1]:
    if scores[i] > 0:
        print(f"{scores[i]:.3f}", items[i])