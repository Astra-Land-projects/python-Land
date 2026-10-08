from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from jose import jwt
import hashlib

app = FastAPI()
SECRET = "change-me"
ALG = "HS256"
users = {"arya": hashlib.sha256("1234".encode()).hexdigest()}

class Login(BaseModel):
    username: str
    password: str

def token(username):
    payload = {"sub": username, "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, SECRET, algorithm=ALG)

@app.post("/login")
def login(data: Login):
    if users.get(data.username) != hashlib.sha256(data.password.encode()).hexdigest():
        raise HTTPException(401, "invalid credentials")
    return {"access_token": token(data.username), "token_type": "bearer"}