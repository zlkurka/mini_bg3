from tools.enums import MenuOptions
from actions.action_class import Action
from rich import print

class Heal(Action):
    
    def __init__(self, name: str, heal_dice: dict, heal_const: int, can_choose_target: bool, target_count: int = 1, spell_slot_level: int = 0):
        
        self.name = name
        self.heal_dice: dict = heal_dice
        self.heal_const: int = heal_const
        self.can_choose_target: bool = can_choose_target
        self.target_count: int = target_count
        self.spell_slot_level: int = spell_slot_level
    
    def action(self, character, enemies: list, team: list, fighters: list):
        
        nevermindSelected = False

        # Expend spell slot
        if self.spell_slot_level > 0:
            if not character.cast_leveled_spell(self.spell_slot_level):
                nevermindSelected = True 
                return character, enemies, team, nevermindSelected

        if self.can_choose_target:
            
            target = character.choose_target(team, self)
            if target == MenuOptions.nevermind:
                nevermindSelected = True
                if self.spell_slot_level:
                    character.spell_slots[self.spell_slot_level] += 1
                return character, enemies, team, nevermindSelected
                
            heal_amount = self.roll_dice(self.heal_dice) + self.heal_const
            
            print(f"{character.name} healed {target.name} for {heal_amount} HP.")
            target.heal(heal_amount)

            team[team.index(target)] = target
        
        else:   
            target = character
            heal_amount = self.roll_dice(self.heal_dice)
            target.heal(heal_amount)

            print(f"{character.name} healed self for {heal_amount} HP.")

        return character, enemies, team, nevermindSelected