from random import sample
from rich import print
from encounters.events.events import *
from encounters.combat.combats import *
from characters.companions import *
from characters.create_custom_character import create_custom_character
from tools.menu import menu
from tools.print_list import print_list
from tools.rich_capitalize import rich_capitalize
from tools.enums import MenuOptions


def main():

    companions = [Astarion, Gale, Karlach, Laezel, Shadowheart, Wyll, Minthara, Halsin, Jaheira, Minsc] 
    combats = [Goblins_4x, OwlbearMother, UndeadGroup, Training]
    events = [SwordInStone]

    party = []

    if input('Press [ENTER] to start.') == 'dev':
        
        encounter = Goblins_4x
        party = [Astarion, Karlach, Gale, Shadowheart]

        party = encounter.begin(party)
    
    while True:
        match menu(options=["Begin campaign", "Choose party", "Face an encounter", "Add custom character", "Romance"], menu_text="What would you like to do?"):
            
            case "Begin campaign":

                if not party:
                    party = pick_party(companions)
                if not party:
                    continue
                
                campaign = [
                    Goblins_4x, 
                    SwordInStone,
                    OwlbearMother,
                    UndeadGroup, 
                ]

                for item in campaign:
                    party = item.begin(party)
                    party = group_long_rest(party)

            case "Choose party":
                if party:
                    companions.extend(party)
                party = pick_party(companions)

            case "Face an encounter":
                
                if not party:
                    party = pick_party(companions)
                if not party:
                    continue

                match menu(options=["Combat", "Event"], menu_text="What kind of encounter would you like to face?"):
                    case "Combat":
                        party = menu(options=combats, menu_text="Who would you like to fight?").begin(party)
                    case "Event":
                        party = menu(options=events, menu_text="What event would you like to experience?").begin(party)

                party = []

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


def pick_party(companions_originalList=list):
    
    companions = list(companions_originalList)

    companions.extend(["Custom character", None, MenuOptions.nevermind])
    party = []

    for x in range(4):
        
        while True:
            selection = menu(companions, f"Who would you like in your party? ({4-x} slots remaining.)", show_race=True, show_class=True)

            if selection or party:
                break
            print("You must have at least one character in your party!")
        
        # Selection: Nevermind
        if selection == MenuOptions.nevermind:
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