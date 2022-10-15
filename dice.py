import random

class Die:
    def __init__(self, num_of_sides):
        self.sides = num_of_sides

    def roll(self, num_of_dice=1):
        list_of_results= []
        for die in range(1, num_of_dice+1):
            roll_result = random.randint(1, self.sides)
            list_of_results.append(roll_result)
        return list_of_results
    
    def __repr__(self) -> str:
        return f"This is a d{self.sides}"

d4 = Die(4)
d6 = Die(6)
d8 = Die(8)
d10 = Die(10)
d12 = Die(12)
d20 = Die(20)
d100 = Die(100)

#print(d6.roll(4))

