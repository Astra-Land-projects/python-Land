#pip install openai pillow opencv-python#
#$env:OPENAI_API_KEY="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"#
import os
import sys
import base64
import mimetypes
import tempfile
from pathlib import Path

from openai import OpenAI
from PIL import Image
import cv2


# ============================================================
# ASTRA MULTIMODAL ANALYZER
# Image / Audio / Video → AI Description & Summary
# ============================================================

MODEL = "gpt-5.6-luna"
TRANSCRIBE_MODEL = "gpt-4o-transcribe"

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif"
}

AUDIO_EXTENSIONS = {
    ".mp3", ".wav", ".m4a", ".mp4",
    ".mpeg", ".mpga", ".ogg", ".webm"
}

VIDEO_EXTENSIONS = {
    ".mp4", ".mov", ".avi", ".mkv",
    ".webm", ".m4v"
}


# ============================================================
# CLIENT
# ============================================================

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("\n❌ OPENAI_API_KEY was not found.")
        print("Set your API key first.")
        print('Example:')
        print('export OPENAI_API_KEY="YOUR_API_KEY"')
        sys.exit(1)

    return OpenAI(api_key=api_key)


# ============================================================
# UI
# ============================================================

def banner():
    print("\n" + "=" * 65)
    print("                 ASTRA MULTIMODAL AI")
    print("=" * 65)
    print("        🖼️ Image  |  🎵 Audio  |  🎬 Video")
    print("=" * 65)


def choose_task():
    print("\nChoose an operation:\n")

    print("1. 📝 Describe")
    print("2. 📋 Summarize")
    print("3. 🔍 Analyze")
    print("4. ❓ Ask a question")

    choice = input("\n> ").strip()

    tasks = {
        "1": "describe",
        "2": "summarize",
        "3": "analyze",
        "4": "question"
    }

    return tasks.get(choice, "describe")


def choose_file():
    while True:
        path = input("\n📂 Enter file path:\n> ").strip()

        if not path:
            print("❌ File path cannot be empty.")
            continue

        path = Path(path).expanduser()

        if not path.exists():
            print("❌ File does not exist.")
            continue

        if not path.is_file():
            print("❌ This is not a file.")
            continue

        return path


def ask_question():
    question = input("\n❓ What do you want to know?\n> ").strip()

    if not question:
        return "Describe and analyze the provided content."

    return question


# ============================================================
# PROMPTS
# ============================================================

def build_prompt(task, question=None):
    if task == "describe":
        return """
Describe this content accurately and naturally.

For an image:
- Describe the main scene.
- Identify important visible objects.
- Describe people only using visible, non-sensitive characteristics.
- Describe environment, actions, colors and important details.
- Read visible text when possible.

For audio:
- Focus on the spoken content.

For video:
- Describe the major visual events and scenes.

Do not invent information that cannot be determined.
Return a clear, detailed description.
"""

    if task == "summarize":
        return """
Create a useful summary of the provided content.

Focus on:
- Main subject
- Important events or information
- Key points
- Important visible or spoken details

Avoid unnecessary repetition.
Do not invent facts.
Return a concise but informative summary.
"""

    if task == "analyze":
        return """
Perform a detailed analysis of the provided content.

Identify:
- Main subject
- Important objects or events
- Context
- Visible/spoken information
- Important details
- Possible meaning or purpose when reasonably inferable

Clearly distinguish observations from assumptions.
Do not invent information.
"""

    if task == "question":
        return f"""
Answer the user's question about the provided content.

Question:
{question}

Use only information that can reasonably be obtained from the
provided content. If the answer cannot be determined, say so.
"""

    return "Describe the provided content accurately."


# ============================================================
# IMAGE
# ============================================================

def image_to_data_url(path):
    mime_type, _ = mimetypes.guess_type(path)

    if not mime_type:
        mime_type = "image/jpeg"

    with open(path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


def analyze_image(client, path, prompt):
    print("\n🖼️ Image detected.")
    print("🤖 Analyzing image...\n")

    # Validate image before sending
    try:
        with Image.open(path) as image:
            image.verify()
    except Exception:
        print("❌ Invalid or corrupted image.")
        return None

    image_data = image_to_data_url(path)

    response = client.responses.create(
        model=MODEL,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt
                    },
                    {
                        "type": "input_image",
                        "image_url": image_data,
                        "detail": "high"
                    }
                ]
            }
        ]
    )

    return response.output_text


# ============================================================
# AUDIO
# ============================================================

def transcribe_audio(client, path):
    print("\n🎵 Audio detected.")
    print("🎙️ Transcribing audio...\n")

    try:
        with open(path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model=TRANSCRIBE_MODEL,
                file=audio_file
            )

        return transcript.text

    except Exception as error:
        print(f"❌ Audio transcription failed: {error}")
        return None


def analyze_audio(client, path, prompt):
    transcript = transcribe_audio(client, path)

    if not transcript:
        return None

    print("🤖 Analyzing transcript...\n")

    response = client.responses.create(
        model=MODEL,
        input=[
            {
                "role": "user",
                "content": (
                    f"{prompt}\n\n"
                    "Here is the transcript of the audio:\n\n"
                    f"{transcript}"
                )
            }
        ]
    )

    return response.output_text, transcript


