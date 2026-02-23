from random import shuffle
from tools.menu import menu
from tools.character import Companion, Monster
from characters.companions import Astarion, Gale, Karlach, Laezel, Shadowheart, Wyll
from characters.monsters import get_monsters
from tools.enums import Encounter

def main():
    
    # Set to False if you want to play normal-mode. Sorry if I leave it on True
    DEV_MODE = True

    companions = [Astarion, Gale, Karlach, Laezel, Shadowheart, Wyll] 
    encounters = [Encounter.goblins_4x, Encounter.owlbear]
    
    if DEV_MODE:
        
        party = [Wyll, Shadowheart, Karlach, Laezel]
        encounter = Encounter.owlbear
    
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
        print("- " + fighter.name.capitalize())
    
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
            print("You win!\n")

            for char in original_party:
                if char in party:
                    print(f"{char.name}: {char.current_hp} HP remaining.")
                else:
                    print(f"{char.name}: died in combat.")

            return party


def pick_party(companions=list):
    
    companions.append(None)
    party = []

    for x in range(4):
        
        while True:
            selection = menu(companions, f"Who would you like to in your party? ({4-x} slots remaining.)")
        
            if selection or party:
                break
            
            print("You must have at least one character in your party!")
        
        if not selection:
            break

        party.append(selection)
        companions.remove(selection)
    
    if len(party) == 1:
        print(f"You embark with {party[0].name}!")
        return party
    
    if len(party) == 2:
        print(f"You embark with {party[0].name} and {party[1].name}!")
        return party

    print("You embark with ", end="")
    for char in party:
        
        if (len(party) - 1) - party.index(char) >= 2:
            # e.g., member 0 or 1 of 4
            print(char.name, end=", ")
        
        if (len(party) - 1) - party.index(char) == 1:
            # e.g., member 2 of 3 or 3 of 4
            print(char.name, end=", and ")
        
        if (len(party) - 1) - party.index(char) == 0:
            # last member of party
            print(char.name, end="!\n")
    
    return party


main()