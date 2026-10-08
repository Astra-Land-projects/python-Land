import random

def generate_name(syllables):
    """Generates a random name with a specified number of syllables."""

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    name = ""
    for i in range(syllables):
        name += random.choice(consonants) + random.choice(vowels)

    return name.capitalize()

if __name__ == "__main__":
    num_syllables = 3
    name = generate_name(num_syllables)
    print(name)