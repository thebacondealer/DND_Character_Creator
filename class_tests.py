import abilities_class_current as abil_clas
import Custom_Errors as CE
import dice as d
import DnD_Classes as cls


def create_character():
    """Function that creates an instance of the PC object based on user inputs."""

    # Get player's name from user
    pc_name_input = input("\nEnter your characters name and hit enter:\n\n")
    lowered_name = pc_name_input.lower()
    final_name = lowered_name.title()

    # Check if entered value is valid
    while True:

    # Ask user what kind of character they want to be
        pc_class_input = input("\nEnter your desired character class and hit enter:\n\n")
        formatted_input = pc_class_input.title()

        # If invalid entry was made, ask again until proper response given
        if formatted_input not in [c.class_name for c in classes]:
            print("Invalid Entry! Enter either Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard.\n")
            continue

        # Set chosen class equal to corresponding class object
        chosen_class = next((c for c in classes if c.class_name==formatted_input), None)

        # Create new PC with specified parameters
        self_PC = PC(final_name, chosen_class)

        # Return created PC
        return self_PC

def calc_ability_score(num_of_dice=4, die_obj=d.d6):
    four_dice = die_obj.roll(num_of_dice)
    total = 0
    #print(four_dice)
    smallest_die = die_obj.sides
    for die in four_dice:
        if die < smallest_die:
            smallest_die = die
    four_dice.remove(smallest_die)
    three_dice = four_dice
    #print(three_dice)
    for die in three_dice:
        total += die
    #print(total)
    return total                

str_score = calc_ability_score()
dex_score = calc_ability_score()
con_score = calc_ability_score()
int_score = calc_ability_score()
wis_score = calc_ability_score()
cha_score = calc_ability_score()

'''print(str_score)
print(dex_score)
print(con_score)
print(int_score)
print(wis_score)
print(cha_score)'''

def create_character():
    pc_name_input = input("\nEnter your character's name and hit enter:\n\n")
    final_name = pc_name_input.strip().title()

    while True:
        try:
            pc_class_input = input("\nEnter your desired character class and hit enter:\n\n")
            formatted_input = pc_class_input.strip().title()
            ability_scores = abil_clas.Abilities().ability_scores
            if formatted_input in ability_scores:
                final_class = formatted_input
                break
            else:
                raise CE.InvalidInput()
        except CE.InvalidInput:
            print("Invalid Input, Please Try Again")

    pc_level_input = input("\nIf you are creating a character above Level 1, enter your desired level in numeric form. Otherwise, just hit enter to continue.\n\n")
    final_level = int(pc_level_input) if pc_level_input.isdigit() else 1

    self_pc = PC(final_name, final_class, final_level)
    return self_pc

def create_character():
    pc_name_input = input("\nEnter your characters name and hit enter:\n\n")
    lowered_name = pc_name_input.lower()
    final_name = lowered_name.title()
    while True:
        try:
            pc_class_input = input("\nEnter your desired character class and hit enter:\n\n")
            formated_input = pc_class_input.title()
            input_check = dict_key_exists(abil_clas.Abilities().ability_scores, formated_input)
            if input_check == False:
            #if not formated_input in cls.class_obj_dict.keys():
                #raise CE.InvalidInput()
                pass
            else:
                for clas in cls.class_obj_dict.keys():
                    if formated_input == clas:
                        final_class = str(formated_input)
                        return final_class
        except CE.InvalidInput:
            print("Invalid Input, Please Try Again")
        else:
            break
    pc_level_input = input("\nIf you are creating a character above Level 1, enter your desired level in numeric form, otherwise just hit enter to continue\n\n")
    if pc_level_input == '':
        self_PC = PC(final_name, final_class)
    else:
        final_level = int(pc_level_input)
        self_PC = PC(final_name, final_class, final_level)
    return self_PC

class PC:
    def __init__(self, name, class_name, level=1):
        self.abil_cls_obj = abil_clas.Abilities()
        self.name = name.strip().title()
        self.level = level
        self.clas = cls.Class(class_name)
        hit_die = self.clas.hit_die.sides
        con_mod = self.abil_cls_obj.con_mod
        dex_mod = self.abil_cls_obj.dex_mod
        self.max_health = level * (hit_die + con_mod)
        self.health = self.max_health
        self.armor_class = 10 + dex_mod
        self.is_conscious = True

    def __repr__(self):
        return f"This is {self.name}, a level {self.level} {self.clas.class_name}. They have {self.health} hit points remaining."

class PC:
    def __init__(self, name, class_name, level=1):
        self.abil_cls_obj = abil_clas.Abilities()
        self.name = name
        self.level = level
        self.clas = cls.class_obj_dict[class_name]#str(class_name).title()
        self.max_health = level * (self.clas.hit_die.sides + self.abil_cls_obj.con_mod)
        self.health = self.max_health
        self.armor_class = 10 + self.abil_cls_obj.dex_mod
        self.is_conscious = True

    def __repr__(self):
        return f"This is {self.name}, a level {self.level} {self.clas.class_name}. They have {self.health} hit points remaining." #using one[1] 's' for sake of syntax




def get_character_name():
    pc_name_input = input("\nEnter your character's name and hit enter:\n\n")
    return pc_name_input.strip().title()

def validate_class_input(pc_class_input):
    return str(pc_class_input).title() in cls.class_obj_dict

def get_character_class():
    while True:
        pc_class_input = input("\nEnter your desired character class and hit enter:\n\n")
        if validate_class_input(pc_class_input):
            return pc_class_input.title()
        elif not validate_class_input(pc_class_input):
            raise CE.InvalidInput
        break

def get_character_level():
    pc_level_input = input("\nIf you are creating a character above Level 1, enter your desired level in numeric form, otherwise just hit enter to continue\n\n")
    return int(pc_level_input) if pc_level_input else 1

def create_character():
    character_name = get_character_name()
    character_class = get_character_class()
    character_level = get_character_level()
    return PC(character_name, character_class, character_level)

self_PC = create_character()