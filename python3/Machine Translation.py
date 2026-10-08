translations = {
    "hello": "سلام",
    "goodbye": "خداحافظ",
    "how are you": "حالت چطوره",
    "thank you": "ممنون",
    "good morning": "صبح بخیر",
    "good night": "شب بخیر",
    "computer": "کامپیوتر",
    "programming": "برنامه نویسی",
    "artificial intelligence": "هوش مصنوعی",
    "machine learning": "یادگیری ماشین"
}

text = input("English: ").lower().strip()

if text in translations:
    print("Persian:", translations[text])
else:
    words = text.split()

    result = []

    for word in words:
        result.append(translations.get(word, word))

    print("Persian:", " ".join(result))