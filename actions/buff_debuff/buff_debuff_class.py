from actions.action_class import Action
from conditions.condition_class import Condition
from conditions.positive_conditions import *
from tools.enums import SpecialAction, MenuOptions, AbilityScore, Skill, Spell
from tools.rich_capitalize import rich_capitalize
from rich import print

class Buff(Action):

    def __init__(self, name, condition: Condition, targetSelf: bool = False, multi_target: int = 1, spell_slot_level: int = 0, requires_concentration: bool = False, required_self_conditions: list = []):
        self.name = name
        self.condition: Condition = condition
        self.targetSelf: bool = targetSelf
        self.spell_slot_level: int = spell_slot_level
        self.requires_concentration: bool = requires_concentration
        self.multi_target: int = multi_target
        self.required_self_conditions: list = required_self_conditions
    
    def action(self, character, enemies: list, team: list, fighters: list, action_is_consumable: bool = False,) -> tuple:
        
        nevermindSelected = False
        
        # Expend spell slot
        if self.spell_slot_level > 0  and not action_is_consumable:
            if not character.cast_leveled_spell(self.spell_slot_level):
                nevermindSelected = True 
                return character, enemies, team, nevermindSelected

        # Hide action is contested by max passive perception of enemies
        if self.name == SpecialAction.hide:
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
            else:
                print(f"{character} tried to hide, but was spotted.")
                return character, enemies, team, nevermindSelected

        # Gives buff to self
        if self.targetSelf: 
            character.gain_condition(self.condition)
            chosen_targets = [character]
        
        # Give buff to others, up to number of multi_target
        else:
            target_options = []
            chosen_targets = []
            for char in team:
                if self.condition in char.conditions:
                    continue
                target_options.append(char)
            for iter in range(self.multi_target):

                target = character.choose_target(target_options, self)
                if target == MenuOptions.nevermind:
                    nevermindSelected = True
                    return character, enemies, team, nevermindSelected
                
                if not target:
                    break
                
                target.gain_condition(self.condition)
                target_options.remove(target)
                if target:
                    chosen_targets.append(target)
                
                if None not in target_options:
                    target_options.append(None)
                
        return character, enemies, team, nevermindSelected, chosen_targets