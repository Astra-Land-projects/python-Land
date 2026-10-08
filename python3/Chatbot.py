import random
from datetime import datetime

responses = {
    "hello": [
        "Hello! 👋",
        "Hi! How can I help you?",
        "Hey! Nice to meet you."
    ],

    "how are you": [
        "I'm doing great!",
        "I'm fine, thanks!",
        "Ready to help you!"
    ],

    "name": [
        "I'm MiniBot.",
        "My name is MiniBot."
    ],

    "bye": [
        "Goodbye!",
        "See you later!",
        "Bye 👋"
    ]
}


def get_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return random.choice(responses["hello"])

    if "how are you" in message:
        return random.choice(responses["how are you"])

    if "your name" in message or "who are you" in message:
        return random.choice(responses["name"])

    if "time" in message:
        return f"Current time: {datetime.now().strftime('%H:%M:%S')}"

    if "bye" in message or "goodbye" in message:
        return random.choice(responses["bye"])

    return "I don't understand that yet."


print("MiniBot started!")
print("Type 'bye' to exit.")

while True:
    user = input("\nYou: ")

    if "bye" in user.lower():
        print("Bot:", get_response(user))
        break

    print("Bot:", get_response(user))