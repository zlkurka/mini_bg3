from tools.character import Companion
from tools.enums import CharacterName, CharClass, Race, AbilityScore

Astarion = Companion(
    name=CharacterName.astarion.value, 
    charclass=CharClass.rogue, 
    race=Race.elf, 
    level=1,
    ability_scores={
        AbilityScore.STR: -1,
        AbilityScore.DEX: 3,
        AbilityScore.CON: 0,
        AbilityScore.INT: 1,
        AbilityScore.WIS: 0,
        AbilityScore.CHA: 2,
    },
)
Gale = Companion(
    name=CharacterName.gale.value, 
    charclass=CharClass.wizard, 
    race=Race.human, 
    level=1,
    ability_scores={
        AbilityScore.STR: -1,
        AbilityScore.DEX: 0,
        AbilityScore.CON: 2,
        AbilityScore.INT: 3,
        AbilityScore.WIS: 1,
        AbilityScore.CHA: 0,
    },
)
Karlach = Companion(
    name=CharacterName.karlach.value, 
    charclass=CharClass.barbarian, 
    race=Race.tiefling, 
    level=1,
    ability_scores={
        AbilityScore.STR: 3,
        AbilityScore.DEX: 0,
        AbilityScore.CON: 2,
        AbilityScore.INT: -1,
        AbilityScore.WIS: 0,
        AbilityScore.CHA: 1,
    },
)
Laezel = Companion(
    name=CharacterName.laezel.value, 
    charclass=CharClass.fighter, 
    race=Race.githyanki, 
    level=1,
    ability_scores={
        AbilityScore.STR: 3,
        AbilityScore.DEX: 2,
        AbilityScore.CON: 1,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 0,
        AbilityScore.CHA: -1,
    },
)
Shadowheart = Companion(
    name=CharacterName.shadowheart.value, 
    charclass=CharClass.cleric, 
    race=Race.half_elf, 
    level=1,
    ability_scores={
        AbilityScore.STR: 1,
        AbilityScore.DEX: -1,
        AbilityScore.CON: 2,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 3,
        AbilityScore.CHA: 0,
    },
)
Wyll = Companion(
    name=CharacterName.wyll.value, 
    charclass=CharClass.warlock, 
    race=Race.human, 
    level=1,
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 2,
        AbilityScore.CON: 1,
        AbilityScore.INT: 0,
        AbilityScore.WIS: -1,
        AbilityScore.CHA: 3,
    },
)