import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

topic = input("Research topic: ")

prompt = f"""
Act as a research assistant.

Topic:
{topic}

Provide:

1. Overview
2. Important concepts
3. Key questions
4. Possible applications
5. Learning roadmap
6. Further research directions
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

print(response.choices[0].message.content)