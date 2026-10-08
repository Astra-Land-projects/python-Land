# project_192_text_checkers.py

a = input("First text: ").lower().replace(" ", "")
b = input("Second text (for anagram): ").lower().replace(" ", "")

pal = input("Palindrome text: ").lower().replace(" ", "")

print("Anagram:", sorted(a) == sorted(b))
print("Palindrome:", pal == pal[::-1])