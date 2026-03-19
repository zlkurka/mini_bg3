from random import shuffle
from tools.menu import menu
from tools.print_list import print_list
from tools.enums import Encounter, CharacterType
from tools.defaults import char_classes, char_races, ability_scores
from tools.save_handler import load_character, save_character
from characters.companions import *
from characters.monsters import get_monsters


def main():

    companions = [Astarion, Gale, Karlach, Laezel, Shadowheart, Wyll, Minthara, Halsin, Jaheira, Minsc] 
    encounters = [Encounter.goblins_4x, Encounter.owlbear, Encounter.training_dummy]
    party = []

    if input('Press [ENTER] to start.') == 'dev':    
        party = [Gale, Shadowheart, Karlach, Laezel]
        encounter = Encounter.owlbear
        party = combat(party, encounter)
    
    while True:
        match menu(["Go to combat", "Choose party", "Add custom character", "Save a character to file",], "What would you like to do?"):
            
            case "Go to combat":
                
                if not party:
                    party = pick_party(companions)

                for char in party:
                    companions.remove(char)

                encounter = menu(encounters, "Who would you like to fight?")
                party = combat(party, encounter)

                companions.extend(party)
                party = []
            
            case "Choose party":
                if party:
                    companions.extend(party)
                party = pick_party(companions)
            
            case "Add custom character":
                companions.append(create_custom_character())
            
            case "Save a character to file":
                save_character(menu(companions, "Which character would you like to save?", show_race=True, show_class=True))
        
            case _:
                print("Invalid option!")


def combat(party=list, encounter=Encounter):

    monsters = get_monsters(encounter)
    original_party = list(party)

    # Roll initiative
    initiative_rolls = {}
    for char in party + monsters:
        roll = 1
        if roll not in initiative_rolls:
            initiative_rolls.update({roll: [char]})
        else: 
            chars_at_initiative = initiative_rolls[roll]
            chars_at_initiative.append(char)
            initiative_rolls.update({roll: chars_at_initiative})
    
    fighters = list(initiative_rolls.keys())
    fighters.sort()
    fighters.reverse()

    for roll in list(fighters):
        chars = initiative_rolls[roll]
        if type(chars) != list:
            chars = [chars]
        else:
            shuffle(chars)
        for char in chars:
            fighters.append(char)
        fighters.remove(roll)

    # Print initiative
    print("\nInitiative: ")
    for fighter in fighters:
        print("- " + str(fighter).capitalize())
    
    initiative = 0
    
    # Combat
    while True:
        
        fighter = fighters[initiative]

        initiative += 1
        if initiative >= len(fighters):
            initiative = 0

        if fighter.current_hp <= 0:
            continue
        
        monsters, party, fighters = fighter.action(monsters, party, fighters)
        
        if not party:
            print("You lose!")
            return []
        if not monsters:
            print("\nYou win!\n")

            for char in original_party:
                if char in party:
                    print(f"{char.name}: {char.current_hp} HP remaining.")
                else:
                    print(f"{char.name}: died in combat.")

            return party


def pick_party(companions_originalList=list):
    
    companions = list(companions_originalList)

    companions.extend(["Custom character", None, "Nevermind"])
    party = []

    for x in range(4):
        
        while True:
            selection = menu(companions, f"Who would you like in your party? ({4-x} slots remaining.)", show_race=True, show_class=True)

            if selection or party:
                break
            print("You must have at least one character in your party!")
        
        # Selection: Nevermind
        if selection == "Nevermind":
            return []
        
        # Selection: None
        if not selection:
            break
        
        # Selection: New custom
        if selection == "Custom character":
            custom_character = create_custom_character()
            if custom_character:
                selection = custom_character
                companions_originalList.append(selection)
        
        party.append(selection)
        if selection in companions:
            companions.remove(selection)
    
    print_list(party, "You embark with")
    return party


def create_custom_character():

    match menu(['Create character','Load character'], "Would you like to create a new character or load a pre-existing one?"):
        case 'Create character':
            pass
        case 'Load character':
            loaded_character = load_character()
            if loaded_character:
                return loaded_character
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
    
    custom_character = Character(name=custom_character_name, character_type=CharacterType.companion, charclass=custom_character_charclass, race=custom_character_race, level=custom_character_level, ability_scores=custom_character_ability_scores)
    
    match menu(['Yes', 'No'], "Would you like to save this character?"):
        case 'Yes':
            save_character(custom_character)
        case 'No':
            pass
        case _:
            print('Invalid option!')

    return custom_character


main()