from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException
from jose import jwt
from pydantic import BaseModel


app = FastAPI(title="JWT API")


SECRET_KEY = "change-this-secret"
ALGORITHM = "HS256"


class Login(BaseModel):
    username: str
    password: str


users = {
    "arya": "1234"
}


def create_token(username):

    payload = {
        "sub": username,
        "exp": datetime.utcnow()
        + timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


@app.post("/login")
def login(data: Login):

    if users.get(data.username) != data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_token(
        data.username
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }