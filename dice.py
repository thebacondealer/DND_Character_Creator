import random


class Die:
    def __init__(self, num_of_sides):
        self.sides = num_of_sides

    def roll(self, num_of_dice=1):
        """
        Roll the die a specified number of times and return the results as a list.

        Args:
            num_of_dice (int): The number of times to roll the die. Defaults to 1.

        Returns:
            list: List of integers representing the results of the rolls.
        """
        list_of_results = []
        for _ in range(num_of_dice):
            roll_result = random.randint(1, self.sides)
            list_of_results.append(roll_result)
        return list_of_results
    
    def __repr__(self):
        """
        Returns a string representation of the die.

        Returns:
            str: String representation of the die.
        """
        return f"This is a d{self.sides}"

# Create instances of different dice
d4 = Die(4)
d6 = Die(6)
d8 = Die(8)
d10 = Die(10)
d12 = Die(12)
d20 = Die(20)
d100 = Die(100)

# Test 1: Roll a single die
#print("Test #1")
#print(d6.roll())  # Roll a single d6
# Expected output: A single random number between 1 and 6
#print("\n")

# Test 2: Roll multiple dice
#print("Test #2")
#print(d10.roll(4))  # Roll 4 d10 dice
# Expected output: A list of 4 random numbers between 1 and 10
#print("\n")

# Test 3: Print string representation of a die
#print("Test #3")
#print(d20)
# Expected output: "This is a d20"
#print("\n")

# Test 4: Roll multiple dice with different number of sides
#print("Test #4")
#print(d6.roll(3))  # Roll 3 d6 dice
# Expected output: A list of 3 random numbers between 1 and 6

#print(d10.roll())  # Roll a single d10
# Expected output: A single random number between 1 and 10
#print("\n")

# Test 5: Roll a combination of different dice
#print("Test #5")
#results = d6.roll(2) + d10.roll(3) + d20.roll()
#print(results)
# Expected output: A list of random numbers from rolling 2 d6 dice, 3 d10 dice, and 1 d20
#print("\n")

# Test 6: Print string representation of different dice
#print("Test #6")
#print(d4)
# Expected output: "This is a d4"

#print(d12)
# Expected output: "This is a d12"

#print(d100)
# Expected output: "This is a d100"

def test_die_rolling():
    # Create a 6-sided die
    die = Die(6)
    # Roll the die once and expect a single value in the result list
    assert len(die.roll()) == 1
    # Roll the die 10 times and expect 10 values in the result list
    assert len(die.roll(num_of_dice=10)) == 10
    # Roll the die 100 times and ensure all values are within the valid range
    rolls = die.roll(num_of_dice=100)
    assert all(1 <= roll <= 6 for roll in rolls)

def test_die_representation():
    # Create a 12-sided die
    die = Die(12)
    # Check the string representation of the die
    assert repr(die) == "This is a d12"

# Run the tests
#print(test_die_rolling())
#print(test_die_representation())

