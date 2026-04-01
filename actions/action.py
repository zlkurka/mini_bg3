from tools.enums import Dice, AbilityScore
from random import randint
from rich import print

class Action():

    def __init__(self, name, dice: dict, modifier: AbilityScore, multi_target: int = 1, spell_slot_level: int = 0):
        self.name = name
        self.damage_dice: dict = dice
        self.modifier: AbilityScore = modifier
        self.multi_target: int = multi_target
        self.spell_slot_level: int = spell_slot_level

    def __repr__(self):
        return "[italic purple]" + str(self.name) + "[/italic purple]"

    def action(self, character, enemies: list, team: list, fighters: list):
        nevermindSelected = False
        return character, enemies, team, nevermindSelected
    
    def roll_dice(self, dice: dict):
        
        output = 0
        
        for die_type in dice:
            for roll in range(dice[die_type]):
                output += randint(1, die_type.value)
        
        return output
    
    def get_modifier(self, ability_type: AbilityScore, character):
        
        if ability_type == AbilityScore.finesse:
            return max(
                character.ability_scores[AbilityScore.STR], 
                character.ability_scores[AbilityScore.DEX]
            )
        elif ability_type == AbilityScore.spellcasting:
            return max(
                character.ability_scores[AbilityScore.INT], 
                character.ability_scores[AbilityScore.WIS], 
                character.ability_scores[AbilityScore.CHA]
            )
        else:
            return character.proficiency_bonus + character.ability_scores[ability_type]

PassAction = Action(
    name='Pass action', 
    dice={Dice.d4: 0}, 
    modifier=0, 
    multi_target=0,
)