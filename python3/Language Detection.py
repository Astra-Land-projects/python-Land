from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "Hello how are you",
    "I love programming",
    "Bonjour comment allez vous",
    "Je suis étudiant",
    "Hallo wie geht es dir",
    "Ich lerne Deutsch",
    "سلام حالت چطوره",
    "من برنامه نویسی دوست دارم"
]

labels = [
    "English",
    "English",
    "French",
    "French",
    "German",
    "German",
    "Persian",
    "Persian"
]

vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2, 5)
)

X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

while True:
    text = input("\nEnter text (q to quit): ")

    if text.lower() == "q":
        break

    X_test = vectorizer.transform([text])
    prediction = model.predict(X_test)

    print("Language:", prediction[0])