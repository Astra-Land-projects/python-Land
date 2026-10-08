import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
while True:
    q = input("Student (exit): ")
    if q == "exit": break
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Teach step by step with examples."},
                  {"role": "user", "content": q}]
    )
    print(r.choices[0].message.content)