import os

try:
    from openai import OpenAI
except ImportError:
    print("Install with:")
    print("pip install openai")
    raise


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY environment variable is missing."
    )


client = OpenAI(api_key=api_key)

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]


print("===== AI CHAT =====")
print("Type /exit to quit.")


while True:
    user = input("\nYou: ")

    if user.lower() == "/exit":
        break

    messages.append({
        "role": "user",
        "content": user
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    answer = response.choices[0].message.content

    print("\nAI:", answer)

    messages.append({
        "role": "assistant",
        "content": answer
    })