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

    romance_availability_confirmed = False
    romance_blocked=False

    if input('Press [ENTER] to start.') == 'dev':
        Karlach.equip_item(Longsword_plus1)
        Party.active_party = [BingusGringus, Nightkill, Karlach, Shadowheart]
        Party.do_encounter(Goblins_4x)

    main_menu_options = ["Begin campaign", "Choose party", "Face an encounter", "Add custom character", "Romance"]

    while True:
        match menu(options=main_menu_options, menu_text="What would you like to do?"):
            
            case "Begin campaign":
                campaign(Party=Party, romance_availability_confirmed=romance_availability_confirmed, romance_blocked=romance_blocked)
                
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
                romance_availability_confirmed, romance_blocked = romance(companions=Party.companions, romance_availability_confirmed=romance_availability_confirmed)
                if romance_blocked and "Romance" in main_menu_options:
                    main_menu_options.remove("Romance")
        
            case _:
                print("Invalid option!")


def campaign(Party: PartyInfo, romance_availability_confirmed: bool = False, romance_blocked: bool = False):
    
    campaign_encounters = [
        Goblins_4x, 
        SwordInStone,
        OwlbearMother,
        UndeadGroup, 
    ]

    camp_menu_options = ["Go to next encounter", "Change active party", "Manage equipment", "Long rest", "Romance"]
    if romance_blocked: 
        camp_menu_options.remove("Romance")

    while True:
        match menu(options=camp_menu_options, menu_text="What would you like to do?"):
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
                romance_availability_confirmed, romance_blocked = romance(companions=Party.companions, romance_availability_confirmed=romance_availability_confirmed)
                if romance_blocked and "Romance" in camp_menu_options:
                    camp_menu_options.remove("Romance")

            case _:
                print("Invalid option!")


def romance(companions, romance_availability_confirmed):
    romance_blocked = False
    if not romance_availability_confirmed:
        romance_availability_confirmed = True
        romance_blocked = menu(menu_text='This feature is only available to players aged 18 years and older. By entering "Yes", you confirm that you are old enough to access this feature.', options=["Yes", "No"]) == "No"
    
    if romance_blocked: 
        return romance_availability_confirmed, True
            
    romanceable_companions = list(companions)
    for char in [Nightkill]:
        if char in romanceable_companions:
            romanceable_companions.remove(char)
    if len(romanceable_companions) == 0:
        print("There are no romanceable companions!")
    if len(romanceable_companions) == 1:
        print(f"{romanceable_companions[0]} goes to town on that thang.")
    if len(romanceable_companions) >=2:
        sex_havers = sample(romanceable_companions, 2)
        print(f"{sex_havers[0]} fucks the shit out of {sex_havers[1]}.")
    
    return romance_availability_confirmed, False


if __name__ == "__main__":
    main()