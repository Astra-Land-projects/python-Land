# project_194_word_counter.py

from collections import Counter

text = input("Text: ").lower()
words = text.split()

counter = Counter(words)

for word, count in counter.most_common():
    print(word, ":", count)