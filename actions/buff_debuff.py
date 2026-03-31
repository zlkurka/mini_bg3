from actions.action import Action
from conditions.condition import Condition, BarbarianRaging
from tools.enums import SpecialAction, MenuOptions

class Buff(Action):

    def __init__(self, name, condition: Condition, targetSelf: bool = False, spell_slot_level: int = 0):
        self.name = name
        self.condition: Condition = condition
        self.targetSelf: bool = targetSelf
        self.spell_slot_level: int = spell_slot_level
    
    def action(self, character, enemies: list, team: list, fighters: list) -> tuple:
        
        nevermindSelected = False

        if self.targetSelf: 
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