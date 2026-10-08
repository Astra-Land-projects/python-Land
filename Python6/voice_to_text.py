from faster_whisper import WhisperModel
from pathlib import Path
import sys


# ==============================
# CONFIGURATION
# ==============================

MODEL_SIZE = "small"
DEVICE = "cpu"
COMPUTE_TYPE = "int8"

LANGUAGES = {
    "1": ("fa", "Persian"),
    "2": ("en", "English"),
    "3": (None, "Auto Detect")
}


# ==============================
# FUNCTIONS
# ==============================

def load_model():
    print("\n🧠 Loading Whisper model...")
    print("This may take a while the first time.\n")

    try:
        model = WhisperModel(
            MODEL_SIZE,
            device=DEVICE,
            compute_type=COMPUTE_TYPE
        )

        print("✅ Model loaded successfully!")
        return model

    except Exception as error:
        print(f"❌ Could not load model.")
        print(f"Details: {error}")
        sys.exit(1)


def choose_language():
    print("\n🌍 Select language:")
    print("1. 🇮🇷 Persian")
    print("2. 🇬🇧 English")
    print("3. 🌎 Auto Detect")

    choice = input("\n> ").strip()

    return LANGUAGES.get(choice, LANGUAGES["3"])[0]


def choose_audio():
    while True:
        path = input("\n🎵 Enter audio file path:\n> ").strip()

        if not path:
            print("❌ Please enter a file path.")
            continue

        path = Path(path)

        if not path.exists():
            print("❌ File not found.")
            continue

        if not path.is_file():
            print("❌ This is not a file.")
            continue

        return path


def transcribe(model, audio_file, language):
    print("\n🎙️ Transcribing...")
    print("Please wait...\n")

    try:
        segments, info = model.transcribe(
            str(audio_file),
            language=language,
            beam_size=5,
            vad_filter=True
        )

        text_parts = []

        for segment in segments:
            text_parts.append(segment.text.strip())

        text = " ".join(text_parts).strip()

        if not text:
            print("⚠️ No speech was detected.")
            return None

        return text

    except Exception as error:
        print("❌ Transcription failed.")
        print(f"Details: {error}")
        return None


def save_text(audio_file, text):
    output_file = audio_file.with_suffix(".txt")

    try:
        output_file.write_text(
            text,
            encoding="utf-8"
        )

        return output_file

    except Exception as error:
        print(f"⚠️ Could not save text file: {error}")
        return None


# ==============================
# MAIN
# ==============================

def main():

    print("=" * 55)
    print("             ASTRA VOICE → TEXT")
    print("=" * 55)

    print("\n🎧 Supported common audio formats:")
    print("MP3 | WAV | M4A | FLAC | OGG")

    audio_file = choose_audio()

    language = choose_language()

    model = load_model()

    text = transcribe(
        model,
        audio_file,
        language
    )

    if text is None:
        return

    print("\n" + "=" * 55)
    print("📝 TRANSCRIPTION")
    print("=" * 55)

    print("\n" + text)

    output_file = save_text(
        audio_file,
        text
    )

    if output_file:
        print("\n" + "=" * 55)
        print("✅ Completed successfully!")
        print(f"📄 Text file: {output_file.resolve()}")
        print("=" * 55)


if __name__ == "__main__":
    main()