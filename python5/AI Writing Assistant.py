import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
text = input("Text:\n")
task = input("Task (improve/summarize/professional): ")

prompt = f"{task} this text:\n\n{text}"
r = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
print(r.choices[0].message.content)