from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Authentication API")


class User(BaseModel):
    username: str
    password: str


users = []


@app.post("/register")
def register(user: User):

    for existing in users:
        if existing["username"] == user.username:
            return {"error": "Username already exists"}

    users.append({
        "username": user.username,
        "password": user.password
    })

    return {
        "message": "User registered successfully"
    }


@app.post("/login")
def login(user: User):

    for existing in users:

        if (
            existing["username"] == user.username
            and existing["password"] == user.password
        ):
            return {
                "message": "Login successful"
            }

    return {
        "error": "Invalid username or password"
    }