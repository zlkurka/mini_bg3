from conditions.condition_class import Condition
from tools.enums import BuffCondition, RollAlteration, Dice, RollType, AbilityScore, Skill

# Incoming damage alteration
BarbarianRaging = Condition(
    name=BuffCondition.barbarian_raging,
    alters_incoming_damage=True,
)
Hiding = Condition(
    name=BuffCondition.hiding, 
    roll_alteration=RollAlteration.advantage,
    applicable_roll_types=[RollType.attack],
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
MurderHoboBloodRage = Condition(
    name=BuffCondition.murder_hobo_blood_rage,
    alters_outgoing_damage=True,
)
UndeadMurderHoboBloodlessRage = Condition(
    name=BuffCondition.undead_murder_hobo_bloodless_rage,
    alters_outgoing_damage=True,
    modifier = 20,
)

# Altering rolls
BardicInspiration = Condition(
    name=BuffCondition.bardic_inspiration,
    roll_alteration=RollAlteration.dice_modifier,
    applicable_roll_types=[RollType.ability_check, RollType.attack],
    dice={Dice.d6: 1,},
)
Blessed = Condition(
    name=BuffCondition.blessed,
    roll_alteration=RollAlteration.dice_modifier,
    applicable_roll_types=[RollType.attack],
    dice={Dice.d4: 1,},
)

# Armor class
BarbarianUnarmoredDefense = Condition(
    name=BuffCondition.barbarian_unarmored_defense,
    base_armor_class=10,
    ability_scores_added_to_armor_class=[AbilityScore.CON, AbilityScore.DEX],
    maximum_dexterity_modifier_for_armor_class=None,
)
MageArmored = Condition(
    name=BuffCondition.mage_armor,
    base_armor_class=13,
    ability_scores_added_to_armor_class=[AbilityScore.DEX],
    maximum_dexterity_modifier_for_armor_class=None,
)
MonkUnarmoredDefense = Condition(
    name=BuffCondition.monk_unarmored_defense,
    base_armor_class=10,
    ability_scores_added_to_armor_class=[AbilityScore.DEX, AbilityScore.WIS],
    maximum_dexterity_modifier_for_armor_class=None,
)