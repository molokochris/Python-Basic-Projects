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

def randomNum():
    return (random.randrange(100)/100) 

class Warrior:
    def __init__(self, name="", health=100, maxAttack=100, maxBlock=100):
        self.name = name
        self.health = health
        self.maxAttack = maxAttack
        self.maxBlock = maxBlock
    
    def attack(self):
        return randomNum() * self.maxAttack + .5
    
    def block(self):
        return randomNum() * self.maxBlock + .5

class Battle:

# print(randomNum())