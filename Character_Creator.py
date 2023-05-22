import abilities_class_current as abil_clas
import Custom_Errors as CE
import DnD_Classes as cls


# Define the PC class
class PC:
    def __init__(self, name, class_name, level=1):
        self.abil_cls_obj = abil_clas.Abilities().ability_scores  # Create an instance of the Abilities class
        self.name = name  # Assign the character's name
        self.level = level  # Assign the character's level
        self.clas = cls.class_obj_dict[class_name]  # Assign the character's class from the class dictionary
        self.max_health = level * (self.clas.hit_die.sides + self.abil_cls_obj["Constitution"]['modifier'])  # Calculate the character's maximum health
        self.health = self.max_health  # Assign the character's current health
        self.armor_class = 10 + self.abil_cls_obj["Dexterity"]['modifier']  # Calculate the character's armor class
        self.is_conscious = True  # Assign a flag indicating if the character is conscious

    def __repr__(self):
        return f"This is {self.name}, a level {self.level} {self.clas.class_name}. They have {self.health} hit points remaining."

## COLLECTING CHARACTER INFO AND CREATING OBJECT ##

# Function to get the character's name
def get_character_name():
    pc_name_input = input("\nEnter your character's name and hit enter:\n\n")
    return pc_name_input.strip().title()

# Function to validate the character's class input
def validate_class_input(pc_class_input):
    return str(pc_class_input).title() in cls.class_obj_dict

# Function to get the character's class
def get_character_class():
    while True:
        try:
            pc_class_input = input("\nEnter your desired character class and hit enter:\n\n")
            if validate_class_input(pc_class_input):
                return pc_class_input.title()
            elif not validate_class_input(pc_class_input):
                raise CE.InvalidInput
        except CE.InvalidInput:
            print("Invalid Input, Please Try Again")
        else:
            break

# Function to get the character's level
def get_character_level():
    pc_level_input = input("\nIf you are creating a character above Level 1, enter your desired level in numeric form, otherwise just hit enter to continue\n\n")
    return int(pc_level_input) if pc_level_input else 1

# Function to create the character object
def create_character():
    character_name = get_character_name()
    character_class = get_character_class()
    character_level = get_character_level()
    return PC(character_name, character_class, character_level)

# Function to print the available commands
def print_available_commands():
    print("\nAvailable Commands:")
    print("1. Show Name")
    print("2. Show Level")
    print("3. Show Class")
    print("4. Show Max Health")
    print("5. Show Current Health")
    print("6. Show Armor Class")
    print("7. Show Ability Scores")
    print("8. Show Available Commands")
    print("9. Exit")

# Function to process the user's input
def process_user_input(user_input, self_pc):
    if user_input == "1":
        print("\nName:", self_pc.name)
    elif user_input == "2":
        print("\nLevel:", self_pc.level)
    elif user_input == "3":
        print("\nClass:", self_pc.clas)
    elif user_input == "4":
        print("\nMax Health:", self_pc.max_health)
    elif user_input == "5":
        print("\nCurrent Health:", self_pc.health)
    elif user_input == "6":
        print("\nArmor Class:", self_pc.armor_class)
    elif user_input == "7":
        print("\nAbility Scores:")
        for score_set in self_pc.abil_cls_obj.items():
            print(score_set[0] + ":", score_set[1])
    elif user_input == "8":
        print_available_commands()
    elif user_input == "9":
        exit()
    else:
        print("Invalid Command")

# Function to welcome the user
def welcome_user():

    print("\nWelcome to the Character Creation program!")
    print("Let's create and view your D&D character.")
    print("--------------------------------------")

# Main program entry point
def main():
    welcome_user()
    # Create the character
    self_pc = create_character()
    
    #Shows Command Menu for the first time
    print_available_commands()

    #Main program loop
    while True:
        user_input = input("\nEnter a command number: ")
        process_user_input(user_input, self_pc)

# Call the main function to start the program
if __name__ == "__main__":
    main()