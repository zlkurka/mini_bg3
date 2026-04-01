from tools.enums import BuffCondition
from rich import print

class Condition():

    def __init__(self, name, reduces_damage: bool = False, gives_advantage: bool = False):
        self.name = name
        self.reduces_damage: bool = reduces_damage
        self.gives_advantage: bool = gives_advantage
    
    def __repr__(self) -> str:
        return "[italic blue]" + str(self.name) + "[/italic blue]"

    def reduce_damage(self, damage: int, character) -> int:
        
        if not self.reduces_damage:
            return 0
        
        # Checking conditions
        if self.name == BuffCondition.barbarian_raging:
            new_damage = round((1 - barbarian_rage_damage_reduction[character.level]) * damage)
        elif self.name == BuffCondition.resistant or BuffCondition.hiding:
            new_damage = damage // 2
        
        if new_damage < damage:
            print(f"Damage reduced from {damage} to {new_damage} due to {self} condition.")
        if new_damage > damage:
            print(f"Damage increased from {damage} to {new_damage} due to {self} condition.")
        return new_damage

# Damage reduction
Resistant = Condition(
    name=BuffCondition.resistant,
    reduces_damage=True,
)
BarbarianRaging = Condition(name=BuffCondition.barbarian_raging)
Hiding = Condition(name=BuffCondition.hiding)

barbarian_rage_damage_reduction = {
    1: .3
}

conditions_removed_at_turn_start = []
conditions_removed_at_turn_end = []