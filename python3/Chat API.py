from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Chat API")


class Message(BaseModel):
    username: str
    text: str


messages = []


@app.post("/messages")
def send_message(message: Message):

    new_message = {
        "id": len(messages) + 1,
        "username": message.username,
        "text": message.text
    }

    messages.append(new_message)

    return new_message


@app.get("/messages")
def get_messages():
    return messages


@app.delete("/messages")
def delete_messages():

    messages.clear()

    return {
        "message": "Messages deleted"
    }