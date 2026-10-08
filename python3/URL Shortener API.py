import secrets

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="URL Shortener")


class URLRequest(BaseModel):
    url: str


urls = {}


@app.post("/shorten")
def shorten(data: URLRequest):

    code = secrets.token_urlsafe(5)

    urls[code] = data.url

    return {
        "code": code,
        "url": data.url
    }


@app.get("/urls")
def list_urls():
    return urls


@app.get("/url/{code}")
def get_url(code: str):

    if code not in urls:
        return {
            "error": "URL not found"
        }

    return {
        "url": urls[code]
    }