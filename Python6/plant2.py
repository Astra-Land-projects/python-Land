import os
import sys
import json
import argparse

import torch
from PIL import Image
from transformers import (
    Qwen2_5_VLForConditionalGeneration,
    AutoProcessor,
)
from qwen_vl_utils import process_vision_info


# ============================================================
# ASTRA PLANT DOCTOR
# Offline AI Plant Analyzer
# ============================================================

MODEL_NAME = "Qwen/Qwen2.5-VL-3B-Instruct"


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def print_header():
    print("\n" + "=" * 70)
    print("🌱 ASTRA PLANT DOCTOR")
    print("Offline AI Plant Health Analyzer")
    print("=" * 70)


def check_image(path):
    if not os.path.exists(path):
        print(f"❌ Image not found: {path}")
        sys.exit(1)

    try:
        image = Image.open(path)
        image.verify()
    except Exception:
        print("❌ The selected file is not a valid image.")
        sys.exit(1)


def load_model():
    print("\n🧠 Loading local AI model...")
    print(f"Model: {MODEL_NAME}")
    print("This may take some time on the first run.\n")

    processor = AutoProcessor.from_pretrained(
        MODEL_NAME,
        min_pixels=256 * 28 * 28,
        max_pixels=768 * 28 * 28,
    )

    if torch.cuda.is_available():
        print("🚀 CUDA GPU detected.")

        model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.bfloat16,
            device_map="auto",
        )

    else:
        print("💻 Running on CPU.")
        print("⚠️ CPU inference can be slow.")

        model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float32,
            device_map="auto",
        )

    return model, processor


# ------------------------------------------------------------
# Plant analysis prompt
# ------------------------------------------------------------

SYSTEM_PROMPT = """
You are ASTRA Plant Doctor, an offline AI plant analysis assistant.

Analyze the provided plant image carefully.

Your task is to provide a practical plant-care report.

You MUST distinguish between:
1. Things clearly visible in the image.
2. Things that are probable.
3. Things that cannot reliably be determined from the image.

Never pretend that a diagnosis is certain when it is not.

Analyze:

- Plant identification
- Scientific name if reasonably identifiable
- Overall health
- Visible symptoms
- Possible diseases
- Possible pests
- Possible nutrient deficiencies
- Possible environmental stress
- Leaf condition
- Stem condition
- Soil condition if visible
- Pot condition if visible
- Signs of overwatering
- Signs of underwatering
- Light requirements
- Temperature requirements
- Humidity requirements
- Watering recommendation
- Soil recommendation
- Fertilizer recommendation
- Pruning recommendation
- General care plan
- Immediate actions
- Warning signs that require further inspection

IMPORTANT:

Do not invent exact temperature, humidity, watering frequency,
or fertilizer dosage if the species cannot be identified confidently.

Use ranges and explain uncertainty.

The answer must be practical and easy to understand.

Respond in Persian.

Use this structure:

🌱 IDENTIFICATION
- Common name:
- Scientific name:
- Identification confidence:

❤️ HEALTH
- Overall condition:
- Health confidence:

🔎 VISIBLE SYMPTOMS
- ...

🦠 POSSIBLE PROBLEMS
- Problem:
- Probability:
- Reason:

🐛 POSSIBLE PESTS
- ...

💧 WATER
- Recommendation:
- Warning signs:

☀️ LIGHT
- ...

🌡️ TEMPERATURE
- ...

💦 HUMIDITY
- ...

🪴 SOIL
- ...

🧪 FERTILIZER
- ...

✂️ PRUNING
- ...

📅 CARE PLAN
- Daily:
- Weekly:
- Monthly:

🚑 IMMEDIATE ACTIONS
1.
2.
3.

⚠️ IMPORTANT
Explain what cannot be reliably diagnosed from this image alone.
"""


# ------------------------------------------------------------
# AI analysis
# ------------------------------------------------------------

def analyze_plant(image_path, model, processor):

    image_uri = "file://" + os.path.abspath(image_path)

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": image_uri,
                },
                {
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                },
            ],
        }
    ]

    print("\n🔍 Analyzing plant...")
    print("Please wait...\n")

    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    image_inputs, video_inputs = process_vision_info(messages)

    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )

    # Move tensors to the model device
    if torch.cuda.is_available():
        inputs = inputs.to("cuda")
    else:
        inputs = inputs.to(model.device)

    with torch.no_grad():

        generated_ids = model.generate(
            **inputs,
            max_new_tokens=1400,
            do_sample=False,
        )

    generated_ids_trimmed = [
        output_ids[len(input_ids):]
        for input_ids, output_ids
        in zip(inputs.input_ids, generated_ids)
    ]

    result = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False,
    )

    return result[0].strip()


# ------------------------------------------------------------
# Save report
# ------------------------------------------------------------

def save_report(image_path, report):

    base_name = os.path.splitext(
        os.path.basename(image_path)
    )[0]

    output_file = f"{base_name}_plant_report.txt"

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("=" * 70 + "\n")
        file.write("ASTRA PLANT DOCTOR\n")
        file.write("Offline AI Plant Health Report\n")
        file.write("=" * 70 + "\n\n")

        file.write(report)

        file.write("\n\n")
        file.write("=" * 70 + "\n")
        file.write(
            "Generated locally by ASTRA Plant Doctor.\n"
        )

    return output_file


# ------------------------------------------------------------
# Interactive mode
# ------------------------------------------------------------

def interactive_mode(model, processor):

    print_header()

    while True:

        print("\nOptions:")
        print("1. Analyze plant image")
        print("2. Exit")

        choice = input("\nSelect: ").strip()

        if choice == "1":

            image_path = input(
                "\n📷 Enter image path: "
            ).strip()

            if not image_path:
                print("❌ No image path provided.")
                continue

            check_image(image_path)

            try:
                report = analyze_plant(
                    image_path,
                    model,
                    processor
                )

                print("\n" + "=" * 70)
                print("🌱 PLANT REPORT")
                print("=" * 70)
                print(report)

                output = save_report(
                    image_path,
                    report
                )

                print("\n💾 Report saved:")
                print(output)

            except Exception as error:

                print("\n❌ Analysis failed.")
                print(f"Error: {error}")

        elif choice == "2":

            print("\n👋 ASTRA Plant Doctor closed.")
            break

        else:

            print("❌ Invalid option.")


# ------------------------------------------------------------
# Command-line mode
# ------------------------------------------------------------

def command_line_mode(image_path):

    check_image(image_path)

    print_header()

    model, processor = load_model()

    report = analyze_plant(
        image_path,
        model,
        processor
    )

    print("\n" + "=" * 70)
    print("🌱 PLANT REPORT")
    print("=" * 70)

    print(report)

    output = save_report(
        image_path,
        report
    )

    print("\n💾 Report saved:")
    print(output)


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="ASTRA Plant Doctor - Offline AI Plant Analyzer"
    )

    parser.add_argument(
        "image",
        nargs="?",
        help="Path to plant image"
    )

    args = parser.parse_args()

    model, processor = load_model()

    if args.image:

        check_image(args.image)

        print_header()

        report = analyze_plant(
            args.image,
            model,
            processor
        )

        print("\n" + "=" * 70)
        print("🌱 PLANT REPORT")
        print("=" * 70)

        print(report)

        output = save_report(
            args.image,
            report
        )

        print("\n💾 Report saved:")
        print(output)

    else:

        interactive_mode(
            model,
            processor
        )


if __name__ == "__main__":
    main()
    #pip install torch torchvision transformers accelerate pillowpip install qwen-vl-utils#
    #python main.py#