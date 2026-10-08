positive = {
    "good",
    "great",
    "excellent",
    "happy",
    "amazing"
}

negative = {
    "bad",
    "terrible",
    "sad",
    "hate",
    "awful"
}

text = input("Text: ").lower()
words = set(text.split())

score = len(words & positive) - len(words & negative)

if score > 0:
    print("Positive")
elif score < 0:
    print("Negative")
else:
    print("Neutral")