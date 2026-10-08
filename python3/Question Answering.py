import re

context = """
Python is a programming language created by Guido van Rossum.
Python was first released in 1991.
Python is popular in artificial intelligence and data science.
"""

qa = {
    "who created python": "Guido van Rossum",
    "when was python released": "1991",
    "where is python popular": "Artificial intelligence and data science"
}

question = input("Question: ").lower().strip()

answer = qa.get(question)

if answer:
    print("Answer:", answer)
else:
    words = set(re.findall(r"\w+", question))

    best_answer = None
    best_score = 0

    for key, value in qa.items():
        key_words = set(re.findall(r"\w+", key))
        score = len(words & key_words)

        if score > best_score:
            best_score = score
            best_answer = value

    if best_answer:
        print("Answer:", best_answer)
    else:
        print("I don't know.")