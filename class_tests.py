import dice as d
        
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
