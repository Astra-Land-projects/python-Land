text = input("Text: ")

english = sum(
    c in "abcdefghijklmnopqrstuvwxyz"
    for c in text.lower()
)

persian = sum(
    "\u0600" <= c <= "\u06ff"
    for c in text
)

if english > persian:
    print("English")
elif persian > english:
    print("Persian")
else:
    print("Unknown / Mixed")