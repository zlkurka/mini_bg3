from actions.action import Action
from tools.menu import menu
from tools.enums import SummonType, MenuOptions
from copy import deepcopy
from rich import print

class Summon(Action):

    def __init__(self, spell_slot_level: int = 0, summon_type: SummonType = SummonType.familiar, creatureCanAttack: bool = True):
        self.spell_slot_level: int = spell_slot_level
        self.summon_type: SummonType = summon_type
        self.creatureCanAttack: bool = creatureCanAttack
    
    def action(self, character, enemies: list, team: list, fighters: list):
        
        nevermindSelected = False

        # Expend spell slot
        if self.spell_slot_level > 0:
            if not character.cast_leveled_spell(self.spell_slot_level):
                nevermindSelected = True 
                return character, enemies, team, nevermindSelected

        selected_creature = deepcopy(menu([], "What creature would you like to summon?"))

        team.append(selected_creature)
        fighters.insert(fighters.index(character) + 1, selected_creature)

        return character, enemies, team, nevermindSelected

FindFamiliar = Summon(
    spell_slot_level=1,
    summon_type=SummonType.familiar,
    creatureCanAttack=True,
)