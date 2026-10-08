import pyttsx3


engine = pyttsx3.init()

engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)


print("Text To Speech")
print("Type 'exit' to stop.")

while True:
    text = input("\nText: ")

    if text.lower() == "exit":
        break

    engine.say(text)
    engine.runAndWait()