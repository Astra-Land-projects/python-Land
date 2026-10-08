from collections import Counter
import re

text = input("Text: ").lower()

words = re.findall(
    r"\b[a-zA-Z]{3,}\b",
    text
)

counter = Counter(words)

for word, count in counter.most_common(10):
    print(word, ":", count)