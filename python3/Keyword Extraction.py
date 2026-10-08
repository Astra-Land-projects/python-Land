import re
from collections import Counter


STOP_WORDS = {
    "the", "is", "a", "an", "and", "or",
    "to", "of", "in", "on", "for", "with",
    "this", "that", "are", "was", "be",
    "as", "by", "from", "it"
}


def extract_keywords(text, count=10):
    words = re.findall(
        r"\b[a-zA-Z]{3,}\b",
        text.lower()
    )

    words = [
        word for word in words
        if word not in STOP_WORDS
    ]

    frequency = Counter(words)

    return frequency.most_common(count)


text = """
Artificial intelligence and machine learning are transforming
software development. Python is widely used for artificial
intelligence, data analysis, deep learning and automation.
Machine learning models can process large amounts of data.
"""

keywords = extract_keywords(text)

print("Keywords:\n")

for word, count in keywords:
    print(f"{word}: {count}")