from random import randint
from rich import print
from tools.menu import menu
from tools.rich_capitalize import rich_capitalize
from tools.enums import Dice, RollAlteration, BuffCondition, RollType

def roll_d20(character = None, roll_bonus: int = 0, print_feedback: bool = True, roll_type: RollType = None):

    roll = randint(1, Dice.d20.value)
    
    if not character:
        return roll + roll_bonus

    # Adding alterations from conditions

    advantage_given = False
    disadvantage_given = False
    flat_modifier = 0
    dice_modifier = {}
    dice_total_bonus = 0

    for cond in list(character.conditions):
        if cond.applicable_roll_type != roll_type:
            continue
        
        alteration = cond.roll_alteration
        
        if cond.name == BuffCondition.bardic_inspiration:
            match menu(menu_text=f"Would {character} like to use their {BuffCondition.bardic_inspiration}?",options=["Yes","No"]):
                case "Yes":
                    character.conditions.remove(cond)
                case "No":
                    continue
                case _:
                    print("Invalid input!")

        if alteration == RollAlteration.advantage:
            advantage_given = True
        if alteration == RollAlteration.disadvantage:
            disadvantage_given = True
        if alteration == RollAlteration.flat_modifer:
            flat_modifier = cond.modifier
        if alteration == RollAlteration.dice_modifier:
            
            proposed_bonus = 0
            for die in cond.dice:
                proposed_bonus += (die.value // 2) + 1

            if proposed_bonus > dice_total_bonus:
                dice_modifier = cond.dice
                dice_total_bonus = proposed_bonus

    if advantage_given and disadvantage_given:
        advantage_given = False
        disadvantage_given = False

    # Advantage and disadvantage
    if advantage_given:
        roll = max(roll, randint(1, Dice.d20.value))
    elif disadvantage_given:
        roll = min(roll, randint(1, Dice.d20.value))
    original_roll = int(roll)
    
    roll += roll_bonus

    # Flat modifier
    roll += flat_modifier

    # Dice modifier
    dice_modification = 0
    for die in dice_modifier:
        dice_modification += randint(1, die.value)
    roll += dice_modification
    
    if not print_feedback:
        return roll

    # Printing roll
    if advantage_given:
        print(f"With advantage, {character}", end="")
    elif disadvantage_given:
        print(f"With disadvantage, {character}", end="")
    else:
        print(rich_capitalize(character), end="")

    print(f" rolled {roll} ({original_roll}", end="")
    
    if roll_bonus > 0:
        print(f" + {roll_bonus}", end="")
    if roll_bonus < 0:
        print(f" - {roll_bonus * -1}", end="")

    if flat_modifier > 0:
        print(f" + {flat_modifier}", end="")
    if flat_modifier < 0:
        print(f" - {flat_modifier * -1}", end="")

    if dice_modification > 0:
        print(f" + {dice_modification}", end="")
    if dice_modification < 0:
        print(f" - {dice_modification * -1}", end="")

    print(").")
    return roll