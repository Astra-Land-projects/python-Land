from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = [
    "The Matrix science fiction action",
    "Inception science fiction thriller",
    "Titanic romance drama",
    "Interstellar science fiction drama",
    "Avengers action superhero",
    "The Notebook romance drama"
]

vectorizer = TfidfVectorizer()

matrix = vectorizer.fit_transform(movies)

similarity = cosine_similarity(matrix)


def recommend(index, count=3):

    scores = list(enumerate(similarity[index]))

    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    for i, score in scores[1:count+1]:
        print(
            f"{movies[i]} ({score:.2f})"
        )


for i, movie in enumerate(movies):
    print(i, movie)

index = int(input("Movie number: "))

recommend(index)