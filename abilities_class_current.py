import dice as d  # Import the dice module as 'd'

class Abilities:
    scores_and_mods = {
        range(1, 2):     -5,
        range(2, 4):     -4,
        range(4, 6):     -3,
        range(6, 8):     -2,
        range(8, 10):    -1,
        range(10, 12):   +0,
        range(12, 14):   +1,
        range(14, 16):   +2,
        range(16, 18):   +3,
        range(18, 20):   +4,
        range(20, 22):   +5,
        range(22, 24):   +6,
        range(24, 26):   +7,
        range(26, 28):   +8,
        range(28, 30):   +9,
        range(30, 31):   +10
    }  # Dictionary mapping score ranges to their corresponding modifiers

    @staticmethod
    def calc_ability_score(num_of_dice=4, die_obj=d.d6):
        # Static method to calculate ability score
        rolls = sorted(die_obj.roll(num_of_dice))  # Roll the dice and sort the rolls in ascending order
        return sum(rolls[1:])  # Return the sum of the highest three rolls

    @classmethod
    def calc_ability_modifier(cls, ability_score):
        # Class method to calculate ability modifier
        for score_range, modifier in cls.scores_and_mods.items():
            # Iterate through the score ranges and modifiers in the dictionary
            if ability_score in score_range:
                # If the ability score falls within the current range
                return modifier  # Return the corresponding modifier
        return 0  # If no range matches, return 0 as the default modifier

    def __init__(self):
        self.ability_scores = {}  # Initialize an empty dictionary for storing ability scores
        for ability_name in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            # Iterate through the list of ability names
            ability_score = self.calc_ability_score()  # Calculate the ability score
            ability_modifier = self.calc_ability_modifier(ability_score)  # Calculate the ability modifier
            self.ability_scores[ability_name] = {ability_score: ability_modifier}
            # Add the ability score and modifier to the dictionary
            self.ability_scores[ability_name] = {
                'score': ability_score,
                'modifier': ability_modifier
            }
            # Update the dictionary entry to include the 'score' and 'modifier' keys
