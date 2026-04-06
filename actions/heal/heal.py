from actions.heal.heal_class import Heal
from tools.enums import Spell, Dice

CureWounds = Heal(
    name = Spell.cure_wounds,
    heal_dice = {Dice.d8: 1},
    heal_const = 1,
    can_choose_target = True,
    target_count = 1,
    spell_slot_level=1
)
HealingWord = Heal(
    name = Spell.healing_word,
    heal_dice = {Dice.d4: 1},
    heal_const = 1,
    can_choose_target = True,
    target_count = 1,
    spell_slot_level=0
)