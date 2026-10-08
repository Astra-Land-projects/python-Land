import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

email = input("Email:\n")

prompt = f"""
Analyze this email and return:

1. Summary
2. Intent
3. Important information
4. Suggested reply

Email:

{email}
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