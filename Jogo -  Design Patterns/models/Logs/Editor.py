from models.Logs.Memento import Memento

class Editor():

    def __init__(self):
        self.text = str()

    def save(self):
        return Memento(self.text)

    def showText(self):
        print(self.text)