class StringBuilder:
    def __init__(self):
        self.strings = []

    def append(self, string):
        self.strings.append(string)

    def __str__(self):
        return "".join(self.strings)