import ability_modifiers as abil_mods
import dice as d
import classes as cls

class PC:
    def __init__(self, name, class_name, level=1):
        self.abilities = abil_mods.Abilities()
        self.name = name
        self.level = level
        self.clas = cls.class_obj_dict[class_name]
        self.max_health = level * (self.clas.hit_die.sides + self.abilities.con_mod)
        self.health = self.max_health
        self.armor_class = 10 + self.abilities.dex_mod
        self.is_conscious = True

    def __repr__(self):
        return f"This is {self.name}, a level {self.level} {self.clas.class_name}. They have {self.health} hit points remaining." #using one[1] 's' for sake of syntax

    def level_up(self):
        self.level += 1

    def conscious(self):
        self.is_conscious = True
        if self.health == 0:
            self.health = 1
        print(f"{self.name} is conscious!")

    def unconscious(self):
        self.is_conscious = False
        if self.health != 0:
            self.health = 0
        print(f"{self.name} is unconscious!")

    def heal(self, amount):
        if self.health == 0:
            self.is_conscious = True    
        self.health += amount
        if self.health >= self.max_health:
            self.health = self.max_health
        print(f"{self.name} now has {self.health} health.")
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.is_conscious == False
        else:
            print(f"{self.name} now has {self.health} health.")
    
    def deal_damage(self, target):
        damage_amount = 0
        target.take_damage(damage_amount)
    
    def attack(self, target):
        if self.is_conscious == False:
            print(f"{self.name} can't attack because they are unconscious!")
        else:
            attack_roll = d.d20.roll
            if attack_roll >= target.armor_class:
                self.deal_damage(target)

class Monster:
    def __init__(self, monster_type, level):
        self.type = monster_type
        self.level = level
        self.max_health = 10 + level
        self.health = self.max_health
        self.armor_class = 10 + self.level

    def unconscious(self):
        self.is_conscious = False
        if self.health != 0:
            self.health = 0
        print(f"{self.name} is unconscious!")

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.unconscious()
        else:
            print(f"{self.type} now has {self.health} health.")

    def third(self):
        pass

    def __repr__(self):
        return "This is the Monster Class"

pc_name_input = str(input("Enter your characters name and hit enter:\n\n"))
lowered_name = pc_name_input.lower()
final_name = lowered_name.title()

pc_class_input = str(input("Enter your desired character class and hit enter:\n\n"))
lowered_class = pc_class_input.lower()
final_class = lowered_class.title()

pc_level_input = input("If you are creating a character above Level 1, enter your desired level in numeric form, otherwise just hit enter to continue\n\n")
if pc_level_input == '':
    completed_PC_1 = PC(final_name, final_class)
else:
    final_level = int(pc_level_input)
    completed_PC_1 = PC(final_name, final_class, final_level)

sara = PC("Sara", "Monk")
jim = PC("Jim", "Barbarian")

zombie = Monster("Zombie", 1)


print("Character Info: \n" + str(completed_PC_1))
print("Armor Class: " + str(completed_PC_1.armor_class))
print("Character Name: " + completed_PC_1.name)
print("Character Level: " + str(completed_PC_1.level))
print("Character Class: " + str(completed_PC_1.clas))
print("Max Health: " + str(completed_PC_1.max_health))
print("Current Health: " + str(completed_PC_1.health))
print("Character Ability Scores: \n" + str(completed_PC_1.abilities.abilities))
#print("\n")
#print(sara)
#print(sara.name)
#print(sara.level)
#print(sara.clas)
#print(sara.max_health)
#print(sara.health)
#print(sara.abilities.abilities)


