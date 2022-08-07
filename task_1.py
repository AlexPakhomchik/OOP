class Nobody():
    def __init__(self, name:str):
        self.name = name
        if self.name != 'Nobody':
            self.name = "I'm Nobody, not" + ' ' + name
        else:
            self.name = 'Nobody'
    def qwe(self):
        print(self.name)

alex = Nobody('alex')
alex.qwe()
