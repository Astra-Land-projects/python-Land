from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Blog API")


class Post(BaseModel):
    title: str
    content: str


posts = []


@app.get("/")
def home():
    return {"message": "Blog API is running"}


@app.get("/posts")
def get_posts():
    return posts


@app.post("/posts")
def create_post(post: Post):
    new_post = {
        "id": len(posts) + 1,
        "title": post.title,
        "content": post.content
    }

    posts.append(new_post)

    return new_post


@app.get("/posts/{post_id}")
def get_post(post_id: int):

    for post in posts:
        if post["id"] == post_id:
            return post

    return {"error": "Post not found"}