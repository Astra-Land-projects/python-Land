import re

skills = {
    "python",
    "django",
    "fastapi",
    "sql",
    "tensorflow",
    "pytorch",
    "docker",
    "git",
    "flutter",
    "machine learning"
}

resume = open(
    "resume.txt",
    encoding="utf-8"
).read().lower()

found = []

for skill in skills:

    if re.search(
        r"\b" + re.escape(skill) + r"\b",
        resume
    ):
        found.append(skill)

score = len(found) / len(skills) * 100

print("Detected skills:")

for skill in found:
    print("-", skill)

print(f"\nSkill Match: {score:.1f}%")