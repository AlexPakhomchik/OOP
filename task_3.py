class MyString():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def __lt__(self, other):
        return MyString(len(self.value) < len(self.value))

    def __le__(self, other):
        return MyString(len(self.value) <= len(self.value))

    def __eq__(self, other):
        return MyString(len(self.value) == len(self.value))

    def __gt__(self, other):
        return MyString(len(self.value) > len(self.value))

    def __ge__(self, other):
        return MyString(len(self.value) >= len(self.value))
