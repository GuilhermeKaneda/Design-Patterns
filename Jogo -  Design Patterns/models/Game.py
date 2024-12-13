from models.Characters import Knight, Enemy, Wizard, Cleric, UniversalCharacterBridge
from models.Logs.Editor import Editor
from models.Logs.History import History
from models.Player import Player
import random

class Game():
    def __init__(self):
        self.knight = Knight.Knight(100, 10, 10)
        self.knightHandler = UniversalCharacterBridge.UniversalCharacterBridge(self.knight)

        self.cleric = Cleric.Cleric(100, 15, 5)
        self.clericHandler = UniversalCharacterBridge.UniversalCharacterBridge(self.cleric)

        self.wizard = Wizard.Wizard(100, 20, 0)
        self.wizardHandler = UniversalCharacterBridge.UniversalCharacterBridge(self.wizard)


        self.party = Player()
        self.party.add(self.knightHandler)
        self.party.add(self.clericHandler)
        self.party.add(self.wizardHandler)

        self.enemy = Enemy.Enemy(100, 20, 10)
        self.enemyHandler = UniversalCharacterBridge.UniversalCharacterBridge(self.enemy)

        self.editor = Editor()
        self.history = History()

    def start_game(self):
        print(f''' You stand against Smaug, the ferocious dragon!\n
              
                _--^^^#####//      \\\#####^^^--_
             _-^##########// (    ) \\\##########^-_
            -############//  |\^^/|  \\\############-
          _/############//   (@::@)   \\\############\_
         /#############((     \\\//     ))#############\\
        -###############\\\    (oo)    //###############-
       -#################\\\  / "" \  //#################-
      -###################\\\/  ><  \//###################-
     _#/|##########/\######(       )######/\##########|\#_\n\n
              ''')

        while self.party.party[0].character.hp > 0 and self.party.party[1].character.hp > 0 and self.party.party[2].character.hp > 0 and self.enemy.hp > 0:
            print("=== MENU ===")
            print("1. Attack")
            print("2. Heal")
            print("3. Use Special")
            print("4. Repeat last used action\n")

            choice = '0'

            while True:
                if choice not in ['1', '2', '3', '4']:
                    choice = input('Choose your action: ')
                else:
                    if choice == '1':
                        self.party.attack(self.enemy)
                        break
                    
                    elif choice == '2':
                        print()
                        self.party.heal()
                        break
                    
                    elif choice == '3':
                        print()
                        if(self.party.special(self.enemy) == 0):
                            choice = '0'
                        else:
                            break

                    elif choice == '4':
                        lastChoice = '4'

                        while lastChoice == '4':
                            lastChoice = str(self.history.getLastMemento().action)
                        
                        if lastChoice == '4':
                            print("\nThere's no valid previous choice registered! Try again!\n")
                            choice = '0'
                        elif lastChoice != -1:
                            choice = lastChoice
                    else:
                        print("\nInvalid choice. Please try again!\n")
                
            self.editor.text = choice
            self.history.addMemento(self.editor.save())

            if self.enemy.hp <= 0:
                break

            # Turno do inimigo
            while True:
                if self.enemy.mana >= 100:
                    print(self.enemyHandler.special())
                    break

                enemyChoice = random.randint(1,4)

                if 1 <= enemyChoice <= 3:
                    print(self.enemyHandler.attack(self.party))
                else:
                    print(self.enemyHandler.heal())
                
                break

        if self.enemy.hp <= 0:
            print("Congrats! you defeated the monster!")
        else:
            print("Not this time, fellow adventurers!")