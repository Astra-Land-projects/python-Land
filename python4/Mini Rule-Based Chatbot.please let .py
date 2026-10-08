# project_198_chatbot.py

while True:
    msg = input("You: ").lower()

    if "hello" in msg:
        print("Bot: Hello!")
    elif "how are you" in msg:
        print("Bot: I'm fine.")
    elif "python" in msg:
        print("Bot: Python is great.")
    elif "bye" in msg:
        print("Bot: Bye!")
        break
    else:
        print("Bot: I don't know.")