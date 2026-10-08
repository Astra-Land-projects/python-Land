from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
messages = [{"role": "system", "content": "You are a helpful local AI."}]

while True:
    q = input("You (exit): ")
    if q == "exit": break
    messages.append({"role": "user", "content": q})
    r = client.chat.completions.create(model="llama3.2", messages=messages)
    ans = r.choices[0].message.content
    print(ans)
    messages.append({"role": "assistant", "content": ans})