from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Notification API"
)


class Notification(BaseModel):
    user: str
    message: str


notifications = []


@app.post("/notifications")
def create_notification(
    notification: Notification
):

    item = {
        "id": len(notifications) + 1,
        "user": notification.user,
        "message": notification.message,
        "read": False
    }

    notifications.append(item)

    return item


@app.get("/notifications/{user}")
def get_notifications(user: str):

    return [
        item
        for item in notifications
        if item["user"] == user
    ]


@app.patch(
    "/notifications/{notification_id}"
)
def mark_read(notification_id: int):

    for item in notifications:

        if item["id"] == notification_id:

            item["read"] = True

            return item

    return {
        "error": "Notification not found"
    }