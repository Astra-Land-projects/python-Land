import os


class FileManager:

    def list_files(self):
        files = os.listdir()
        if not files:
            print("No files found.")
            return

        for file in files:
            print(file)

    def create_file(self, name):
        with open(name, "w") as file:
            file.write("")
        print("File created.")

    def read_file(self, name):
        if os.path.exists(name):
            with open(name, "r") as file:
                print(file.read())
        else:
            print("File not found.")

    def delete_file(self, name):
        if os.path.exists(name):
            os.remove(name)
            print("File deleted.")
        else:
            print("File not found.")