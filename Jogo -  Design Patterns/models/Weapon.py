from models.Characters.Character import Character

class Weapon():

    def attack(self, damage: int, target: Character):
        # Diminui a vida do personagem se o dano for > 0 e se o alvo tiver vida suficiente
        target.hp = target.hp - damage if damage else target.hp
        target.hp = 0 if target.hp < 0 else target.hp