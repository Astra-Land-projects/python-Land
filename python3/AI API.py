import os

from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel


app = FastAPI(title="AI API")


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


class Question(BaseModel):
    text: str


@app.post("/ask")
def ask_ai(question: Question):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": question.text
            }
        ]
    )

    answer = (
        response
        .choices[0]
        .message
        .content
    )

    return {
        "question": question.text,
        "answer": answer
    }