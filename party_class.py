from rich import print
from characters.create_custom_character import create_custom_character
from characters.character_class import Character
from actions.attacks.attacks import Attack
from actions.action_class import Action
from items.item_class import Item
from tools.defaults import empty_spell_slots
from tools.rich_capitalize import rich_capitalize
from tools.menu import menu
from tools.print_list import print_list
from tools.enums import MenuOptions

class PartyInfo():
    
    def __init__(self, companions: list = [], gold: int = 0, items: list = [], active_party: list = []):
        self.companions: list =list(companions)
        self.gold: int = gold
        self.items: list = list(items)
        self.active_party: list = list(active_party)
    
    def do_encounter(self, encounter):
        if not self.active_party:
            self.pick_party()
        
        loot = encounter.begin(self.active_party)
        self.attain_loot(loot)

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
    
    def attain_loot(self, loot):
        if not loot:
            return
        
        for item in loot:

            if type(item) == Character:
                print(f"Companion found: {item}")
                self.companions.append(Character)
                continue
            
            if type(item) == Item:
                print(f"Item attained: {item}")
                self.items.append(item)
                continue
            
            if type(item) == Action or Attack:
                
                if item and item.spell_slot_level > 0:
                    print(f"Spell attained: {item}")
                    recipient_options = []
                    for char in self.companions:
                        if char.spell_slots != empty_spell_slots:
                            recipient_options.append(char)
                else:
                    print(f"Special action attained: {item}")
                    recipient_options = self.companions

                character_choice = menu(menu_text="Who should recieve this?", options=recipient_options)
                character_choice.actions.append(item)
                print(f"{rich_capitalize(item)} added to {character_choice}'s actions.")
                continue

    def manage_equipment(self):
        
        equippable_items = []
        for itm in self.items:
            if itm.is_equippable:
                equippable_items.append(itm)
        
        while True:
            match menu(options=["View equipped items", "Unequip all items", "Go back"], menu_text="What would you like to do?"):
                case "View equipped items":
                    character_choice = menu(menu_text="Whose items would you like to see?", options=list(self.companions) + ["All"])
                    if character_choice == "All":
                        for char in self.companions:
                            char.print_equipment()
                    else:
                        while True:
                            character_choice.print_equipment()
                            match menu(options=["Equip an item", "Unequip an item", MenuOptions.nevermind], menu_text="What would you like to do?"):
                                
                                case "Equip an item":
                                    if not equippable_items:
                                        print("No items able to be equipped!")
                                        continue
                                    item_to_equip = menu(options=list(equippable_items) + [MenuOptions.nevermind], menu_text="What item would you like to equip?", show_item_type=True)
                                    removed_item = character_choice.equip_item(item_to_equip)
                                    self.items.remove(item_to_equip)
                                    equippable_items.remove(item_to_equip)
                                    if removed_item:
                                        self.items.append(removed_item)
                                        equippable_items.append(removed_item)
                                
                                case "Unequip an item":
                                    remove_item_options = []
                                    for item_type in character_choice.equipment:
                                        if character_choice.equipment[item_type]:
                                            remove_item_options.append(character_choice.equipment[item_type])
                                    if not remove_item_options:
                                        print("No items able to be unequipped!")
                                        continue
                                    removed_item = character_choice.unequip_item(item=menu(options=list(remove_item_options) + [MenuOptions.nevermind], menu_text="What would you like to unequip?", show_item_type=True))
                                    if removed_item:
                                        self.items.append(removed_item)
                                        equippable_items.append(removed_item)
                                
                                case _:
                                    break

                case "Unequip all items":
                    match menu(menu_text="Who would you like to unequip all items", options=["All companions", "Only active party members", MenuOptions.nevermind]):
                        case "All companions":
                            for char in self.companions:
                                removed_items = char.unequip_all()
                                self.items.extend(removed_items)
                                equippable_items.extend(removed_items)
                        case "Only active party members":
                            for char in self.active_party:
                                removed_items = char.unequip_all()
                                self.items.extend(removed_items)
                                equippable_items.extend(removed_items)
                        case _:
                            pass
                
                case "Go back":
                    return

    def group_long_rest(self):
        for char in self.companions:
            char.long_rest()

    def add_custom_character(self):
        custom_character = create_custom_character()
        if custom_character:
            self.companions.append(custom_character)