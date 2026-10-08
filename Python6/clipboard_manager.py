import pyperclip


class ClipboardManager:

    def copy(self, text):
        pyperclip.copy(text)
        print("Copied.")

    def paste(self):
        print("Clipboard:", pyperclip.paste())