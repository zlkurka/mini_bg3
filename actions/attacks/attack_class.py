from actions.action_class import Action
from conditions.positive_conditions import Hiding
from tools.enums import AbilityScore, Weapon, MenuOptions, RollType
from tools.rich_capitalize import rich_capitalize
from tools.roll_d20 import roll_d20
from rich import print

class Attack(Action):
    
    def __init__(
        self, 
        name, 
        damage_dice: dict, 
        ability_score_modifier: AbilityScore, 
        multi_target: int = 1, 
        ranged: bool = False, 
        area_of_effect: bool = False, 
        savingThrow_abilityScore: AbilityScore = None, 
        halfDamage_onSave: bool = False, 
        use_damage_modifier: bool = True, 
        spell_slot_level: int = 0,
        requires_concentration: bool = False,
        weapon_bonus: int = 0,
        required_self_conditions: list = []
    ):
        
        self.name = name
        self.damage_dice: dict = damage_dice
        self.ability_score_modifier: AbilityScore = ability_score_modifier
        self.ranged: bool = ranged
        self.use_damage_modifier: bool = use_damage_modifier
        self.spell_slot_level: int = spell_slot_level
        self.requires_concentration: bool = requires_concentration
        self.savingThrow_abilityScore: AbilityScore = savingThrow_abilityScore
        self.weapon_bonus: int = weapon_bonus
        self.required_self_conditions: list = required_self_conditions

        if area_of_effect == True:
            self.area_of_effect: bool = True
            self.multi_target: int = 0
            self.halfDamage_onSave: bool = halfDamage_onSave
        else: 
            self.area_of_effect: bool = False
            self.multi_target: int = multi_target
            self.halfDamage_onSave: bool = False

    def __repr__(self):
        if self.weapon_bonus:
            return "[italic purple]" + str(self.name) + f", +{self.weapon_bonus}" + "[/italic purple]"
        return "[italic purple]" + str(self.name) + "[/italic purple]"

    def action(self, character, enemies: list, team: list, fighters: list, action_is_consumable: bool = False,):
        
        nevermindSelected = False 

        # Expend spell slot
        if self.spell_slot_level > 0 and not action_is_consumable:
            if not character.cast_leveled_spell(self.spell_slot_level):
                nevermindSelected = True 
                return character, enemies, team, nevermindSelected

        # Action with required self condition
        for cond in self.required_self_conditions:
            if cond not in character.conditions:
                nevermindSelected = True 
                return character, enemies, team, nevermindSelected
        
        chosen_targets = []

        # Area of effect
        if self.area_of_effect:
            for target in list(enemies):
                chosen_targets.append(target)
                if self.check_if_hit(character, target):
                    target, enemies = self.deal_damage(character=character, target=target, enemies=enemies, halved_damage=False)
                else:
                    if self.halfDamage_onSave:
                        target, enemies = self.deal_damage(character=character, target=target, enemies=enemies, halved_damage=True)

        # Individual-target
        for iter in range(self.multi_target):
            if not enemies:
                break
            while True:
                
                target = character.choose_target(targets=enemies, action=self)
                if not target:
                    break
                if target == MenuOptions.nevermind:
                    nevermindSelected = True
                    return character, enemies, team, nevermindSelected
                
                chosen_targets.append(target)
                if target.current_hp <= 0:
                    continue
                if self.check_if_hit(character, target):
                    target, enemies = self.deal_damage(character=character, target=target, enemies=enemies, halved_damage=False)
                break

        # Update lastAttack_isMelee
        if self.ranged:
            character.lastAttack_isMelee = False
        else: 
            character.lastAttack_isMelee = True

        # Return
        return character, enemies, team, nevermindSelected, chosen_targets
    
    def check_if_hit(self, character, target):
        
        attack_modifier: int = character.get_modifier(ability_type=self.ability_score_modifier) + self.weapon_bonus
        
        if self.savingThrow_abilityScore:
            hitSuccessful = roll_d20(character=target, roll_bonus=target.ability_scores[self.savingThrow_abilityScore], roll_type=RollType.attack) <= attack_modifier + 8 # change if I add proficiency bonuses
        else:
            hitSuccessful =  roll_d20(character=character, roll_bonus=attack_modifier, roll_type=RollType.attack) >= target.armor_class
        
        if not hitSuccessful and not self.halfDamage_onSave:
            print(f"{rich_capitalize(character)} misses {target} with {self.name}.")
        return hitSuccessful
    
    def deal_damage(self, character, target, enemies, halved_damage: bool):
        damage = self.roll_dice(self.damage_dice)

        for cond in character.conditions:
            damage = cond.alter_outgoing_damage(damage=damage, roll_type=RollType.attack, character=character)

        if self.use_damage_modifier:
            damage += character.get_modifier(self.ability_score_modifier, exclude_proficiency_bonus=True) + self.weapon_bonus
        
        if halved_damage:
            damage = damage // 2
            print(f"{rich_capitalize(target)} resists {character}'s {self.name}, but they still take {damage} damage!")
        else: 
            print(f"{rich_capitalize(character)} hits {target} with {self.name} for {damage} damage!")
        target.take_damage(damage)

        if target.current_hp <= 0:
            enemies.remove(target)
        else:
            enemies[enemies.index(target)] = target

        return target, enemies
    