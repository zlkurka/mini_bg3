from tools.enums import BuffCondition
from rich import print

class Condition():

    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return "[italic blue]" + str(self.name) + "[/italic blue]"

    def reduce_damage(self, damage: int, character) -> int:
        
        if self.name == BuffCondition.barbarian_raging:
            new_damage = round((1 - barbarian_rage_damage_reduction[character.level]) * damage)
        elif self.name == BuffCondition.resistant:
            new_damage = damage // 2
        
        if new_damage < damage:
            print(f"Damage reduced from {damage} to {new_damage} due to {self} condition.")
        if new_damage > damage:
            print(f"Damage increased from {damage} to {new_damage} due to {self} condition.")
        return new_damage

Resistant = Condition(name=BuffCondition.resistant)
BarbarianRaging = Condition(name=BuffCondition.barbarian_raging)

barbarian_rage_damage_reduction = {
    1: .3
}