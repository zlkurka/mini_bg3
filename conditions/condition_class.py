from tools.enums import BuffCondition, RollAlteration, AbilityScore, RollType
from tools.rich_capitalize import rich_capitalize
from rich import print
from random import randint

class Condition():

    def __init__(
        self, 
        name, 
        dice: dict = {},
        modifier: int = 0,
        alters_incoming_damage: bool = False, 
        alters_outgoing_damage: bool = False,
        roll_alteration: RollAlteration = None, 
        applicable_roll_types: list[RollType] = [],
        gives_advantage_on_self: bool = False,
        base_armor_class: int = None,
        maximum_dexterity_modifier_for_armor_class: int = None,
        ability_scores_added_to_armor_class: list[AbilityScore] = [],
        health_tick: int = 0, # -1 is damage, 1 is heal, 0 is none
        incapacitated: bool = False,
    ):
        self.name = name
        self.dice: dict = dice
        self.modifier: int = modifier
        self.alters_incoming_damage: bool = alters_incoming_damage
        self.alters_outgoing_damage: bool = alters_outgoing_damage
        self.roll_alteration: RollAlteration = roll_alteration
        self.applicable_roll_types: list[RollType] = applicable_roll_types
        self.gives_advantage_on_self: bool = gives_advantage_on_self
        self.base_armor_class: int = base_armor_class
        self.maximum_dexterity_modifier_for_armor_class: int = maximum_dexterity_modifier_for_armor_class
        self.ability_scores_added_to_armor_class: list[AbilityScore] = ability_scores_added_to_armor_class
        self.health_tick: int = health_tick # -1 is damage, 1 is heal, 0 is none
        self.incapacitated: bool = incapacitated
    
    def __repr__(self) -> str:
        return "[italic blue]" + str(self.name) + "[/italic blue]"

    def ticking_health_alteration(self, character) -> int:
        if not self.health_tick: 
            return 0

        health_alteration = self.modifier

        for die_type in self.dice:
            for roll in range(self.dice[die_type]):
                health_alteration += randint(1, die_type.value)

        if self.health_tick < 0:
            print(f"{rich_capitalize(character)} takes {health_alteration} damage due to {self} condition.")
            character.take_damage(health_alteration)
        if self.health_tick > 0:
            print(f"{rich_capitalize(character)} heals {health_alteration} HP due to {self} condition.")
            character.heal(health_alteration)

        return health_alteration
        
    
    def alter_incoming_damage(self, damage: int, character) -> int:
        
        if not self.alters_incoming_damage:
            return damage
        
        new_damage = 0

        # Checking conditions
        if self.name in [BuffCondition.resistant, BuffCondition.hiding]:
            new_damage = damage // 2
        elif self.name == BuffCondition.barbarian_raging:
            new_damage = round((1 - barbarian_rage_damage_reduction[character.level]) * damage)
        elif self.name == BuffCondition.undead_fortitude:
            if damage >= character.current_hp and character.ability_check(ability_type=AbilityScore.CON, difficulty_class=damage + 5):
                new_damage = character.current_hp - 1
            else:
                new_damage = damage
        else:
            print(f"Manner of damage reduction for condition {self} not found!")
        
        # Print damage change
        if new_damage < damage:
            print(f"Damage reduced from {damage} to {new_damage} due to {self} condition.")
        if new_damage > damage:
            print(f"Damage increased from {damage} to {new_damage} due to {self} condition.")
        
        return new_damage
    
    def alter_outgoing_damage(self, damage: int = 0, roll_type: RollType = None, character = None) -> int:
        
        if not self.alters_outgoing_damage:
            return damage
        
        if self.name == BuffCondition.murder_hobo_blood_rage:
            self.modifier = round((character.max_hp - character.current_hp) / 2)

        new_damage = damage + self.modifier

        if new_damage < damage:
            print(f"Damage reduced from {damage} to {new_damage} due to {self} condition.")
        if new_damage > damage:
            print(f"Damage increased from {damage} to {new_damage} due to {self} condition.")
        
        return new_damage

barbarian_rage_damage_reduction = {
    1: .3
}