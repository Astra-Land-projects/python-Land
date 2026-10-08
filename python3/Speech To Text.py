import speech_recognition as sr

recognizer = sr.Recognizer()


def speech_to_text():
    with sr.Microphone() as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(
            audio,
            language="en-US"
        )

        return text

    except sr.UnknownValueError:
        return "Could not understand speech."

    except sr.RequestError as error:
        return f"Service error: {error}"


result = speech_to_text()

print("\nRecognized text:")
print(result)