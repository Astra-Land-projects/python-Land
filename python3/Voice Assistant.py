import datetime
import webbrowser

try:
    import speech_recognition as sr
    import pyttsx3
except ImportError:
    print("Install:")
    print("pip install SpeechRecognition pyttsx3")
    raise


engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except sr.UnknownValueError:
        speak("I couldn't understand you.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""


def command(text):
    if "hello" in text:
        speak("Hello! How can I help you?")

    elif "time" in text:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "open google" in text:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open youtube" in text:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "exit" in text or "stop" in text:
        speak("Goodbye!")
        return False

    else:
        speak("I don't know that command yet.")

    return True


speak("Voice assistant started.")

while True:
    user_command = listen()

    if user_command and not command(user_command):
        break