# project_199_prompt_builder.py

task = input("Task: ").strip()
tone = input("Tone: ").strip()
length = input("Length: ").strip()

prompt = f"""
Write a {tone} text about {task}.
Keep it {length}.
"""

print(prompt.strip())