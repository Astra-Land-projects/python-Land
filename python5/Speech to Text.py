import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak...")
    audio = r.listen(source)
print(r.recognize_google(audio, language="en-US"))