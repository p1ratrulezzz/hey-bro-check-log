from sys import stdout

class Printer:
    def __init__(self):
        self.target_resource = stdout

    def print(self, text):
        self.target_resource.write(text)