import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

code = open(
    "main.py",
    encoding="utf-8"
).read()

prompt = f"""
Generate Python unit tests
using pytest for this code.

Include:

- Normal cases
- Edge cases
- Invalid input
- Error cases

Code:

{code}
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