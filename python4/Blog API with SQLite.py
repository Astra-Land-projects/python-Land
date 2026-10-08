import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
db = sqlite3.connect("blog.db", check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT)")
db.commit()

class Post(BaseModel):
    title: str
    content: str

@app.get("/posts")
def posts():
    cur = db.execute("SELECT id, title, content FROM posts")
    return [{"id": i, "title": t, "content": c} for i, t, c in cur.fetchall()]

@app.post("/posts")
def add(post: Post):
    cur = db.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (post.title, post.content))
    db.commit()
    return {"id": cur.lastrowid, **post.model_dump()}