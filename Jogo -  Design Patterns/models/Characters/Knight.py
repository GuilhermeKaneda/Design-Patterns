from models.Characters.Character import Character
from models.Weapon import Weapon
import random

class Knight(Character):
    
    def __init__(self, hp: int, damage: int, armor: int):
        super().__init__(hp, damage, armor)
        self.weapon = Weapon()
        self.specialRounds = 0
        self.specialAdditional = 20

    def attack(self, target: Character) -> str:
        # Calcula o dano causado
        damagePoints = (self.damage - target.armor)

        # Verifica se o cavaleiro está com o especial ativo. Se sim, aumenta o dano e diminui a duração do especial em um round
        if self.specialRounds > 0:
            damagePoints += self.specialAdditional
            self.specialRounds -= 1
            self.mana -= 20

        self.weapon.attack(damagePoints, target)

        self.mana += 20

        return f'''
              Knight slayed the Dragon with his greatsword, dealing {damagePoints} damage!\n
              Target life is {target.hp} now.
              '''
        
    def heal(self) -> str:
        # Se cura num intervalo inteiro de 3 a 10
        self.hp += random.randint(3,10)
        if self.hp > 100:
            self.hp = 100

        self.mana += 20

        return f'''Knight looked in his adventure bag and found a potion! Drinking it made him heal to {self.hp} hp!'''

    def special(self, target=0) -> str:
        if self.mana >= 100:
            self.mana = 0
            # Especial do cavaleiro: aumenta seu dano por 3 rounds
            self.specialRounds = 3
        
            return f'''Knight raised his sword and got blessed by the very gods! Now his attacks deals {self.specialAdditional} additional damage in the next three rounds!'''
        else:
            return f'Not enough mana! You got only {self.mana} points'