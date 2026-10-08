import os


class TextEditor:

    def create_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("")
        print("File Created.")

    def read_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                print(file.read())
        else:
            print("File Not Found.")

    def append_text(self, filename, text):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")
        print("Text Added.")

    def overwrite_file(self, filename, text):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        print("File Updated.")

    def delete_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
            print("File Deleted.")
        else:
            print("File Not Found.")