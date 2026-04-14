from random import sample
from rich import print
from party_class import PartyInfo
from encounters.events.events import *
from encounters.combat.combats import *
from characters.companions import *
from tools.menu import menu


def main():

    Party = PartyInfo(companions=[Nightkill, Faylen, BingusGringus, Gale, Karlach, Laezel, Shadowheart, Bard, Monk, Minsc, TheDev])

    combats = [Goblins_4x, OwlbearMother, UndeadGroup, Training]
    events = [SwordInStone]

    if input('Press [ENTER] to start.') == 'dev':
        Karlach.equip_item(Longsword_plus1)
        Party.active_party = [BingusGringus, Nightkill, Karlach, Shadowheart]
        Party.do_encounter(Goblins_4x)

    while True:
        match menu(options=["Begin campaign", "Choose party", "Face an encounter", "Add custom character", "Romance"], menu_text="What would you like to do?"):
            
            case "Begin campaign":
                campaign(Party)
                
            case "Choose party":
                Party.pick_party()

            case "Face an encounter":
                match menu(options=["Combat", "Event"], menu_text="What kind of encounter would you like to face?"):
                    case "Combat":
                        Party.do_encounter(menu(options=combats, menu_text="Who would you like to fight?"))
                    case "Event":
                        Party.do_encounter(menu(options=events, menu_text="What event would you like to experience?"))

            case "Add custom character":
                Party.add_custom_character()

            case "Romance":
                romance(Party.companions)
        
            case _:
                print("Invalid option!")


def campaign(Party: PartyInfo):
    
    campaign_encounters = [
        Goblins_4x, 
        SwordInStone,
        OwlbearMother,
        UndeadGroup, 
    ]
    
    while True:
        match menu(options=["Go to next encounter", "Change active party", "Manage equipment", "Long rest", "Romance"], menu_text="What would you like to do?"):
            case "Go to next encounter":
                Party.do_encounter(campaign_encounters[0])
                campaign_encounters.pop(0)

            case "Change active party":
                Party.pick_party()

            case "Manage equipment":
                Party.manage_equipment()

            case "Long rest":
                Party.group_long_rest()

            case "Romance":
                romance(Party.companions)

            case _:
                print("Invalid option!")


def romance(companions):
    romanceable_companions = list(companions)
    for char in [Nightkill]:
        if char in romanceable_companions:
            romanceable_companions.remove(char)
    if len(romanceable_companions) == 0:
        print("There are no romanceable companions!")
    if len(romanceable_companions) == 1:
        print(f"{romanceable_companions[0]} goes to town on that thang.")
    if len(romanceable_companions) ==2:
        sex_havers = sample(romanceable_companions, 2)
        print(f"{sex_havers[0]} fucks the shit out of {sex_havers[1]}.")


if __name__ == "__main__":
    main()