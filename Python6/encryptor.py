from cryptography.fernet import Fernet


class Encryptor:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, filename):
        with open(filename, "rb") as file:
            data = file.read()

        encrypted = self.cipher.encrypt(data)

        with open(filename + ".enc", "wb") as file:
            file.write(encrypted)

        with open("secret.key", "wb") as file:
            file.write(self.key)

        print("Encrypted.")