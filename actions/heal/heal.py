from actions.heal.heal_class import Heal
from tools.enums import Spell, Dice, Potion

CureWounds = Heal(
    name = Spell.cure_wounds,
    heal_dice = {Dice.d8: 1},
    heal_const = 1,
    spell_slot_level=1
)
HealingWord = Heal(
    name = Spell.healing_word,
    heal_dice = {Dice.d4: 1},
    heal_const = 1,
    spell_slot_level=0
)
HealingPotion = Heal(
    name = Potion.minor_health,
    heal_dice = {Dice.d4: 2},
    heal_const = 2,
    targetSelf = True,
)