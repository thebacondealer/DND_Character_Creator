import abilities_class as abil_class
import dice as d
import classes as cls

class PC:
    def __init__(self, name, class_name, level=1):
        self.abilities = abil_class.Abilities()
        self.name = name
        self.level = level
        self.clas = cls.class_obj_dict[class_name]
        self.max_health = level * (self.clas.hit_die.sides + self.abilities.con_mod)
        self.health = self.max_health
        self.armor_class = 10 + self.abilities.dex_mod
        self.is_conscious = True

    def __repr__(self):
        return f"This is {self.name}, a level {self.level} {self.clas.class_name}. They have {self.health} hit points remaining." #using one[1] 's' for sake of syntax

    
## PROGRAM START ##
desired_funtion = input("\nWould you like to use the Character Creator, or, play the Dungeon?\n\n")
lowered_func = desired_funtion.lower()

if lowered_func == "dungeon":
    import Dungeon
    Dungeon
elif lowered_func == "character creator" or "cc":
    pass

## COLLECTING CHARACTER INFO AND CREATING OBJECT ##
def create_character():
    pc_name_input = input("\nEnter your characters name and hit enter:\n\n")
    lowered_name = pc_name_input.lower()
    final_name = lowered_name.title()
    
    pc_class_input = input("\nEnter your desired character class and hit enter:\n\n")
    lowered_input = pc_class_input.lower()
    lowered_class = cls.class_list

    if lowered_input not in lowered_class:
        print("Invalid Input, Please Try Again")
        #pc_class_input = input("\nEnter your desired character class and hit enter:\n\n")
    else:
        final_class = lowered_input.title()

    pc_level_input = input("\nIf you are creating a character above Level 1, enter your desired level in numeric form, otherwise just hit enter to continue\n\n")
    if pc_level_input == '':
        self_PC = PC(final_name, final_class)
    else:
        final_level = int(pc_level_input)
        self_PC = PC(final_name, final_class, final_level)
    return self_PC

self_PC = create_character()

def print_name():
    print("Your name is: " + self_PC.name)

def print_abilities():
    print(self_PC.abilities)

def print_level():
    print("You are level " + str(self_PC.level))

def print_class():
    print(self_PC.clas)

def print_max_health():
    print(self_PC.max_health)

def print_health():
    print(self_PC.health)

def print_armor_class():
    print(self_PC.armor_class)

def print_character():
    print(self_PC)

def run_menu():
        print("Available Commands:\n")
        
        available_commands = {
            "Show Name": print_name(), 
            "Show Abilities": print_abilities(),
            "Show Level": print_level(),
            "Show Class": print_class(),
            "Show Max Health": print_max_health(),
            "Show Health": print_health(),
            "Show Armor Class": print_armor_class(),
            "Show Character": print_character(),
            "\nCreate New Character": create_character(),
            "\n\nExit": exit()
        }

        #print(stringavailable_commands.keys())

        """get_command = input("Input a Command\n\n")
        lowered_command = get_command.lower()
        if lowered_command in available_commands:
            for command in available_commands:
                if lowered_command in command:
                    available_commands[command]
            
        elif lowered_command == "exit":
            exit()"""

#run_menu()
#sara = PC("Sara", "Monk")
#jim = PC("Jim", "Barbarian")

#zombie = Monster("Zombie", 1)

#print("Character Info: \n" + str(completed_PC_1))
#print("Armor Class: " + str(completed_PC_1.armor_class))
#print("Character Name: " + completed_PC_1.name)
#print("Character Level: " + str(completed_PC_1.level))
#print(str(self_PC.clas))
#print("Max Health: " + str(completed_PC_1.max_health))
#print("Current Health: " + str(completed_PC_1.health))
print(str(self_PC.abilities))
#print("\n")
#print(sara)
#print(sara.name)
#print(sara.level)
#print(sara.clas)
#print(sara.max_health)
#print(self_PC.health)
#print(sara.abilities.abilities)
