import dice as d

hit_dice_dict = {
    "Barbarian": d.d12,
    "Bard": d.d8,
    "Cleric": d.d8,
    "Druid": d.d8,
    "Fighter": d.d10,
    "Monk": d.d8,
    "Paladin": d.d10,
    "Ranger": d.d10,
    "Rogue": d.d8,
    "Sorcerer": d.d6,
    "Warlock": d.d8,
    "Wizard": d.d6
}

class Class:
    def __init__(self, class_name): 
        self.hit_die = hit_dice_dict[class_name]
        self.class_name = class_name

    def __repr__(self):
        return f"This is the {self.class_name} class. Its hit die is a d{self.hit_die.sides}."

barbarian = Class("Barbarian")
bard = Class("Bard")
cleric = Class("Cleric")
druid = Class("Druid")
fighter = Class("Fighter")
monk = Class("Monk")
paladin = Class("Paladin")
ranger = Class("Ranger")
rogue = Class("Rogue")
sorcerer = Class("Sorcerer")
warlock = Class("Warlock")
wizard = Class("Wizard")

class_list = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]

class_obj_dict = {
    "Barbarian": barbarian,
    "Bard": bard,
    "Cleric": cleric,
    "Druid": druid,
    "Fighter": fighter,
    "Monk": monk,
    "Paladin": paladin,
    "Ranger": ranger,
    "Rogue": rogue,
    "Sorcerer": sorcerer,
    "Warlock": warlock,
    "Wizard": wizard
}

# Test the Class and Class Object Dict functionality

#print(barbarian)
# Output: This is the Barbarian class. Its hit die is a d12.

#print(class_obj_dict["Bard"])
# Output: This is the Bard class. Its hit die is a d8.

#print(class_obj_dict["Ranger"])
# Output: This is the Ranger class. Its hit die is a d10.

#print(class_obj_dict["Sorcerer"])
# Output: This is the Sorcerer class. Its hit die is a d6.


