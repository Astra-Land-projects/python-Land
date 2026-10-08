# project_185_quiz_cli.py

questions = [
    ("Python is a ...?", "programming language"),
    ("2 + 2 = ?", "4"),
    ("Flutter uses ...?", "dart"),
]

score = 0

for q, a in questions:
    ans = input(q + " ").strip().lower()
    if ans == a:
        score += 1

print(f"Score: {score}/{len(questions)}")