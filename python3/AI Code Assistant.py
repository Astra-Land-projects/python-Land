import os

from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set."
    )


client = OpenAI(api_key=api_key)


SYSTEM_PROMPT = """
You are an AI programming assistant.

You can:
- explain code
- find bugs
- improve code
- refactor code
- generate code

Always provide clear and useful answers.
"""


def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


print("===== AI CODE ASSISTANT =====")
print("Commands: explain, debug, improve, generate")
print("Type 'exit' to quit.")


while True:
    command = input("\nCommand: ")

    if command.lower() == "exit":
        break

    code = input("\nPaste your code:\n")

    prompt = f"""
Task: {command}

Code:
```text
{code}
answer = ask_ai(prompt)

print("\nAI:")
print(answer)