import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

text = open(
    "meeting.txt",
    encoding="utf-8"
).read()

prompt = f"""
Summarize this meeting.

Return:

- Summary
- Decisions
- Action items
- Important points
- Questions

Meeting:

{text}
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