from conditions.condition_class import Condition
from tools.enums import BuffCondition, RollAlteration, Dice

# Incoming damage alteration
BarbarianRaging = Condition(
    name=BuffCondition.barbarian_raging,
    alters_incoming_damage=True,
)
Hiding = Condition(
    name=BuffCondition.hiding, 
    roll_alteration=RollAlteration.advantage,
)
Resistant = Condition(
    name=BuffCondition.resistant,
    alters_incoming_damage=True,
)
UndeadFortitude = Condition(
    name=BuffCondition.undead_fortitude,
    alters_incoming_damage=True,
)

# Outgoing damage alteration
BajesusFreakingOut = Condition(
    name=BuffCondition.bajesus_freaking_out,
    alters_outgoing_damage=True,
    modifier=2,
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