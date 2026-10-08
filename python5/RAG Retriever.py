from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

chunks = [
    "Python is great for automation.",
    "FastAPI builds modern APIs.",
    "TensorFlow is used for deep learning.",
]

v = TfidfVectorizer(stop_words="english")
m = v.fit_transform(chunks)

while True:
    q = input("Question (exit): ")
    if q == "exit": break
    scores = cosine_similarity(v.transform([q]), m)[0]
    best = scores.argmax()
    print("Context:", chunks[best])