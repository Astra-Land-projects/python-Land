from cryptography.fernet import Fernet


class Decryptor:

    def decrypt(self, filename):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()

        cipher = Fernet(key)

        with open(filename, "rb") as file:
            encrypted = file.read()

        data = cipher.decrypt(encrypted)

        output = filename.replace(".enc", "")

        with open(output, "wb") as file:
            file.write(data)

        print("Decrypted.")