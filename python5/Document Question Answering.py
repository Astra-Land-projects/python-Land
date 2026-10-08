import re

document = open(
    "document.txt",
    encoding="utf-8"
).read()

sentences = re.split(
    r"(?<=[.!?])\s+",
    document
)

while True:

    question = input(
        "\nQuestion (exit): "
    )

    if question == "exit":
        break

    words = set(
        re.findall(
            r"\w+",
            question.lower()
        )
    )

    scored = []

    for sentence in sentences:

        sentence_words = set(
            re.findall(
                r"\w+",
                sentence.lower()
            )
        )

        score = len(
            words & sentence_words
        )

        scored.append(
            (score, sentence)
        )

    scored.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    print(
        "\nAnswer:",
        scored[0][1]
    )