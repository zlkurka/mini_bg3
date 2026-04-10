from tools.enums import BuffCondition, RollAlteration, AbilityScore, RollType
from rich import print

class Condition():

    def __init__(
        self, 
        name, 
        dice: dict = {},
        modifier: int = 0,
        alters_incoming_damage: bool = False, 
        alters_outgoing_damage: bool = False,
        roll_alteration: RollAlteration = None, 
        applicable_roll_type: RollType = None, # Add shit for making hide only apply to attacks and stuff
        gives_advantage_on_self: bool = False,
    ):
        self.name = name
        self.dice: dict = dice
        self.modifier: int = modifier
        self.alters_incoming_damage: bool = alters_incoming_damage
        self.alters_outgoing_damage: bool = alters_outgoing_damage
        self.roll_alteration: bool = roll_alteration
        self.applicable_roll_type: RollType = applicable_roll_type
        self.gives_advantage_on_self: bool = gives_advantage_on_self
    
    def __repr__(self) -> str:
        return "[italic blue]" + str(self.name) + "[/italic blue]"

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
        
        if roll_type == self.applicable_roll_type:
            new_damage = damage + self.modifier

        if new_damage < damage:
            print(f"Damage reduced from {damage} to {new_damage} due to {self} condition.")
        if new_damage > damage:
            print(f"Damage increased from {damage} to {new_damage} due to {self} condition.")
        
        return new_damage

barbarian_rage_damage_reduction = {
    1: .3
}