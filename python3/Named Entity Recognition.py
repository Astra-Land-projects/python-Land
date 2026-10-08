import spacy


MODEL = "en_core_web_sm"

try:
    nlp = spacy.load(MODEL)
except OSError:
    print("Model not installed.")
    print("Run:")
    print("python -m spacy download en_core_web_sm")
    raise


text = """
Elon Musk founded SpaceX and Tesla.
Tesla is based in the United States.
Elon Musk was born in South Africa.
"""


doc = nlp(text)

print("Named Entities:\n")

for entity in doc.ents:
    print(
        f"Text: {entity.text:<20} "
        f"Type: {entity.label_}"
    )