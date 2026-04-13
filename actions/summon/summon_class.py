from actions.action_class import Action
from actions.summon.summon_lists import summon_types
from tools.menu import menu
from tools.enums import SummonType
from copy import deepcopy
from rich import print

class Summon(Action):

    def __init__(self, name = "", spell_slot_level: int = 0, summon_type: SummonType = SummonType.familiar, creatureCanAttack: bool = True, required_self_conditions: list = []):
        self.name = name
        self.spell_slot_level: int = spell_slot_level
        self.summonable_creatures: list = summon_types[summon_type]
        self.creatureCanAttack: bool = creatureCanAttack
        self.required_self_conditions: list = required_self_conditions
    
    def action(self, character, enemies: list, team: list, fighters: list):
        
        nevermindSelected = False

        # Expend spell slot
        if self.spell_slot_level > 0:
            if not character.cast_leveled_spell(self.spell_slot_level):
                nevermindSelected = True 
                return character, enemies, team, nevermindSelected

        selected_creature = deepcopy(menu(self.summonable_creatures, "What creature would you like to summon?"))

        selected_creature.character_type = character.character_type
        team.append(selected_creature)
        fighters.insert(fighters.index(character) + 1, selected_creature)

        return character, enemies, team, nevermindSelected