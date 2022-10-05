import random

class Abilities:
    def __init__(self):
        scores_and_mods = {
            range(1, 1):     -5,
            range(2, 3+1):   -4,
            range(4, 5+1):   -3,
            range(6, 7+1):   -2,
            range(8, 9+1):   -1,
            range(10, 11+1): +0,
            range(12, 13+1): +1,
            range(14, 15+1): +2,
            range(16, 17+1): +3,
            range(18, 19+1): +4,
            range(20, 21+1): +5,
            range(22, 23+1): +6,
            range(24, 25+1): +7,
            range(26, 27+1): +8,
            range(28, 29+1): +9,
            range(30, 30):  +10
        }

        def calc_ability_score(num_of_dice=4, number_of_sides=6):
            four_dice = []
            total = 0
            for die in range(1, num_of_dice+1):
                die_roll = random.randint(1, number_of_sides)
                four_dice.append(die_roll)
            #print(four_dice)
            smallest_die = number_of_sides
            for die in four_dice:
                if die < smallest_die:
                    smallest_die = die
            four_dice.remove(smallest_die)
            three_dice = four_dice
            #print(three_dice)
            for die in three_dice:
                total += die
            return total

        def calc_ability_modifier(ability_score):
            for score_range in scores_and_mods:
                if ability_score in score_range:
                    modifier = scores_and_mods[ability_score]
                    return modifier
        
        
        self.str_score = calc_ability_score()
        self.dex_score = calc_ability_score()
        self.con_score = calc_ability_score()
        self.int_score = calc_ability_score()
        self.wis_score = calc_ability_score()
        self.cha_score = calc_ability_score()

        

        self.str_mod = calc_ability_modifier(self.str_score)
        self.dex_mod = calc_ability_modifier(self.dex_score)
        self.con_mod = calc_ability_modifier(self.con_score)
        self.int_mod = calc_ability_modifier(self.int_score)
        self.wis_mod = calc_ability_modifier(self.wis_score)
        self.cha_mod = calc_ability_modifier(self.cha_score)

        self.ability_scores = {
            "Strength":     {self.str_score: self.str_mod},
            "Dexterity":    {self.dex_score: self.dex_mod},
            "Constitution": {self.con_score: self.con_mod},
            "Intelligence": {self.int_score: self.int_mod},
            "Wisdom":       {self.wis_score: self.wis_mod},
            "Charisma":     {self.cha_score: self.cha_mod}
        }      
            

person_1_abilities = Abilities()
person_2_abilities = Abilities()

print(person_1_abilities)
