from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = FastAPI()

texts = [
    "I love this product",
    "This is amazing",
    "I hate this",
    "This is terrible"
]

labels = [
    "positive",
    "positive",
    "negative",
    "negative"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

model = LogisticRegression()

model.fit(X, labels)


class TextRequest(BaseModel):
    text: str


@app.post("/classify")
def classify(data: TextRequest):

    X_new = vectorizer.transform(
        [data.text]
    )

    result = model.predict(X_new)[0]

    return {
        "classification": result
    }