import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

goal = input("Goal: ")

prompt = f"""
Create a practical project plan.

Goal:
{goal}

Return:

- Milestones
- Tasks
- Dependencies
- Testing
- Final result
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