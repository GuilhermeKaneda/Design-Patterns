from models.Characters.Character import Character

# Classe composite (contém os personagens do jogo)
class Player(Character):

    def __init__(self):
        self.party = []
    
    # Todos os personagens da party atacam
    def attack(self, target: Character):
        for character in self.party:
            print(character.attack(target))

    # Todos os personagens se curam
    def heal(self):
        for character in self.party:
            print(character.heal())

    # Todos usam o poder especial
    def special(self, target: Character=0):
        for character in self.party:
            answer = character.special(target)
            print(answer)

            if answer.startswith('Not enough mana!'):
                return 0
        
        return 1

    # -- Métodos de acesso da lista --
    # Adiciona um personagem à party
    def add(self, character: Character):
        self.party.append(character)

    # Remove um personagem da party
    def remove(self, character: Character):
        self.party.remove(character)