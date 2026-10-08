# project_186_md_to_html.py

import re

text = input("Markdown text: ")

text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
text = re.sub(r"^\# (.*)$", r"<h1>\1</h1>", text, flags=re.M)
text = re.sub(r"^\#\# (.*)$", r"<h2>\1</h2>", text, flags=re.M)

print(text)