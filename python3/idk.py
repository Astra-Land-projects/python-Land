


# ✍️ پروژه ۹۳ — AI Writing Assistant

### `project_93_ai_writing_assistant.py`

python
import os

from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set."
    )


client = OpenAI(api_key=api_key)


def improve_text(text, task):
    prompt = f"""
You are an AI writing assistant.

Task:
{task}

Text:
{text}

Return an improved version.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional writing assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


print("===== AI WRITING ASSISTANT =====")

while True:
    print("\n1. Improve")
    print("2. Summarize")
    print("3. Make professional")
    print("4. Make simple")
    print("5. Exit")

    choice = input("\nChoose: ")

    if choice == "5":
        break

    text = input("\nEnter text:\n")

    tasks = {
        "1": "Improve the writing.",
        "2": "Summarize the text.",
        "3": "Make the text professional.",
        "4": "Make the text simple and easy to understand."
    }

    task = tasks.get(
        choice,
        "Improve the text."
    )

    result = improve_text(text, task)

    print("\nResult:")
    print(result)