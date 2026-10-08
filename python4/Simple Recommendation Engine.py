# project_197_recommendation.py

items = {
    "python": {"ai", "backend", "automation"},
    "flutter": {"mobile", "ui", "apps"},
    "fastapi": {"backend", "api", "python"},
    "tensorflow": {"ai", "ml", "deep learning"},
}

user_tags = set(input("Your interests (comma separated): ").lower().split(","))

scores = []
for name, tags in items.items():
    score = len(user_tags & tags)
    scores.append((score, name))

scores.sort(reverse=True)

for score, name in scores:
    print(name, "->", score)