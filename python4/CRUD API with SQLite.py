import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
db = sqlite3.connect("app.db", check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, done INTEGER DEFAULT 0)")
db.commit()

class Task(BaseModel):
    title: str
    done: bool = False

@app.get("/tasks")
def list_tasks():
    cur = db.execute("SELECT id, title, done FROM tasks")
    return [{"id": i, "title": t, "done": bool(d)} for i, t, d in cur.fetchall()]

@app.post("/tasks")
def add_task(task: Task):
    cur = db.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (task.title, int(task.done)))
    db.commit()
    return {"id": cur.lastrowid, **task.model_dump()}

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    db.execute("UPDATE tasks SET title=?, done=? WHERE id=?", (task.title, int(task.done), task_id))
    db.commit()
    return {"message": "updated"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    db.commit()
    return {"message": "deleted"}