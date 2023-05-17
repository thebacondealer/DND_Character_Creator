## GAME COMMANDS ##

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

    def deal_damage(self, target):
        damage_amount = 0
        target.take_damage(damage_amount)

    def __repr__(self):
        return "This is the Monster Class"
    
## STARTING ROOM ##
print("\nYou blearily open your eyes. \nYour head is throbbing, as if it's been rung repeatedly against something.\n\nWho are you?") 

## COLLECTING CHARACTER INFO AND CREATING OBJECT ##
pc_name_input = input("\nEnter your characters name and hit enter:\n\n")
lowered_name = pc_name_input.lower()
final_name = lowered_name.title()

pc_class_input = input("\nEnter your desired character class and hit enter:\n\n")
lowered_class = pc_class_input.lower()
final_class = lowered_class.title()

pc_level_input = input("\nIf you are creating a character above Level 1, enter your desired level in numeric form, otherwise just hit enter to continue\n\n")
if pc_level_input == '':
    completed_PC_1 = PC(final_name, final_class)
else:
    final_level = int(pc_level_input)
    completed_PC_1 = PC(final_name, final_class, final_level)

print("\nYou shakily pull yourself off the wet floor to your feet. You don't recognize the room you're standing in and you don't remember how you got here.\nYou should try to find a way out.")
print("The room yor're in is dark and there's a dripping sound coming from the corner. You can make out a doorway in the wall accros from you.")

## ROOM  1 ##:
"\nThis is a plain square room made of smooth, cool, dark stone"

## ROOM  2 ##:
## ROOM  3 ##:
## ROOM  4 ##:
## ROOM  5 ##:
## EXIT SEQUENCE ##:
'''5 room text dungeon crawl. 5 rooms, 5 monsters of increasing difficulty.
    starting area
    Room 1
    Room 2
    Room 3
    Room 4
    Room 5
    exit sequence