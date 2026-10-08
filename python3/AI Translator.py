import os

from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set."
    )


client = OpenAI(api_key=api_key)


def translate(text, source, target):

    prompt = f"""
Translate the following text.

Source language: {source}
Target language: {target}

Text:
{text}

Return only the translation.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


print("===== AI TRANSLATOR =====")

text = input("Text: ")
source = input("Source language: ")
target = input("Target language: ")

result = translate(
    text,
    source,
    target
)

print("\nTranslation:")
print(result)