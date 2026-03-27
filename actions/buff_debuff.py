from actions.action import Action
from conditions.condition import Condition, Resistant
from tools.enums import Buff, SpecialAction

class Buff(Action):

    def __init__(self, name, condition=Condition, targetSelf=bool, spell_slot_level=int):
        self.name = name
        self.condition: Condition = condition
        self.targetSelf: bool = targetSelf

        if spell_slot_level != int:
            self.spell_slot_level: int = spell_slot_level
        else:
            self.spell_slot_level: int = 0
    
    def action(self, character, enemies=list, team=list, fighters=list):
        character.conditions.append(self.condition)
        return character, enemies, team

Rage = Buff(SpecialAction.barbarian_rage, condition=Resistant, targetSelf=True)