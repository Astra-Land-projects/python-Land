#pip install --upgrade openai pillow opencv-python#

import sys
import base64
import mimetypes
import tempfile
from pathlib import Path

import cv2
from PIL import Image
from openai import OpenAI


# ============================================================
# ASTRA MULTIMODAL AI
# Image / Audio / Video Analyzer
# ============================================================

VISION_MODEL = "gpt-5.6-luna"
TRANSCRIPTION_MODEL = "gpt-4o-transcribe"

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif"
}

AUDIO_EXTENSIONS = {
    ".mp3", ".wav", ".m4a", ".mpeg",
    ".mpga", ".ogg", ".webm"
}

VIDEO_EXTENSIONS = {
    ".mp4", ".mov", ".avi", ".mkv",
    ".webm", ".m4v"
}


# ============================================================
# CLIENT
# ============================================================

def create_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("\n❌ OPENAI_API_KEY is not set.")
        print("\nSet your API key first:")
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
    print("          Image • Audio • Video Analyzer")
    print("=" * 65)


def choose_operation():
    print("\nChoose an operation:\n")
    print("1. 📝 Describe")
    print("2. 📋 Summarize")
    print("3. 🔍 Analyze")
    print("4. ❓ Ask a question")

    choice = input("\n> ").strip()

    operations = {
        "1": "describe",
        "2": "summarize",
        "3": "analyze",
        "4": "question"
    }

    return operations.get(choice, "describe")


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
            print("❌ This path is not a file.")
            continue

        return path


def choose_question():
    question = input("\n❓ Ask something about the file:\n> ").strip()

    if not question:
        return "Describe the provided content."

    return question


# ============================================================
# PROMPTS
# ============================================================

def create_prompt(operation, question=None):

    if operation == "describe":
        return """
Describe the provided content clearly and accurately.

For images:
- Describe the main scene.
- Identify important visible objects.
- Describe actions and environment.
- Describe colors and relevant visual details.
- Read visible text when possible.
- Do not identify a person's identity.
- Do not infer sensitive personal information.

For audio:
- Focus on the spoken content.

For video:
- Describe the important visual scenes and events.

Do not invent information.
Clearly separate observations from assumptions.
"""

    if operation == "summarize":
        return """
Summarize the provided content.

Focus on:
- Main subject
- Most important information
- Important events
- Key points
- Relevant details

Keep the summary concise but useful.
Do not invent information.
"""

    if operation == "analyze":
        return """
Perform a detailed analysis of the provided content.

Include:
- Main subject
- Important objects or events
- Context
- Key information
- Important details
- Reasonable conclusions

Clearly distinguish observations from assumptions.
Do not invent information.
"""

    if operation == "question":
        return f"""
Answer the following question using the provided content.

Question:
{question}

Only use information that can reasonably be determined
from the provided content.

If the answer cannot be determined, clearly say so.
"""

    return "Describe the provided content accurately."


# ============================================================
# IMAGE HELPERS
# ============================================================

def validate_image(path):
    try:
        with Image.open(path) as image:
            image.verify()

        return True

    except Exception:
        return False


