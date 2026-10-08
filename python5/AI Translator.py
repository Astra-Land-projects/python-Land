import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
text = input("Text: ")
source = input("Source language: ")
target = input("Target language: ")

prompt = f"Translate from {source} to {target}. Return only translation.\n\n{text}"
r = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
print(r.choices[0].message.content)