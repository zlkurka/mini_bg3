from tools.enums import MenuOptions
from actions.action_class import Action
from rich import print

class Heal(Action):
    
    def __init__(self, name: str, heal_dice: dict, heal_const: int, targetSelf: bool = False, multi_target: int = 1, spell_slot_level: int = 0, requires_concentration: bool = False, required_self_conditions: list = []):
        
        self.name = name
        self.heal_dice: dict = heal_dice
        self.heal_const: int = heal_const
        self.targetSelf: bool = targetSelf
        self.multi_target: int = multi_target
        self.spell_slot_level: int = spell_slot_level
        self.requires_concentration: bool = requires_concentration
        self.required_self_conditions: list = required_self_conditions
    
    def action(self, character, enemies: list, team: list, fighters: list, action_is_consumable: bool = False,):
        
        nevermindSelected = False

        # Expend spell slot
        if self.spell_slot_level > 0 and not action_is_consumable:
            if not character.cast_leveled_spell(self.spell_slot_level):
                nevermindSelected = True 
                return character, enemies, team, nevermindSelected
        
        # Choosing target
        if self.targetSelf:
            target = character
            chosen_targets = [character]

            heal_amount = self.roll_dice(self.heal_dice)
            print(f"{character.name} healed self for {heal_amount} HP.")
            target.heal(heal_amount)
        else:
            chosen_targets = []
            for iter in range(self.multi_target):
                target = character.choose_target(team, self)
                if target == MenuOptions.nevermind:
                    nevermindSelected = True
                    if self.spell_slot_level:
                        character.spell_slots[self.spell_slot_level] += 1
                    return character, enemies, team, nevermindSelected
                
                chosen_targets.append(target)
                heal_amount = self.roll_dice(self.heal_dice)
                print(f"{character.name} healed {target} for {heal_amount} HP.")
                target.heal(heal_amount)

        return character, enemies, team, nevermindSelected, chosen_targets