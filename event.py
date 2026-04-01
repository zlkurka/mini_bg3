from tools.enums import AbilityScore
from tools.menu import menu
from actions.attacks import Longsword
from actions.action import PassAction
from rich import print
from characters.character import Character

class Event():

    def __init__(self, name, description: str, options: list[EventOption]):
        self.name = name
        self.description: str = description
        self.options: list = options
    
    def __repr__(self):
        return "[bold]" + str(self.name) + "[/bold]"

    def begin(self, party: list):
        print(str(self) + "\n\n" + self.description + "\n")
        choice = menu(menu_text="What will you do?", options=self.options)
        
        if len(party) > 1:
            character_making_check = menu(menu_text="Who is up to the task?",options=party)
        else:
            character_making_check = party[0]
        
        checkSuccessful = character_making_check.ability_check(ability_type=choice.ability_check, difficulty_class=choice.difficulty_class)
        if not checkSuccessful:
            print(choice.failure_text.format(character_making_check))
        else:
            print(choice.success_text.format(character_making_check))

            for item in choice.rewards:
                if type(item) == Character:
                    party.append(Character)


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

SwordInStone = Event(
    name = "The Sword in the Stone",
    description = "You find a longsword stuck firmly in a rock. You notice some runes carved into the stone.",
    options = [
        EventOption(
            name = "Pull out the sword",
            ability_check = AbilityScore.STR,
            difficulty_class = 15,
            rewards = [Longsword],
            success_text = "{} wrenches the sword from the stone. It gleams in your faint torchlight.",
            failure_text = "{} pulls at the sword with all their might, but it won't budge.",
        ),
        EventOption(
            name = "Examine the runes etched into the rock",
            ability_check = AbilityScore.INT,
            difficulty_class = 15,
            rewards = [PassAction],
            success_text = "{} studies the runes and recognizes them as the incantation for a powerful spell.",
            failure_text = "{} examines the runes, but is unable to decipher them.",
        ),
    ],
)

if __name__ == "__main__":
    from characters.companions import Karlach, Gale
    SwordInStone.begin([Karlach, Gale])