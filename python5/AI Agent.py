import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def agent(task):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are an AI planning agent.

Break tasks into:

1. Goal
2. Steps
3. Required tools
4. Expected result
"""
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    return response.choices[0].message.content


while True:

    task = input("Task (exit): ")

    if task == "exit":
        break

    print(agent(task))