from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Task Manager API"
)


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = []


@app.post("/tasks")
def create_task(task: Task):

    item = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(item)

    return item


@app.get("/tasks")
def get_tasks():
    return tasks


@app.patch("/tasks/{task_id}")
def update_task(
    task_id: int,
    task: Task
):

    for item in tasks:

        if item["id"] == task_id:

            item["title"] = task.title
            item["completed"] = task.completed

            return item

    return {
        "error": "Task not found"
    }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for item in tasks:

        if item["id"] == task_id:

            tasks.remove(item)

            return {
                "message": "Task deleted"
            }

    return {
        "error": "Task not found"
    }