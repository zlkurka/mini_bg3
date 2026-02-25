from random import shuffle
from tools.menu import menu
from tools.print_list import print_list
from characters.companions import Astarion, Gale, Karlach, Laezel, Shadowheart, Wyll
from characters.monsters import get_monsters
from tools.enums import Encounter
from tools.defaults import char_classes, char_races, ability_scores
from tools.character import Companion


def main():
    
    # Set to False if you want to play normal-mode. Sorry if I leave it on True
    DEV_MODE = False

    companions = [Astarion, Gale, Karlach, Laezel, Shadowheart, Wyll] 
    encounters = [Encounter.goblins_4x, Encounter.owlbear, Encounter.training_dummy]
    
    if DEV_MODE:
        
        party = [Wyll, Shadowheart, Karlach, Laezel]
        encounter = Encounter.goblins_4x
    
    else:
        party = pick_party(companions)
        encounter = menu(encounters, "Who would you like to fight?")

    party = combat(party, encounter)


def combat(party=list, encounter=Encounter):

    monsters = get_monsters(encounter)
    original_party = list(party)

    # Initiative
    fighters = party + monsters
    shuffle(fighters)
    
    print("\nInitiative: ")
    for fighter in fighters:
        print("- " + str(fighter).capitalize())
    
    initiative = 0
    skipped_fighters = []
    
    # Combat
    while True:
        
        fighter = fighters[initiative]

        initiative += 1
        if initiative >= len(fighters):
            initiative = 0

        if fighter in skipped_fighters:
            continue

        monsters, party, skipped_fighters = fighter.action(monsters, party, skipped_fighters)

        if not party:
            print("You lose!")
            return party
        if not monsters:
            print("\nYou win!\n")

            for char in original_party:
                if char in party:
                    print(f"{char.name}: {char.current_hp} HP remaining.")
                else:
                    print(f"{char.name}: died in combat.")

            return party


def pick_party(companions=list):
    
    companions.extend(["New custom character", None])
    party = []

    for x in range(4):
        
        while True:
            selection = menu(companions, f"Who would you like in your party? ({4-x} slots remaining.)", show_race=True, show_class=True)

            if selection or party:
                break
            print("You must have at least one character in your party!")
        
        # Selection: None
        if not selection:
            break
        
        # Selection: New custom
        if selection == "New custom character":
            custom_character = create_custom_character()
            if custom_character:
                selection = custom_character
        
        party.append(selection)
        if selection in companions:
            companions.remove(selection)
    
    print_list(party, "You embark with")
    return party


def create_custom_character():

    match menu(['Yes','No'], "Would you like to load a character from an existing save?"):
        case 'Yes':
            return None
        case 'No':
            pass
        case _: 
            print("Invalid option!")
            return None
    
    custom_character_name = input("Enter your character's name: ")
    custom_character_charclass = menu(char_classes, "Select your character's class.")
    custom_character_race = menu(char_races, "Select your character's race.")
    custom_character_level = 1
    custom_character_ability_scores = {}
    
    standard_array_scores = [3, 2, 1, 0, 0, -1]
    for score in ability_scores:
        score_assigned = menu(standard_array_scores, f"What score would you like to assign to {score}?")
        standard_array_scores.remove(score_assigned)
        custom_character_ability_scores.update({score: score_assigned})
    
    custom_character  = Companion(name=custom_character_name, charclass=custom_character_charclass, race=custom_character_race, level=custom_character_level, ability_scores=custom_character_ability_scores)
    
    return custom_character


main()