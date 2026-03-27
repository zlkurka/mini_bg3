from actions.action import Action
from tools.enums import Buff

class Condition():

    def __init__(self, name):
        self.name = name

    def reduce_damage(self, damage):
        
        if self.name == Buff.resistant:
            print(f"Damage halved from {damage} to {damage // 2} due to {self.name} condition.")
            return damage // 2
        
        return damage

Resistant = Condition(name=Buff.resistant)