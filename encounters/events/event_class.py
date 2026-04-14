from rich import print
from encounters.combat.combats import *
from tools.menu import menu
from tools.defaults import empty_spell_slots
from tools.rich_capitalize import rich_capitalize

class Event():

    def __init__(self, name, description: str = "", options: list = []):
        self.name = name
        self.description: str = description
        self.options: list = options
        self.rewards: list = []
    
    def __repr__(self):
        return "[bold]" + str(self.name) + "[/bold]"

    def begin(self, party: list):

        print(str(self))
        if self.description:
            print("\n\n" + self.description + "\n")

        self.do_option(options=self.options, party=party)

        print()
        return self.rewards
    
    def do_option(self, options: list, party: list):

        choice=menu(menu_text="What will you do?", options=options)
        contest_successful = True

        character_making_check = None
        if choice.ability_check:
            if len(party) > 1:
                character_making_check = menu(menu_text="Who is up to the task?",options=party)
            else:
                character_making_check = party[0]
        
            contest_successful = character_making_check.ability_check(ability_type=choice.ability_check, difficulty_class=choice.difficulty_class)
        
        if choice.combat:
            self.rewards.extend(choice.combat.begin(party=party))
            if len(party) == 0:
                contest_successful = False
        
        if not contest_successful:
            print(choice.failure_text.format(character_making_check))
        else:
            print(choice.success_text.format(character_making_check))
            self.rewards.extend(choice.rewards)
            if choice.options:
                self.do_option(options=choice.options, party=party)
        
        return


class EventOption():

    def __init__(self, name, options: list = [], ability_check = None, difficulty_class: int = 0, combat = None, rewards: list = [], success_text: str = "", failure_text: str = "",):
        self.name = name
        self.options: list = options
        self.ability_check = ability_check
        self.difficulty_class: int = difficulty_class
        self.combat = combat
        self.rewards: list = rewards
        self.success_text: str = success_text
        self.failure_text: str = failure_text
    
    def __repr__(self):
        return str(self.name)