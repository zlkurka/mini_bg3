from actions.action import Action
from conditions.condition import Condition, BarbarianRaging, BardicInspiration, Blessed, Hiding
from tools.enums import SpecialAction, MenuOptions, AbilityScore, Skill, Spell
from rich import print

class Buff(Action):

    def __init__(self, name, condition: Condition, targetSelf: bool = False, multi_target: int = 1, spell_slot_level: int = 0):
        self.name = name
        self.condition: Condition = condition
        self.targetSelf: bool = targetSelf
        self.spell_slot_level: int = spell_slot_level
        self.multi_target: int = multi_target
    
    def action(self, character, enemies: list, team: list, fighters: list) -> tuple:
        
        nevermindSelected = False
        
        # Expend spell slot
        if self.spell_slot_level > 0:
            if not character.cast_leveled_spell(self.spell_slot_level):
                nevermindSelected = True 
                return character, enemies, team, nevermindSelected

        # Hide action is contested by max passive perception of enemies
        elif self.name == SpecialAction.hide:
            roll = character.ability_check(ability_type=Skill.stealth)
            hide_success = True
            for char in enemies:
                enemy_passive_perception = char.ability_scores[AbilityScore.WIS] + 10
                if Skill.perception in char.skills:
                    enemy_passive_perception += char.proficiency_bonus
                if enemy_passive_perception >= roll:
                    hide_success = False
                    break
            if hide_success:
                print(f"{character} successfully hid.")
                character.conditions.append(self.condition)
            else:
                print(f"{character} tried to hide, but was spotted.")
        
        # Gives buff to self
        elif self.targetSelf: 
            character.conditions.append(self.condition)
        
        # Give buff to others, up to number of multi_target
        else:
            for iter in range(self.multi_target):
                target_options = []
                for char in team:
                    if self.condition in char.conditions:
                        continue
                    target_options.append(char)

                target = character.choose_target(target_options, self)
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
BardicInspire = Buff(
    name=SpecialAction.bardic_inspire,
    condition=BardicInspiration,
)
Bless = Buff(
    name=Spell.bless,
    condition=Blessed,
    spell_slot_level=1,
    multi_target=3
)
Hide = Buff(
    name=SpecialAction.hide, 
    condition=Hiding, 
    targetSelf=True
)