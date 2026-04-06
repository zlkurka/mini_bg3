from actions.buff_debuff.buff_debuff_class import Buff
from conditions.conditions import *
from tools.enums import SpecialAction, Spell

# General
Hide = Buff(
    name=SpecialAction.hide, 
    condition=Hiding, 
    targetSelf=True
)

# Leveled spells
Bless = Buff(
    name=Spell.bless,
    condition=Blessed,
    spell_slot_level=1,
    multi_target=3
)

# Class-specific
BarbarianRage = Buff(
    name=SpecialAction.barbarian_rage, 
    condition=BarbarianRaging, 
    targetSelf=True
)
BardicInspire = Buff(
    name=SpecialAction.bardic_inspire,
    condition=BardicInspiration,
)

# Monster-specific
BajesusFreakOut = Buff(
    name=SpecialAction.bajesus_freak_out,
    condition=BajesusFreakingOut,
    targetSelf=True,
)