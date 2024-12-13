from models.Characters.Character import Character

class CharacterBridge():

    def __init__(self, character:  Character):
        self.character = character

    def attack(self, target):
        pass

    def heal(self):
        pass

    def special(self, target=0):
        pass