from random import shuffle, sample
from rich import print
from event import SwordInStone
from characters.companions import *
from characters.monsters import get_monsters
from characters.create_custom_character import create_custom_character
from conditions.condition import conditions_removed_at_turn_start, conditions_removed_at_turn_end
from tools.menu import menu
from tools.print_list import print_list
from tools.enums import Encounter, CharacterType
from tools.rich_capitalize import rich_capitalize


def main():

    companions = [Astarion, Gale, Karlach, Laezel, Shadowheart, Wyll, Minthara, Halsin, Jaheira, Minsc] 
    encounters = [Encounter.goblins_4x, Encounter.owlbear, Encounter.training_dummy]
    party = []

    if input('Press [ENTER] to start.') == 'dev':
        party = [Bard, Karlach, Gale, Shadowheart]
        encounter = Encounter.goblins_4x
        party = combat(party, encounter)
    
    while True:
        match menu(options=["Begin campaign", "Fight some monsters", "Choose party", "Add custom character", "Romance"], menu_text="What would you like to do?"):
            
            case "Begin campaign":

                if not party:
                    party = pick_party(companions)
                if not party:
                    continue
                
                party = combat(party, Encounter.goblins_4x)
                party = group_long_rest(party)

                party = SwordInStone.begin(party)
                party = combat(party, Encounter.owlbear)
                party = group_long_rest(party)

            case "Fight some monsters":
                
                if not party:
                    party = pick_party(companions)
                if not party:
                    continue
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

            case "Romance":
                while True:
                    sex_havers = sample(companions, 2)
                    if Nightkill not in sex_havers:
                        break
                print(f"{sex_havers[0]} fucks the shit out of {sex_havers[1]}.")
        
            case _:
                print("Invalid option!")


def combat(party=list, encounter=Encounter):

    monsters = get_monsters(encounter)
    original_party = list(party)

    # Roll initiative
    initiative_rolls = {}
    for char in party + monsters:
        roll = char.ability_check(ability_type = Skill.initiative)
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
        print("- " + rich_capitalize(fighter))
    
    initiative = 0
    
    # Combat
    while True:
        
        fighter = fighters[initiative]

        initiative += 1
        if initiative >= len(fighters):
            initiative = 0

        if fighter.current_hp <= 0:
            continue
        
        print()
        for condition in fighter.conditions:
            if condition in conditions_removed_at_turn_start:
                fighter.conditions.remove(condition)

        # Do action
        if fighter.character_type == CharacterType.companion:
            monsters, party, fighters = fighter.action(enemies=monsters, team=party, fighters=fighters)
        elif fighter.character_type == CharacterType.monster:
            party, monsters, fighters = fighter.action(enemies=party, team=monsters, fighters=fighters)
        else:
            print("Error: unacceptable character type!")
            monsters, party, fighters = fighter.action(enemies=monsters, team=party, fighters=fighters)
        
        for condition in fighter.conditions:
            if condition in conditions_removed_at_turn_end:
                fighter.conditions.remove(condition)

        if not party:
            print("\nYou lose!\n")
            return party
            
        if not monsters:
            print("\nYou win!\n")

            for char in original_party:
                if char in party:
                    print(f"{char.name}: {char.current_hp} HP remaining.")
                else:
                    print(f"{char.name}: died in combat.")
        
            print()
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


def group_long_rest(party):
    for char in party:
        char.long_rest()
    return party

if __name__ == "__main__":
    main()