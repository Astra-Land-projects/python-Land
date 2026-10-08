import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask(role, task):

    prompt = f"""
You are the {role} agent.

Task:
{task}
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


topic = input("Research topic: ")

research = ask(
    "Researcher",
    topic
)

critic = ask(
    "Critical reviewer",
    research
)

writer = ask(
    "Technical writer",
    research + "\n\nReview:\n" + critic
)

print(writer)