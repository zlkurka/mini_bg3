from actions.action import Action
from tools.menu import menu
from tools.enums import SummonType
from copy import deepcopy
from rich import print

class Summon(Action):

    def __init__(self, spell_slot_level=int, summon_type=SummonType, creatureCanAttack=bool):
        
        if spell_slot_level != int:
            self.spell_slot_level = spell_slot_level
        else:
            self.spell_slot_level = 0

        self.summon_type: SummonType = summon_type
        if creatureCanAttack != bool:
            self.creatureCanAttack = creatureCanAttack
        else:
            self.creatureCanAttack = True
    
    def action(self, character, enemies=list, team=list, fighters=list):
        
        selected_creature = deepcopy(menu([], "What creature would you like to summon?"))

        team.append(selected_creature)
        fighters.insert(fighters.index(character) + 1, selected_creature)

        return character, enemies, team

FindFamiliar = Summon(
    summon_type=SummonType.familiar,
    creatureCanAttack=True,
)