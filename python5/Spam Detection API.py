from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

spam_words = {
    "free",
    "winner",
    "prize",
    "money",
    "click",
    "offer"
}


class Message(BaseModel):
    text: str


@app.post("/detect")
def detect(message: Message):

    words = set(
        message.text.lower().split()
    )

    score = len(
        words & spam_words
    )

    return {
        "spam": score >= 2,
        "score": score
    }