spam_words = {
    "free",
    "winner",
    "prize",
    "money",
    "offer",
    "click"
}

text = input("Message: ").lower()

words = set(text.split())

score = len(words & spam_words)

if score >= 2:
    print("⚠️ Spam detected")
else:
    print("Message looks normal")