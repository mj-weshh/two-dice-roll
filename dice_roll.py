import random

class Dice:
    def roll(self):
        one = random.randint(1, 6)
        two = random.randint(1, 6)
        return one, two
    

dice = Dice()
print(dice.roll())