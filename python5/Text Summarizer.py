import re
from collections import Counter

text = input("Text: ")
sentences = re.split(r'(?<=[.!?])\s+', text.strip())
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
stop = {"the","is","a","an","of","and","to","in","for","on","with"}
freq = Counter(w for w in words if w not in stop)

scores = {s: sum(freq[w] for w in re.findall(r'\b[a-zA-Z]+\b', s.lower()) if w in freq) for s in sentences}
for s in sorted(scores, key=scores.get, reverse=True)[:3]:
    print(s)