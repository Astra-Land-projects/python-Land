import os

from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set."
    )


client = OpenAI(api_key=api_key)


system_prompt = """
You are an AI tutor.

Teach students step by step.

Rules:
- Explain concepts clearly.
- Give examples.
- Ask questions.
- Don't immediately reveal answers to exercises.
- Adapt explanations to the student's level.
"""


messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]


print("===== AI TUTOR =====")
print("Type 'exit' to quit.")


while True:
    question = input("\nStudent: ")

    if question.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    answer = response.choices[0].message.content

    print("\nTutor:")
    print(answer)

    messages.append({
        "role": "assistant",
        "content": answer
    })