import re
import sys

try:
    import PyPDF2
except ImportError:
    print("Install:")
    print("pip install PyPDF2")
    raise


def read_pdf(path):
    text = ""

    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text


def find_relevant_text(text, question):
    question_words = set(
        re.findall(r"\w+", question.lower())
    )

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text
    )

    scored = []

    for sentence in sentences:
        words = set(
            re.findall(
                r"\w+",
                sentence.lower()
            )
        )

        score = len(question_words & words)

        if score:
            scored.append(
                (score, sentence.strip())
            )

    scored.sort(reverse=True)

    return [
        sentence
        for _, sentence in scored[:5]
    ]


if len(sys.argv) < 2:
    print("Usage:")
    print("python project_88_pdf_chatbot.py book.pdf")
    sys.exit()


pdf_path = sys.argv[1]

text = read_pdf(pdf_path)

print("PDF loaded successfully.")
print("Type 'exit' to quit.")

while True:
    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    results = find_relevant_text(
        text,
        question
    )

    if results:
        print("\nRelevant information:\n")

        for result in results:
            print("-", result)

    else:
        print("No relevant information found.")