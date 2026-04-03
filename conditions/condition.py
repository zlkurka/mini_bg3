from tools.enums import BuffCondition, Dice, RollAlteration, AbilityScore
from rich import print

class Condition():

    def __init__(
        self, 
        name, 
        dice: dict = {},
        modifier: int = 0,
        reduces_damage: bool = False, 
        roll_alteration: RollAlteration = None, 
        gives_advantage_on_self: bool = False,
    ):
        self.name = name
        self.dice: dict = dice
        self.modifier: int = modifier
        self.reduces_damage: bool = reduces_damage
        self.roll_alteration: bool = roll_alteration
        self.gives_advantage_on_self: bool = gives_advantage_on_self
    
    def __repr__(self) -> str:
        return "[italic blue]" + str(self.name) + "[/italic blue]"

    def reduce_damage(self, damage: int, character) -> int:
        
        if not self.reduces_damage:
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

# Damage reduction
BarbarianRaging = Condition(
    name=BuffCondition.barbarian_raging,
    reduces_damage=True,
)
Hiding = Condition(
    name=BuffCondition.hiding, 
    roll_alteration=RollAlteration.advantage,
)
Resistant = Condition(
    name=BuffCondition.resistant,
    reduces_damage=True,
)
UndeadFortitude = Condition(
    name=BuffCondition.undead_fortitude,
    reduces_damage=True,
)

# Improving rolls
BardicInspiration = Condition(
    name=BuffCondition.bardic_inspiration,
    roll_alteration=RollAlteration.dice_modifier,
    dice={Dice.d6: 1,},
)
Blessed = Condition(
    name=BuffCondition.blessed,
    roll_alteration=RollAlteration.dice_modifier,
    dice={Dice.d4: 1,},
)

barbarian_rage_damage_reduction = {
    1: .3
}

conditions_removed_at_turn_start = []
conditions_removed_at_turn_end = []
conditions_removed_at_combat_end = [BarbarianRaging, BardicInspiration, Hiding, Blessed]
conditions_removed_on_action = [Hiding]