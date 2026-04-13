from actions.summon.summon_class import Summon
from tools.enums import SummonType, MenuOptions, Spell

FindFamiliar = Summon(
    name=Spell.find_familiar,
    spell_slot_level=1,
    summon_type=SummonType.familiar,
    creatureCanAttack=True,
)