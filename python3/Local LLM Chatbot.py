from openai import OpenAI


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful local AI assistant."
        )
    }
]


MODEL = "llama3.2"


print("===== LOCAL LLM CHATBOT =====")
print("Type 'exit' to quit.")


while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user
    })

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    answer = (
        response
        .choices[0]
        .message
        .content
    )

    print("\nAI:", answer)

    messages.append({
        "role": "assistant",
        "content": answer
    })