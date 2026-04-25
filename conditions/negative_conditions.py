from conditions.condition_class import Condition
from tools.enums import RollAlteration, Dice, RollType, AbilityScore, Skill

# Roll alteration
ClunkyArmor = Condition(
    name="clunky armor",
    roll_alteration=RollAlteration.disadvantage,
    applicable_roll_types=[Skill.stealth],
    # TODO Idk how I want to make this work
)

# Ticking damage
Bleeding = Condition(
    name="bleeding",
    dice={Dice.d4: 1},
    health_tick=-1,
)

# Incapacitating
Imprisoned = Condition(
    name="imprisoned",
    incapacitated=True,
)