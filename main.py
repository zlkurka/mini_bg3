from random import sample
from rich import print
from party.party_class import PartyInfo
from encounters.events.events import *
from encounters.combat.combats import *
from characters.companions import *
from tools.menu import menu
from items.consumables import MinorHealthPotion

def main():

    companions = [Nightkill, Faylen, BingusGringus, Gale, Karlach, Laezel, Shadowheart, Bard, Monk, Minsc, TheDev]
    Party = PartyInfo(companions=companions)

    combats = [Goblins_4x, OwlbearMother, UndeadGroup, Training]
    events = [TheInjuredAdventurer, SwordInStone, TheMurderHobo]

    romance_availability_confirmed = False
    romance_blocked=False

    Party.items.append(MinorHealthPotion)
    
    if input('Press [ENTER] to start.') == 'dev':
        Party.active_party = [Gale, Shadowheart, Karlach, Nightkill]
        Party.do_encounter(TheMurderHobo)

    main_menu_options = ["Begin campaign", "Choose party", "Face an encounter", "Add custom character", "Romance"]

    while True:
        
        Party.group_long_rest()
        
        match menu(options=main_menu_options, menu_text="[bold]Main Menu[/bold]"):
            
            case "Begin campaign":
                campaign(romance_availability_confirmed=romance_availability_confirmed, romance_blocked=romance_blocked)
                
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


def campaign(romance_availability_confirmed: bool = False, romance_blocked: bool = False):
    
    campaign_encounters = [
        TheInjuredAdventurer,
        SwordInStone,
        Goblins_4x, 
        OwlbearMother,
        TheMurderHobo,
        UndeadGroup, 
    ]

    Party = PartyInfo()
    starting_character = menu(menu_text="Who would you like to start the game as?", options=[Nightkill, Faylen, BingusGringus, Gale, Karlach, Laezel, Shadowheart, Bard, Monk, Minsc, TheDev, "Custom character"])
    if starting_character == "Custom character":
        starting_character = Party.add_custom_character()
    Party.companions.append(starting_character)
    Party.active_party.append(starting_character)

    camp_menu_options = ["Go to next encounter", "Change active party", "Manage equipment", "Long rest", "Cast spells", "Romance"]
    if romance_blocked: 
        camp_menu_options.remove("Romance")

    while True:
        match menu(options=camp_menu_options, menu_text="\n[bold]Camp[/bold]"):
            case "Go to next encounter":
                if Party.do_encounter(campaign_encounters[0]) == "game over":
                    return
                campaign_encounters.pop(0)

            case "Change active party":
                Party.pick_party()

            case "Manage equipment":
                Party.manage_equipment()

            case "Long rest":
                Party.group_long_rest()

            case "Cast spells":
                menu(menu_text="Who should cast some spells?", options=Party.active_party).action(enemies=[], team=Party.active_party, fighters=Party.active_party, items=Party.items)

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