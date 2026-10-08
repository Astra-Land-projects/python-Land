import hashlib


class HashGenerator:

    def generate(self, text):
        print("MD5 :", hashlib.md5(text.encode()).hexdigest())
        print("SHA1:", hashlib.sha1(text.encode()).hexdigest())
        print("SHA256:", hashlib.sha256(text.encode()).hexdigest())