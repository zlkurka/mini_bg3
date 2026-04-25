from tools.enums import Dice, AbilityScore, CharClass
from random import randint
from rich import print

class Action():

    def __init__(self, name, dice: dict = {}, modifier: AbilityScore = None, multi_target: int = 1, spell_slot_level: int = 0, requires_concentration: bool = False):
        self.name = name
        self.damage_dice: dict = dice
        self.modifier: AbilityScore = modifier
        self.multi_target: int = multi_target
        self.spell_slot_level: int = spell_slot_level
        self.requires_concentration: bool = requires_concentration

    def __repr__(self):
        return "[italic purple]" + str(self.name) + "[/italic purple]"

    def action(self, character, enemies: list, team: list, fighters: list, action_is_consumable: bool = False):
        nevermindSelected = False
        chosen_targets = []
        return character, enemies, team, nevermindSelected, chosen_targets
    
    def roll_dice(self, dice: dict):
        
        output = 0
        
        for die_type in dice:
            for roll in range(dice[die_type]):
                output += randint(1, die_type.value)
        
        return output

PassAction = Action(
    name='pass action', 
    multi_target=0
)
BreakConcentration = Action(
    name='break concentration',
    multi_target=0,
    requires_concentration=True,
)