def image_to_data_url(path):
    mime_type, _ = mimetypes.guess_type(str(path))

    if not mime_type:
        mime_type = "image/jpeg"

    with open(path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


# ============================================================
# IMAGE ANALYSIS
# ============================================================

def analyze_image(client, path, prompt):

    print("\n🖼️ Image detected.")
    print("🤖 Sending image to AI...\n")

    if not validate_image(path):
        print("❌ Invalid or corrupted image.")
        return None

    image_data = image_to_data_url(path)

    response = client.responses.create(
        model=VISION_MODEL,
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
# AUDIO TRANSCRIPTION
# ============================================================

def transcribe_audio(client, path):

    print("\n🎙️ Transcribing audio...")
    print("⏳ Please wait...\n")

    try:
        with open(path, "rb") as audio_file:

            result = client.audio.transcriptions.create(
                model=TRANSCRIPTION_MODEL,
                file=audio_file
            )

        return result.text

    except Exception as error:

        print("\n❌ Transcription failed.")
        print(f"Details: {error}")

        return None


# ============================================================
# AUDIO ANALYSIS
# ============================================================

def analyze_audio(client, path, prompt):

    print("\n🎵 Audio detected.")

    transcript = transcribe_audio(
        client,
        path
    )

    if not transcript:
        return None, None

    print("🤖 Analyzing transcript...\n")

    response = client.responses.create(
        model=VISION_MODEL,
        input=[
            {
                "role": "user",
                "content": (
                    prompt
                    + "\n\n"
                    + "TRANSCRIPT:\n"
                    + transcript
                )
            }
        ]
    )

    return response.output_text, transcript


# ============================================================
# VIDEO FRAME EXTRACTION
# ============================================================

def extract_video_frames(path, max_frames=10):

    print("\n🎬 Video detected.")
    print("🎞️ Extracting representative frames...\n")

    video = cv2.VideoCapture(str(path))

    if not video.isOpened():
        raise RuntimeError(
            "Could not open the video."
        )

    total_frames = int(
        video.get(cv2.CAP_PROP_FRAME_COUNT)
    )

    if total_frames <= 0:
        video.release()

        raise RuntimeError(
            "Could not determine video length."
        )

    number_of_frames = min(
        max_frames,
        total_frames
    )

    if number_of_frames == 1:
        indexes = [0]

    else:
        indexes = [
            int(
                i * (total_frames - 1)
                / (number_of_frames - 1)
            )
            for i in range(number_of_frames)
        ]

    extracted = []

    for index in indexes:

        video.set(
            cv2.CAP_PROP_POS_FRAMES,
            index
        )

        success, frame = video.read()

        if not success:
            continue

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        image = Image.fromarray(frame)

        temp = tempfile.NamedTemporaryFile(
            suffix=".jpg",
            delete=False
        )

        temp_path = Path(temp.name)

        temp.close()

        image.save(
            temp_path,
            "JPEG",
            quality=85
        )

        extracted.append(temp_path)

    video.release()

    return extracted


# ============================================================
# VIDEO ANALYSIS
# ============================================================

def analyze_video(client, path, prompt):

    try:
        frames = extract_video_frames(
            path,
            max_frames=10
        )

    except Exception as error:

        print("\n❌ Video processing failed.")
        print(f"Details: {error}")

        return None

    if not frames:
        print("❌ No usable frames were extracted.")
        return None

    print(
        f"📸 Extracted {len(frames)} representative frames."
    )

    print("🤖 Analyzing video...\n")

    content = [
        {
            "type": "input_text",
            "text": (
                prompt
                + "\n\n"
                + "The following images are representative "
                + "frames sampled from the same video. "
                + "Analyze them together and infer the "
                + "sequence of visible events only when "
                + "supported by the frames."
            )
        }
    ]

    for frame in frames:

        try:

            data_url = image_to_data_url(
                frame
            )

            content.append(
                {
                    "type": "input_image",
                    "image_url": data_url,
                    "detail": "low"
                }
            )

        except Exception:
            continue

    try:

        response = client.responses.create(
            model=VISION_MODEL,
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
# SAVE OUTPUT
# ============================================================

def save_analysis(original_file, result):

    output = original_file.with_name(
        original_file.stem
        + "_analysis.txt"
    )

    try:

        output.write_text(
            result,
            encoding="utf-8"
        )

        return output

    except Exception as error:

        print(
            f"⚠️ Could not save analysis: {error}"
        )

        return None


def save_transcript(original_file, transcript):

    output = original_file.with_name(
        original_file.stem
        + "_transcript.txt"
    )

    try:

        output.write_text(
            transcript,
            encoding="utf-8"
        )

        return output

    except Exception as error:

        print(
            f"⚠️ Could not save transcript: {error}"
        )

        return None


# ============================================================
# MAIN
# ============================================================

def main():

    banner()

    client = create_client()

    operation = choose_operation()

    file_path = choose_file()

    question = None

    if operation == "question":
        question = choose_question()

    prompt = create_prompt(
        operation,
        question
    )

    extension = file_path.suffix.lower()

    result = None
    transcript = None

    try:

        # ====================================================
        # IMAGE
        # ====================================================

        if extension in IMAGE_EXTENSIONS:

            result = analyze_image(
                client,
                file_path,
                prompt
            )


        # ====================================================
        # AUDIO
        # ====================================================

        elif extension in AUDIO_EXTENSIONS:

            result, transcript = analyze_audio(
                client,
                file_path,
                prompt
            )


        # ====================================================
        # VIDEO
        # ====================================================

        elif extension in VIDEO_EXTENSIONS:

            result = analyze_video(
                client,
                file_path,
                prompt
            )


        # ====================================================
        # UNKNOWN
        # ====================================================

        else:

            print("\n❌ Unsupported file type.")

            print("\nSupported image formats:")
            print("JPG, JPEG, PNG, WEBP, GIF")

            print("\nSupported audio formats:")
            print("MP3, WAV, M4A, MPEG, MPGA, OGG, WEBM")

            print("\nSupported video formats:")
            print("MP4, MOV, AVI, MKV, WEBM, M4V")

            return

    except KeyboardInterrupt:

        print("\n\n⚠️ Operation cancelled.")

        return

    except Exception as error:

        print("\n❌ API / processing error.")
        print(f"Details: {error}")

        return

    if not result:

        print("\n❌ No result was generated.")

        return

    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    print("\n")
    print("=" * 65)
    print("                         RESULT")
    print("=" * 65)

    print("\n" + result)

    # ========================================================
    # SAVE ANALYSIS
    # ========================================================

    analysis_file = save_analysis(
        file_path,
        result
    )

    transcript_file = None

    if transcript:

        transcript_file = save_transcript(
            file_path,
            transcript
        )

    # ========================================================
    # FINAL
    # ========================================================

    print("\n" + "=" * 65)
    print("                         COMPLETE")
    print("=" * 65)

    if analysis_file:

        print(
            f"\n📄 Analysis saved to:"
            f"\n{analysis_file.resolve()}"
        )

    if transcript_file:

        print(
            f"\n🎙️ Transcript saved to:"
            f"\n{transcript_file.resolve()}"
        )

    print(
        "\n🚀 Astra Multimodal AI finished successfully."
    )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()