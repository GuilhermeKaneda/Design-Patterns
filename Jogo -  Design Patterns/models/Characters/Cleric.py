from models.Characters.Character import Character
from models.Weapon import Weapon
import random

class Cleric(Character):
    
    def __init__(self, hp: int, damage: int, armor: int):
        super().__init__(hp, damage, armor)
        self.weapon = Weapon()

    def attack(self, target: Character) -> str:
        # Calcula o dano causado
        damagePoints = (self.damage - target.armor)

        self.weapon.attack(damagePoints, target)

        self.mana += 20

        return f'''
              Cleric burned the Dragon with Divine Sunlight, dealing {damagePoints} damage!\n
              Target life is {target.hp} now.
              '''
        
    def heal(self) -> str:
        # Se cura num intervalo inteiro de 5 a 10 (clérigo se cura mais)
        self.hp += random.randint(5,15)
        if self.hp > 100:
            self.hp = 100

        self.mana += 20

        return f'''Cleric asked for divine help and healed to {self.hp} hp!'''

    def special(self, target=0) -> str:
        if self.mana >= 100:
            self.mana = 0
            # Especial do clérigo: se cura muito
            self.hp += random.randint(20, 30)
            if self.hp > 100:
                self.hp = 100
        
            return f'''Cleric achieved her godess greatest interest, and healed an extreme amount of hp, reaching to {self.hp}!'''
        else:
            return f'Not enough mana! You got only {self.mana} points'