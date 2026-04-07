from random import sample
from rich import print
from party_class import PartyInfo
from encounters.events.events import *
from encounters.combat.combats import *
from characters.companions import *
from tools.menu import menu


def main():

    Party = PartyInfo(companions=[Nightkill, Faylen, BingusGringus, Gale, Karlach, Laezel, Shadowheart, Wyll])

    combats = [Goblins_4x, OwlbearMother, UndeadGroup, Training]
    events = [SwordInStone]

    if input('Press [ENTER] to start.') == 'dev':
        
        Party.active_party = [Nightkill, Karlach, BingusGringus, Shadowheart]
        Party.embark(Goblins_4x)
    
    while True:
        match menu(options=["Begin campaign", "Choose party", "Face an encounter", "Add custom character", "Romance"], menu_text="What would you like to do?"):
            
            case "Begin campaign":

                campaign = [
                    Goblins_4x, 
                    SwordInStone,
                    OwlbearMother,
                    UndeadGroup, 
                ]

                for encounter in campaign:
                    Party.embark(encounter)
                    Party.group_long_rest()

            case "Choose party":
                Party.pick_party()

            case "Face an encounter":
                match menu(options=["Combat", "Event"], menu_text="What kind of encounter would you like to face?"):
                    case "Combat":
                        Party.embark(menu(options=combats, menu_text="Who would you like to fight?"))
                    case "Event":
                        Party.embark(menu(options=events, menu_text="Who would you like to fight?"))

            case "Add custom character":
                Party.add_custom_character()

            case "Romance":
                while True:
                    sex_havers = sample(Party.companions, 2)
                    if Nightkill not in sex_havers:
                        break
                print(f"{sex_havers[0]} fucks the shit out of {sex_havers[1]}.")
        
            case _:
                print("Invalid option!")

if __name__ == "__main__":
    main()