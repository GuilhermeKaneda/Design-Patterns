from models.Characters.Character import Character
from models.Characters.CharacterBridge import CharacterBridge


class UniversalCharacterBridge(CharacterBridge):

    def __init__(self, character:  Character):
        super().__init__(character)

    def attack(self, target):
        return self.character.attack(target)

    def heal(self):
        return self.character.heal()

    def special(self, target=0):
        return self.character.special(target)