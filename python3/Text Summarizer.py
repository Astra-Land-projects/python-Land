import re
from collections import Counter

text = """
Python is a powerful programming language.
Python is widely used for artificial intelligence.
Machine learning is one of the most popular applications of Python.
Python can also be used for web development.
Many developers use Python because it is simple and readable.
Artificial intelligence is changing many industries.
"""

sentences = re.split(r'(?<=[.!?])\s+', text.strip())

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

stop_words = {
    "the", "is", "a", "of", "for", "and",
    "can", "be", "one", "many", "it"
}

word_frequency = Counter(
    word for word in words
    if word not in stop_words
)

scores = {}

for sentence in sentences:
    sentence_words = re.findall(
        r'\b[a-zA-Z]+\b',
        sentence.lower()
    )

    score = sum(
        word_frequency[word]
        for word in sentence_words
        if word in word_frequency
    )

    scores[sentence] = score

summary_sentences = sorted(
    scores,
    key=scores.get,
    reverse=True
)[:3]

print("\nSUMMARY:\n")

for sentence in summary_sentences:
    print(sentence)