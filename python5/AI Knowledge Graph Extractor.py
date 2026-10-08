import re

text = open(
    "document.txt",
    encoding="utf-8"
).read()

sentences = re.split(
    r"(?<=[.!?])\s+",
    text
)

for sentence in sentences:

    words = sentence.split()

    if len(words) >= 3:

        subject = words[0]
        relation = words[1]
        object_ = " ".join(words[2:])

        print(
            f"{subject} "
            f"--{relation}--> "
            f"{object_}"
        )