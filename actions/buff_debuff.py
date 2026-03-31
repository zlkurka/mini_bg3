from actions.action import Action
from conditions.condition import Condition, BarbarianRaging
from tools.enums import SpecialAction

class Buff(Action):

    def __init__(self, name, condition: Condition, targetSelf: bool = False, spell_slot_level: int = 0):
        self.name = name
        self.condition: Condition = condition
        self.targetSelf: bool = targetSelf
        self.spell_slot_level: int = spell_slot_level
    
    def action(self, character, enemies=list, team=list, fighters=list):
        character.conditions.append(self.condition)
        return character, enemies, team

BarbarianRage = Buff(
    name=SpecialAction.barbarian_rage, 
    condition=BarbarianRaging, 
    targetSelf=True
)