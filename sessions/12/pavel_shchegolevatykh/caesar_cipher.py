import sys
from contextlib import contextmanager


class CeasarEncryptedStream:
    def __init__(self, target):
        self.target = target

    @staticmethod
    def encrypt(text, shift):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        return result

    def write(self, text):
        text = self.encrypt(text, 4)
        self.target.write(text)

    def flush(self):
        pass


@contextmanager
def ceasar_manager():
    original_stdout = sys.stdout
    sys.stdout = CeasarEncryptedStream(sys.stdout)
    yield
    sys.stdout = original_stdout


class CeasarManager:
    def __init__(self):
        self.original_stdout = sys.stdout

    def __enter__(self):
        sys.stdout = CeasarEncryptedStream(sys.stdout)

    def __exit__(self, exc_type, exc_value, tb):
        sys.stdout = self.original_stdout


print("\nGenerator version:")
with ceasar_manager():
    print("just a text")

print("\njust a text")

print("\nClass version:")
with CeasarManager():
    print("just a text")

print("\njust a text")
