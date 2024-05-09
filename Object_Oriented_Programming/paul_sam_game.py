'''
The Game Example:
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Pauul has died and Sam is Victorious
Game Over
'''
import random
import math

class Warrior:
    def __init__(self, name="Warrior", health=0, maxAttack=0, maxBlock=0):
        self.name = name
        self.health = health
        self.maxAttack = maxAttack
        self.maxBlock = maxBlock
    
    def attack(self):
        totalAttack = self.maxAttack * (random.random() + .5)
        return totalAttack
    
    def block(self):
        totalBlock = self.maxBlock * (random.random() + .5)

        return totalBlock

class Battle:

    def startFight(self, warrior1, warrior2):
        
        while True:
            if self.getAttactRes(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            
            if self.getAttactRes(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttactRes(warriorA, warriorB):

        warriorAAttckAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        warriorBDamage = math.ceil(warriorAAttckAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - warriorBDamage

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, warriorBDamage))

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))

            return "Game Over"
        else:
            return "Fight still on.."    

def main():

    Paul = Warrior("Paul", 50, 20, 10)
    Sam = Warrior("Sam", 50, 20, 10)

    battle = Battle()
    battle.startFight(Sam, Paul)
    # print()


main()