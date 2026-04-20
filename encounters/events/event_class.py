from rich import print
from encounters.combat.combats import *
from tools.menu import menu
from tools.defaults import empty_spell_slots
from tools.rich_capitalize import rich_capitalize

class Event():

    def __init__(self, name, description: str = "", options: list = [], rewards: list = []):
        self.name = name
        self.description: str = description
        self.options: list = options
        self.rewards: list = rewards
    
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

        choice=menu(menu_text="What will you do?", options=options, show_ability_check_and_difficulty_class=True)
        contest_successful = True

        ## Checks ##

        # If ability check, do ability check
        character_making_check = None
        if choice.ability_check:
            if len(party) > 1:
                character_making_check = menu(menu_text="Who is up to the task?",options=party)
            else:
                character_making_check = party[0]
        
            if menu(menu_text="Would a character like to use a buff?", options=["Yes", "No"]) == "Yes":
                while True:
                    character_using_buff = menu(menu_text="Who wants to use a buff?", options=list(party + ["All done"]))
                    if character_using_buff == "All done":
                        break
                    character_using_buff.action(team=party, enemies=[], fighters=party)
            contest_successful = character_making_check.ability_check(ability_type=choice.ability_check, difficulty_class=choice.difficulty_class)
        
        # If not abiity check, do voluntary combat
        elif choice.combat:
            self.rewards.extend(choice.combat.begin(party=party))
            if len(party) == 0:
                # This is game over
                contest_successful = False
        

        ## Results ##

        # If succeeded abilility check or voluntary combat
        if contest_successful:

            print(choice.success_text.format(character_making_check))
            self.rewards.extend(choice.rewards)
            if choice.options:
                self.do_option(options=choice.options, party=party)
        
        # If failed abilility check or voluntary combat
        else: 
            print(choice.failure_text.format(character_making_check))
            
            # If involuntary combat on failure
            if choice.combat_on_failure and choice.combat:
                self.rewards.extend(choice.combat.begin(party=party))
                
                # If lost combat (game over)
                if len(party) == 0:
                    print(choice.combat_failure_text)
                # If succeeded combat
                else:
                    print(choice.combat_success_text)
        
        return


class EventOption():

    def __init__(
            self, 
            name, 
            success_text: str = "", 
            failure_text: str = "", 
            options: list = [],
            rewards: list = [], 
            unconditional_rewards: list = [],
            ability_check = None, 
            difficulty_class: int = 0, 
            combat = None, 
            combat_on_failure: bool = False,
            combat_success_text: str = "",
            combat_failure_text: str = "",
        ):
        self.name = name
        self.success_text: str = success_text
        self.failure_text: str = failure_text
        self.options: list = options
        self.rewards: list = rewards
        self.unconditional_rewards: list = unconditional_rewards
        self.ability_check = ability_check
        self.difficulty_class: int = difficulty_class
        self.combat = combat
        self.combat_on_failure: bool = combat_on_failure
        self.combat_success_text: str = combat_success_text
        self.combat_failure_text: str = combat_failure_text
    
    def __repr__(self):
        return str(self.name)