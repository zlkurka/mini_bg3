from tools.menu import menu
from tools.enums import Dice, AbilityScore, Spell
from random import randint

class Action():

    def __init__(self, name, dice, modifier, multi_target):
        self.name = name
        self.damage_dice: dict = dice
        self.modifier: AbilityScore = modifier
        self.multi_target: int = multi_target

    def __repr__(self):
        try:
            return self.name.value
        except AttributeError:
            return self.name

    def action(self, character, enemies=list, team=list):
        return character, enemies, team
    
    def roll_dice(self, dice):
        
        output = 0
        
        for die_type in dice:
            for roll in range(dice[die_type]):
                output += randint(1, die_type.value)
        
        return output
    
    def get_modifier(self, ability_type, character):
        
        if ability_type == AbilityScore.finesse:
            return max(
                character.ability_scores[AbilityScore.STR], 
                character.ability_scores[AbilityScore.DEX]
            )
        elif ability_type == AbilityScore.spellcasting:
            return max(
                character.ability_scores[AbilityScore.INT], 
                character.ability_scores[AbilityScore.WIS], 
                character.ability_scores[AbilityScore.CHA]
            )
        else:
            return character.proficiency_bonus + character.ability_scores[ability_type]

PassAction = Action(
    name='Pass action', 
    dice={Dice.d4: 0}, 
    modifier=0, 
    multi_target=0,
)

class Heal(Action):
    
    def __init__(self, name=str, heal_dice=dict, heal_const=int, can_choose_target=bool, target_count=int, spell_slot_level=int, isConsumable=bool):
        
        self.name = name

        self.heal_dice: dict = heal_dice
        self.heal_const: int = heal_const

        self.can_choose_target: bool = can_choose_target
        self.target_count: int = target_count

        if spell_slot_level:
            self.spell_slot_level: int = spell_slot_level
        else: 
            self.spell_slot_level: int = 0

        if isConsumable:
            self.isConsumable: bool = isConsumable
        else: 
            self.isConsumable: bool = False
    
    def action(self, character, enemies=list, team=list):
        
        if self.spell_slot_level > 0:
            if not character.cast_leveled_spell(self.spell_slot_level):
                return character, enemies, team

        if self.can_choose_target:
            target = menu(team, f"Who would {character.name} like to heal?", show_race=False, show_class=False, show_hp=True)
            heal_amount = self.roll_dice(self.heal_dice) + self.heal_const
            
            print(f"{character.name} healed {target.name} for {heal_amount} HP.")
            target.heal(heal_amount)

            team[team.index(target)] = target
        
        else:   
            target = character
            heal_amount = self.roll_dice(self.heal_dice)
            target.heal(heal_amount)

            print(f"{character.name} healed self for {heal_amount} HP.")

        return character, enemies, team

CureWounds = Heal(
    name = Spell.cure_wounds,
    heal_dice = {Dice.d6: 1},
    heal_const = 1,
    can_choose_target = True,
    target_count = 1,
    spell_slot_level=1
)