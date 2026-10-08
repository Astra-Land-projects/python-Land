import pyttsx3

e = pyttsx3.init()
while True:
    text = input("Text (exit): ")
    if text == "exit": break
    e.say(text)
    e.runAndWait()