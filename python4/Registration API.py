import sqlite3, hashlib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
db = sqlite3.connect("users.db", check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
db.commit()

class User(BaseModel):
    username: str
    password: str

def hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

@app.post("/register")
def register(user: User):
    try:
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, hash_pw(user.password)))
        db.commit()
        return {"message": "registered"}
    except sqlite3.IntegrityError:
        raise HTTPException(400, "username exists")