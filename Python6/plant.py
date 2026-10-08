#pip install --upgrade openai pillow#
#export OPENAI_API_KEY="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"#
import os
import sys
import base64
import mimetypes
from pathlib import Path

from PIL import Image
from openai import OpenAI


# ============================================================
# ASTRA PLANT DOCTOR
# AI Plant Identification & Health Analysis
# ============================================================

MODEL = "gpt-5.6-luna"

SUPPORTED_IMAGES = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".gif"
}


# ============================================================
# CLIENT
# ============================================================

def create_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("\n❌ OPENAI_API_KEY is not set.")
        print("\nSet it first:")
        print('export OPENAI_API_KEY="YOUR_API_KEY"')
        sys.exit(1)

    return OpenAI(api_key=api_key)


# ============================================================
# UI
# ============================================================

def banner():

    print("\n" + "=" * 70)
    print("                    🌱 ASTRA PLANT DOCTOR")
    print("=" * 70)
    print("           AI Plant Identification & Health Analysis")
    print("=" * 70)


def get_image():

    while True:

        path = input("\n📸 Enter plant image path:\n> ").strip()

        if not path:
            print("❌ Please enter an image path.")
            continue

        path = Path(path).expanduser()

        if not path.exists():
            print("❌ File not found.")
            continue

        if not path.is_file():
            print("❌ This is not a file.")
            continue

        if path.suffix.lower() not in SUPPORTED_IMAGES:
            print("❌ Unsupported image format.")
            print("Supported: JPG, JPEG, PNG, WEBP, GIF")
            continue

        return path


# ============================================================
# IMAGE VALIDATION
# ============================================================

def validate_image(path):

    try:

        with Image.open(path) as image:
            image.verify()

        return True

    except Exception:

        return False


# ============================================================
# IMAGE → DATA URL
# ============================================================

def image_to_data_url(path):

    mime_type, _ = mimetypes.guess_type(str(path))

    if not mime_type:
        mime_type = "image/jpeg"

    with open(path, "rb") as file:

        encoded = base64.b64encode(
            file.read()
        ).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


# ============================================================
# PLANT ANALYSIS PROMPT
# ============================================================

def create_prompt():

    return """
You are Astra Plant Doctor, an AI assistant specialized in
plant identification, plant care, and visual plant-health assessment.

Analyze the provided plant image carefully.

Your job is to provide a practical plant-care report.

IMPORTANT RULES:

1. Do not claim certainty when the image does not provide
   enough evidence.

2. If plant identification is uncertain, provide the most
   likely candidates and explain the uncertainty.

3. Do not diagnose a plant disease with absolute certainty
   from an image alone.

4. Distinguish clearly between:
   - Visible observations
   - Possible causes
   - Recommendations

5. Do not invent environmental measurements such as temperature,
   humidity, soil moisture, or light level from the image.

6. If additional information is required, explicitly say what
   information would improve the assessment.

Analyze the following categories:

------------------------------------------------------------
PLANT IDENTIFICATION
------------------------------------------------------------

- Common name
- Scientific name if reasonably identifiable
- Identification confidence from 0-100%
- Possible alternatives if uncertain

------------------------------------------------------------
HEALTH ASSESSMENT
------------------------------------------------------------

- Overall health:
  Healthy / Possibly stressed / Possibly unhealthy / Unclear
- Health confidence
- Visible symptoms
- Leaf condition
- Stem condition
- Color abnormalities
- Signs of pests if visible
- Signs of fungal/bacterial problems if visually plausible
- Signs of water stress if visually plausible
- Signs of nutrient deficiency if visually plausible

------------------------------------------------------------
ENVIRONMENT & CARE
------------------------------------------------------------

Give practical recommendations for the identified plant:

- Light requirements
- Direct vs indirect light
- Approximate daily light duration
- Temperature range
- Humidity preference
- Watering frequency/rules
- Soil moisture preference
- Soil type/drainage
- Pot/drainage recommendations
- Fertilizer requirements
- Fertilizing frequency
- Repotting guidance
- Pruning guidance

Do not present exact environmental numbers as facts if
the species cannot be identified reliably.

------------------------------------------------------------
CARE PLAN
------------------------------------------------------------

Create:

DAILY:
- What should be checked?

WEEKLY:
- What should be checked?
- What maintenance may be needed?

MONTHLY:
- What should be checked?
- Fertilizer/repotting/pruning considerations

------------------------------------------------------------
WARNING SIGNS
------------------------------------------------------------

List symptoms that would indicate the plant is getting worse
and what the owner should check.

------------------------------------------------------------
FINAL ASSESSMENT
------------------------------------------------------------

End with:

Health:
Identification:
Main concern:
Most important action:
Confidence:

Keep the report practical and easy to understand.
"""


# ============================================================
# ANALYZE PLANT
# ============================================================

def analyze_plant(client, image_path):

    print("\n🌱 Plant image detected.")
    print("🔬 Analyzing plant...")
    print("⏳ Please wait...\n")

    image_data = image_to_data_url(image_path)

    response = client.responses.create(
        model=MODEL,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": create_prompt()
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
# SAVE REPORT
# ============================================================

def save_report(image_path, report):

    output = image_path.with_name(
        image_path.stem + "_plant_report.txt"
    )

    try:

        output.write_text(
            report,
            encoding="utf-8"
        )

        return output

    except Exception as error:

        print(
            f"\n⚠️ Could not save report: {error}"
        )

        return None


# ============================================================
# MAIN
# ============================================================

def main():

    banner()

    client = create_client()

    image_path = get_image()

    if not validate_image(image_path):

        print("\n❌ The image appears to be invalid or corrupted.")
        return

    try:

        report = analyze_plant(
            client,
            image_path
        )

    except Exception as error:

        print("\n❌ AI analysis failed.")
        print(f"Details: {error}")
        return

    if not report:

        print("\n❌ No report was returned.")
        return

    # ========================================================
    # DISPLAY
    # ========================================================

    print("\n")
    print("=" * 70)
    print("                       🌱 PLANT REPORT")
    print("=" * 70)

    print("\n" + report)

    # ========================================================
    # SAVE
    # ========================================================

    report_file = save_report(
        image_path,
        report
    )

    print("\n" + "=" * 70)
    print("                         COMPLETE")
    print("=" * 70)

    if report_file:

        print(
            "\n📄 Report saved:"
            f"\n{report_file.resolve()}"
        )

    print("\n🌱 Astra Plant Doctor finished successfully.")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
    #python main.py#