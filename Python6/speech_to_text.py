import speech_recognition as sr


class SpeechToText:

    def listen(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(text)
        except Exception:
            print("Recognition Failed.")