# ============================================================
# VIDEO
# ============================================================

def extract_video_frames(path, max_frames=8):
    print("\n🎬 Video detected.")
    print("🎞️ Extracting important frames...\n")

    cap = cv2.VideoCapture(str(path))

    if not cap.isOpened():
        raise RuntimeError("Could not open video.")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames <= 0:
        cap.release()
        raise RuntimeError("Could not determine video length.")

    frame_count = min(max_frames, total_frames)

    indexes = [
        int(i * (total_frames - 1) / max(frame_count - 1, 1))
        for i in range(frame_count)
    ]

    frames = []

    for index in indexes:
        cap.set(cv2.CAP_PROP_POS_FRAMES, index)

        success, frame = cap.read()

        if not success:
            continue

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(frame)

        temp = tempfile.NamedTemporaryFile(
            suffix=".jpg",
            delete=False
        )

        temp_path = Path(temp.name)
        temp.close()

        image.save(
            temp_path,
            format="JPEG",
            quality=85
        )

        frames.append(temp_path)

    cap.release()

    return frames


def analyze_video(client, path, prompt):
    try:
        frames = extract_video_frames(path)
    except Exception as error:
        print(f"❌ Video processing failed: {error}")
        return None

    if not frames:
        print("❌ No usable frames found.")
        return None

    print(f"📸 Extracted {len(frames)} frames.")
    print("🤖 Analyzing video...\n")

    content = [
        {
            "type": "input_text",
            "text": (
                prompt
                + "\n\n"
                "These images are frames sampled from the same video. "
                "Use them together to understand the video's visual "
                "content and sequence of events."
            )
        }
    ]

    for frame in frames:
        try:
            data_url = image_to_data_url(frame)

            content.append(
                {
                    "type": "input_image",
                    "image_url": data_url,
                    "detail": "low"
                }
            )

        except Exception:
            pass

    try:
        response = client.responses.create(
            model=MODEL,
            input=[
                {
                    "role": "user",
                    "content": content
                }
            ]
        )

        return response.output_text

    finally:
        for frame in frames:
            try:
                frame.unlink()
            except Exception:
                pass


# ============================================================
# SAVE RESULT
# ============================================================

def save_result(original_file, result):
    output_file = original_file.with_name(
        original_file.stem + "_analysis.txt"
    )

    try:
        output_file.write_text(
            result,
            encoding="utf-8"
        )

        return output_file

    except Exception as error:
        print(f"⚠️ Could not save result: {error}")
        return None


def save_transcript(original_file, transcript):
    output_file = original_file.with_name(
        original_file.stem + "_transcript.txt"
    )

    try:
        output_file.write_text(
            transcript,
            encoding="utf-8"
        )

        return output_file

    except Exception as error:
        print(f"⚠️ Could not save transcript: {error}")
        return None


# ============================================================
# MAIN
# ============================================================

def main():
    banner()

    client = get_client()

    task = choose_task()

    file_path = choose_file()

    question = None

    if task == "question":
        question = ask_question()

    prompt = build_prompt(
        task,
        question
    )

    extension = file_path.suffix.lower()

    try:

        # ---------------- IMAGE ----------------

        if extension in IMAGE_EXTENSIONS:

            result = analyze_image(
                client,
                file_path,
                prompt
            )

            transcript = None


        # ---------------- AUDIO ----------------

        elif extension in AUDIO_EXTENSIONS and extension not in VIDEO_EXTENSIONS:

            audio_result = analyze_audio(
                client,
                file_path,
                prompt
            )

            if audio_result is None:
                return

            result, transcript = audio_result


        # ---------------- VIDEO ----------------

        elif extension in VIDEO_EXTENSIONS:

            result = analyze_video(
                client,
                file_path,
                prompt
            )

            transcript = None


        else:
            print("\n❌ Unsupported file type.")
            print("\nSupported:")
            print("Images: JPG, JPEG, PNG, WEBP, GIF")
            print("Audio:  MP3, WAV, M4A, OGG, WEBM")
            print("Video:  MP4, MOV, AVI, MKV, WEBM")
            return

    except KeyboardInterrupt:
        print("\n\n⚠️ Operation cancelled.")
        return

    except Exception as error:
        print("\n❌ An error occurred.")
        print(f"Details: {error}")
        return

    if not result:
        print("\n❌ No result was returned.")
        return

    # ---------------- RESULT ----------------

    print("\n")
    print("=" * 65)
    print("                         RESULT")
    print("=" * 65)

    print("\n" + result)

    # ---------------- SAVE ----------------

    output_file = save_result(
        file_path,
        result
    )

    if transcript:
        transcript_file = save_transcript(
            file_path,
            transcript
        )
    else:
        transcript_file = None

    print("\n" + "=" * 65)
    print("                         DONE")
    print("=" * 65)

    if output_file:
        print(f"\n📄 Analysis: {output_file.resolve()}")

    if transcript_file:
        print(f"🎙️ Transcript: {transcript_file.resolve()}")

    print("\n🚀 Astra Multimodal AI finished successfully.")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
    #python main.py#