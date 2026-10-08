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
Review the following Python code.

Check:

- Bugs
- Security issues
- Performance
- Readability
- Architecture
- Improvements

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