import dice as d

class Class:
  classes = {
    "Barbarian":d.d12,
    "Bard":      d.d8,
    "Cleric":    d.d8,
    "Druid":     d.d8,
    "Fighter":  d.d10,
    "Monk":      d.d8,
    "Paladin":  d.d10,
    "Ranger":   d.d10,
    "Rogue":     d.d8,
    "Sorcerer":  d.d6,
    "Warlock":   d.d8,
    "Wizard":    d.d6
  }
  def __init__(self, class_name): 
    self.hit_die = Class.classes[class_name] #using one[1] 's' for sake of syntax
    self.class_name = [clas for clas, die in Class.classes.items() if die == self.hit_die][0]

  def __repr__(self):
    return f"This is the {self.class_name} class. It's hit die is a d{self.hit_die.sides}."

#class Barbarian(Class):

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

#print(barbarian)

"""class_list = [
  barbarian,
  bard,
  cleric,
  druid,
  fighter,
  monk,
  paladin,
  ranger,
  rogue,
  sorcerer,
  warlock,
  wizard
]"""

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

"""class_obj_dict = {
  "Barbarian": Class("Barbarian"),
  "Bard": Class("Bard"),
  "Cleric": Class("Cleric"),
  "Druid": Class("Druid"),
  "Fighter": Class("Fighter"),
  "Monk": Class("Monk"),
  "Paladin": Class("Paladin"),
  "Ranger": Class("Ranger"),
  "Rogue": Class("Rogue"),
  "Sorcerer": Class("Sorcerer"),
  "Warlock": Class("Warlock"),
  "Wizard": Class("Wizard")
}"""
#class_obj_dict["Fighter".lower()]