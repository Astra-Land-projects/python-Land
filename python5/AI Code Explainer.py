import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
code = input("Paste code:\n")

r = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": f"Explain this code simply:\n\n{code}"}]
)
print(r.choices[0].message.content)