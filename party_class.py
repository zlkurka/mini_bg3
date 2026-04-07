from characters.create_custom_character import create_custom_character
from tools.menu import menu
from tools.print_list import print_list
from tools.enums import MenuOptions

class PartyInfo():
    
    def __init__(self, companions: list = [], gold: int = 0, items: list = [], active_party: list = []):
        self.companions: list =list(companions)
        self.gold: int = gold
        self.items: list = list(items)
        self.active_party: list = list(active_party)
    
    def embark(self, encounter):
        if not self.active_party:
            self.pick_party()
        
        encounter.begin(self.active_party)

    def pick_party(self):
    
        character_options = list(self.companions)

        character_options.extend(["Custom character", MenuOptions.nevermind])
        self.active_party = []

        for x in range(4):
            
            while True:
                selection = menu(character_options, f"Who would you like in your party? ({4-x} slots remaining.)", show_race=True, show_class=True)

                if selection or self.active_party:
                    break
                print("You must have at least one character in your party!")
            
            # Selection: Nevermind
            if selection == MenuOptions.nevermind:
                self.active_party = []
                return
            
            # Selection: None
            if not selection:
                return
            
            # Selection: New custom
            if selection == "Custom character":
                self.add_custom_character()
            
            else:
                self.active_party.append(selection)
                if selection in character_options:
                    character_options.remove(selection)
            
            if None not in character_options:
                character_options.append(None)
        
        print_list(self.active_party, "You embark with")
    
    def group_long_rest(self):
        for char in self.companions:
            char.long_rest()

    def add_custom_character(self):
        custom_character = create_custom_character()
        if custom_character:
            self.companions.append(custom_character)