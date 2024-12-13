from models.Logs.Memento import Memento

class History():

    def __init__(self):
        self.history = list()

    def addMemento(self, memento: Memento):
        self.history.append(memento)

    def getLastMemento(self):
        if len(self.history) > 0:
            return self.history.pop()
        else:
            return -1

    def showMemento(self):
        for memento in self.history:
            print(memento)
