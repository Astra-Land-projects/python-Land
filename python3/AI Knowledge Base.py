import json
import os

from openai import OpenAI


FILE = "knowledge.json"


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def load_knowledge():

    if not os.path.exists(FILE):
        return []

    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def save_knowledge(data):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


knowledge = load_knowledge()


def ask_ai(question):

    context = "\n".join(
        item["content"]
        for item in knowledge
    )

    prompt = f"""
Answer the question using the knowledge below.

Knowledge:
{context}

Question:
{question}
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

    return response.choices[0].message.content


print("===== AI KNOWLEDGE BASE =====")

while True:

    print("\n1. Add knowledge")
    print("2. Ask question")
    print("3. Show knowledge")
    print("4. Exit")

    choice = input("\nChoose: ")

    if choice == "1":

        content = input(
            "\nKnowledge: "
        )

        knowledge.append({
            "content": content
        })

        save_knowledge(knowledge)

        print("Saved.")

    elif choice == "2":

        question = input(
            "\nQuestion: "
        )

        print(
            "\nAI:",
            ask_ai(question)
        )

    elif choice == "3":

        for index, item in enumerate(
            knowledge,
            start=1
        ):
            print(
                f"{index}. "
                f"{item['content']}"
            )

    elif choice == "4":
        break