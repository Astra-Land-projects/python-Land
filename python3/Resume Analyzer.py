import re

resume = """
Arya Gh is a Python developer and AI student.
Skills: Python, FastAPI, TensorFlow, Git, SQL, Flutter.
Experience: Developed Telegram bots and machine learning projects.
"""

skills = [
    "python",
    "fastapi",
    "tensorflow",
    "pytorch",
    "git",
    "sql",
    "flutter",
    "docker",
    "linux",
    "machine learning",
    "deep learning"
]

resume_lower = resume.lower()

found_skills = []

for skill in skills:
    if skill in resume_lower:
        found_skills.append(skill)

emails = re.findall(
    r'[\w\.-]+@[\w\.-]+\.\w+',
    resume
)

phone_numbers = re.findall(
    r'\+?\d[\d\s\-]{7,}\d',
    resume
)

print("\n===== RESUME ANALYSIS =====")

print("\nSkills:")
for skill in found_skills:
    print("-", skill)

print("\nEmail:")
print(emails if emails else "Not found")

print("\nPhone:")
print(phone_numbers if phone_numbers else "Not found")

print("\nSkill Score:")
print(f"{len(found_skills)} / {len(skills)}")