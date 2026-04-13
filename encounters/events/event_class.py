from rich import print
from tools.menu import menu
from tools.defaults import empty_spell_slots
from tools.rich_capitalize import rich_capitalize

class Event():

    def __init__(self, name, description: str = "", options: list = []):
        self.name = name
        self.description: str = description
        self.options: list = options
    
    def __repr__(self):
        return "[bold]" + str(self.name) + "[/bold]"

    def begin(self, party: list):
        print(str(self))
        if self.description:
            print("\n\n" + self.description + "\n")

        choice = menu(menu_text="What will you do?", options=self.options)
        
        if len(party) > 1:
            character_making_check = menu(menu_text="Who is up to the task?",options=party)
        else:
            character_making_check = party[0]
        
        checkSuccessful = character_making_check.ability_check(ability_type=choice.ability_check, difficulty_class=choice.difficulty_class)
        if not checkSuccessful:
            print(choice.failure_text.format(character_making_check))
            loot = []
        else:
            print(choice.success_text.format(character_making_check))
            loot = choice.rewards

        return loot


class EventOption():

    def __init__(self, name, ability_check, difficulty_class: int, rewards: list, success_text: str, failure_text: str,):
        self.name = name
        self.ability_check = ability_check
        self.difficulty_class: int = difficulty_class
        self.rewards: list = rewards
        self.success_text: str = success_text
        self.failure_text: str = failure_text
    
    def __repr__(self):
        return str(self.name)