import random
import string

class PasswordGenerator:

    def generate(self, length):
        chars = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        return "".join(random.choice(chars) for _ in range(length))