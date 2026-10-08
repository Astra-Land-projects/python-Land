from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI(
    title="Astra AI Assistant"
)


# -------------------------
# Knowledge Base
# -------------------------

files = list(
    Path("knowledge").glob("*.txt")
)

documents = [
    file.read_text(
        encoding="utf-8"
    )
    for file in files
]

if documents:

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    matrix = vectorizer.fit_transform(
        documents
    )

else:

    vectorizer = None
    matrix = None


# -------------------------
# Request
# -------------------------

class Question(BaseModel):

    question: str


# -------------------------
# Search
# -------------------------

def search(question):

    if not documents:
        return []

    query = vectorizer.transform(
        [question]
    )

    scores = cosine_similarity(
        query,
        matrix
    )[0]

    indexes = scores.argsort()[::-1][:3]

    return [
        {
            "score":
                float(scores[i]),

            "context":
                documents[i][:1000]
        }

        for i in indexes
    ]


# -------------------------
# Routes
# -------------------------

@app.get("/")
def home():

    return {
        "name":
            "Astra AI Assistant",

        "status":
            "online"
    }


@app.get("/health")
def health():

    return {
        "status":
            "healthy"
    }


@app.post("/ask")
def ask(data: Question):

    results = search(
        data.question
    )

    return {
        "question":
            data.question,

        "results":
            results
    }