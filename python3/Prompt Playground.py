import json
from datetime import datetime


history = []


def save_prompt(prompt, response):
    history.append({
        "time": datetime.now().isoformat(),
        "prompt": prompt,
        "response": response
    })


def show_history():
    if not history:
        print("\nNo history.")
        return

    print("\n===== HISTORY =====")

    for index, item in enumerate(history, start=1):
        print(f"\n[{index}]")
        print("Prompt:", item["prompt"])
        print("Response:", item["response"])


def save_history():
    with open(
        "prompt_history.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            history,
            file,
            ensure_ascii=False,
            indent=4
        )


print("===== PROMPT PLAYGROUND =====")
print("Commands: /history /save /exit")

while True:
    prompt = input("\nPrompt: ")

    if prompt == "/exit":
        break

    if prompt == "/history":
        show_history()
        continue

    if prompt == "/save":
        save_history()
        print("History saved.")
        continue

    response = (
        "Prompt received successfully.\n"
        "Connect this playground to an LLM API "
        "to generate an AI response."
    )

    print("\nResponse:")
    print(response)

    save_prompt(prompt, response)