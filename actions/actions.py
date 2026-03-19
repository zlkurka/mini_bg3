from tools.enums import Dice, AbilityScore
from random import randint

class Action():

    def __init__(self, name, dice, modifier, multi_target):
        self.name = name
        self.damage_dice: dict = dice
        self.modifier: AbilityScore = modifier
        self.multi_target: int = multi_target

    def __repr__(self):
        return str(self.name)

    def action(self, character, enemies=list, team=list, fighters=list):
        return character, enemies, team
    
    def roll_dice(self, dice):
        
        output = 0
        
        for die_type in dice:
            for roll in range(dice[die_type]):
                output += randint(1, die_type.value)
        
        return output
    
    def get_modifier(self, ability_type, character):
        
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