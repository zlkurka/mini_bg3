from actions.action import Action
from conditions.condition import Condition, BarbarianRaging, Hiding
from tools.enums import SpecialAction, MenuOptions, AbilityScore
from rich import print

class Buff(Action):

    def __init__(self, name, condition: Condition, targetSelf: bool = False, spell_slot_level: int = 0):
        self.name = name
        self.condition: Condition = condition
        self.targetSelf: bool = targetSelf
        self.spell_slot_level: int = spell_slot_level
    
    def action(self, character, enemies: list, team: list, fighters: list) -> tuple:
        
        nevermindSelected = False
        
        # Hide action is contested by max passive perception of enemies
        if self.name == SpecialAction.hide:
            roll = character.ability_check(ability_type=AbilityScore.DEX)
            hide_success = True
            for char in enemies:
                if char.ability_scores[AbilityScore.WIS] + 10 >= roll:
                    hide_success = False
                    break
            if hide_success:
                print(f"{character} successfully hid.")
                character.conditions.append(self.condition)
            else:
                print(f"{character} tried to hide, but was spotted.")
        
        elif self.targetSelf: 
            character.conditions.append(self.condition)
        
        else:
            target = character.choose_target(team, self)
            if target == MenuOptions.nevermind:
                nevermindSelected = True
                return character, enemies, team, nevermindSelected
            
            target.conditions.append(self.condition)
            
            target_index = team.index(target)
            team.pop(target_index)
            team.insert(target_index, target)

        return character, enemies, team, nevermindSelected

BarbarianRage = Buff(
    name=SpecialAction.barbarian_rage, 
    condition=BarbarianRaging, 
    targetSelf=True
)
Hide = Buff(
    name=SpecialAction.hide, 
    condition=Hiding, 
    targetSelf=True
)