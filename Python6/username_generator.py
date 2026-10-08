import random

class UsernameGenerator:

    def generate(self, name):
        return f"{name}{random.randint(1000,9999)}"