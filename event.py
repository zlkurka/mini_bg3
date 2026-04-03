from rich import print
from characters.character import Character
from actions.attacks import Attack, Longsword_plus1
from actions.action import Action, PassAction
from tools.enums import AbilityScore, Skill
from tools.menu import menu
from tools.defaults import empty_spell_slots
from tools.rich_capitalize import rich_capitalize

class Event():

    def __init__(self, name, description: str, options: list):
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
                if type(item) == Action or Attack:
                    
                    if item.spell_slot_level > 0:
                        recipient_options = []
                        for char in party:
                            if char.spell_slots != empty_spell_slots:
                                recipient_options.append(char)
                    else:
                        recipient_options = party
                    choice = menu(menu_text="Who should recieve this?", options=recipient_options)
                    choice.actions.append(item)
                    print(f"{rich_capitalize(item)} added to {choice}'s actions.")
                    continue
                if type(item) == Character:
                    party.append(Character)
                    continue

        return party


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
    description = "In the center of this room, you see a longsword with its blade stuck into a stone pedestal.\n" \
    "As you investigate, you notice some runes carved around the top of the pedestal.",
    options = [
        EventOption(
            name = "Pull out the sword",
            ability_check = AbilityScore.STR,
            difficulty_class = 15,
            rewards = [Longsword_plus1],
            success_text = "{} wrenches the sword from the stone. It gleams in your faint torchlight.",
            failure_text = "{} pulls at the sword with all their might, but it won't budge.",
        ),
        EventOption(
            name = "Examine the runes etched into the rock",
            ability_check = Skill.arcana,
            difficulty_class = 15,
            rewards = [PassAction],
                # I think this should be a control spell, which would make this decision more meaningful- big damage or control?
            success_text = "{} studies the runes and recognizes them as the incantation for a powerful spell.",
            failure_text = "{} examines the runes, but is unable to decipher them.",
        ),
    ],
)
# Mimic event:
# - Open the chest or whatever it is
# - Take something small and ignore the chest
# Other idea
# - Look into a chest, pick one of several items, but a random one of them is a mimic and leads to a fight
#   - Could also have an item that is a mimic and hurts you

# Gelatinous cube event

# Talk with a beholder?

# Door puzzle


if __name__ == "__main__":
    from characters.companions import Brains, Brawn
    SwordInStone.begin([Brawn, Brains])