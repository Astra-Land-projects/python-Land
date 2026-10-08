import re

rules = {
    r"\bi is\b": "I am",
    r"\bhe are\b": "he is",
    r"\bshe are\b": "she is",
    r"\bthey is\b": "they are",
    r"\byou is\b": "you are",
    r"\bi has\b": "I have",
    r"\bhe have\b": "he has",
    r"\bshe have\b": "she has"
}

text = input("Enter sentence: ")

corrected = text

for pattern, replacement in rules.items():
    corrected = re.sub(
        pattern,
        replacement,
        corrected,
        flags=re.IGNORECASE
    )

if corrected != text:
    print("Possible correction:")
    print(corrected)
else:
    print("No known grammar errors found.")