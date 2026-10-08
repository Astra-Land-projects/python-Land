import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Question(BaseModel):
    text: str

@app.post("/ask")
def ask(q: Question):
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": q.text}]
    )
    return {"answer": r.choices[0].message.content}