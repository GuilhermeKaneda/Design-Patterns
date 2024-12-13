from models.Characters.Character import Character
from models.Weapon import Weapon
import random

class Enemy(Character):
    
    def __init__(self, hp: int, damage: int, armor: int):
        super().__init__(hp, damage, armor)
        self.weapon = Weapon()
        self.specialPower = False
        self.mana = 0

    def attack(self, target: Character):

        for character in target.party:
                # Calcula o dano causado
                damagePoints = (self.damage - character.character.armor)
                
                if self.specialPower:
                    print('/////  NOW SUFFER FOR YOUR FOOLISH AMBITIONS!  /////\n')

                    damagePoints *= 3
                    self.specialPower = False
                    self.mana -= 40
                    
                self.weapon.attack(damagePoints, character.character)

        self.mana += 40

        return f'''
              Smaug burned your party to the ground, dealing {damagePoints} damage!\n
              Party life is {[character.character.hp for character in target.party]} now
              '''
        
    def heal(self):
        # Se cura num intervalo inteiro de 5 a 10
        self.hp += random.randint(5,10)
        if self.hp > 200:
            self.hp = 200

        self.mana += 40

        return f'The mighty dragon licked his wounds, healing to {self.hp} hp!'

    def special(self, target=0):
        if self.mana >= 100:
            self.mana = 0
            # Especial do dragão: triplica seu dano por uma rodada
            self.specialPower = True
        
        return f'The dragon communes with its inner greed, and will cause doubled damage in its next attack!'