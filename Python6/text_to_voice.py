from gtts import gTTS
from pathlib import Path


def main():
    print("=" * 45)
    print("        TEXT → VOICE CONVERTER")
    print("=" * 45)

    text = input("\n📝 Enter your text:\n> ").strip()

    if not text:
        print("❌ Text cannot be empty.")
        return

    print("\n🌍 Select language:")
    print("1. English")
    print("2. Persian")

    language = input("> ").strip()

    languages = {
        "1": "en",
        "2": "fa"
    }

    if language not in languages:
        print("❌ Invalid language.")
        return

    filename = input("\n💾 Enter output filename (without .mp3):\n> ").strip()

    if not filename:
        filename = "output"

    # Remove .mp3 if the user already typed it
    if filename.lower().endswith(".mp3"):
        filename = filename[:-4]

    output = Path(f"{filename}.mp3")

    try:
        print("\n⏳ Converting text to voice...")

        tts = gTTS(
            text=text,
            lang=languages[language],
            slow=False
        )

        tts.save(output)

        print("\n" + "=" * 45)
        print("✅ Conversion completed successfully!")
        print(f"🎵 File: {output.resolve()}")
        print("=" * 45)

    except Exception as error:
        print("\n❌ An error occurred.")
        print(f"Details: {error}")


if __name__ == "__main__":
    main()