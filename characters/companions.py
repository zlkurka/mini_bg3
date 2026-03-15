from tools.character import Companion
from tools.enums import CharacterName, CharClass, Race, AbilityScore

Astarion = Companion(
    name=CharacterName.astarion, 
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
    name=CharacterName.gale, 
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
    name=CharacterName.karlach, 
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
    name=CharacterName.laezel, 
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
    name=CharacterName.shadowheart, 
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
    name=CharacterName.wyll, 
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
Minthara = Companion(
    name=CharacterName.minthara, 
    charclass=CharClass.paladin, 
    race=Race.drow, 
    level=1,
    ability_scores={
        AbilityScore.STR: 3,
        AbilityScore.DEX: -1,
        AbilityScore.CON: 1,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 0,
        AbilityScore.CHA: 2,
    },
)
Halsin = Companion(
    name=CharacterName.halsin, 
    charclass=CharClass.druid, 
    race=Race.elf, 
    level=1,
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 2,
        AbilityScore.CON: 1,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 3,
        AbilityScore.CHA: 0,
    },
)
Jaheira = Companion(
    name=CharacterName.jaheira, 
    charclass=CharClass.druid, 
    race=Race.half_elf, 
    level=1,
    ability_scores={
        AbilityScore.STR: -1,
        AbilityScore.DEX: 0,
        AbilityScore.CON: 2,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 3,
        AbilityScore.CHA: 1,
    },
)
Minsc = Companion(
    name=CharacterName.minsc, 
    charclass=CharClass.ranger, 
    race=Race.human, 
    level=1,
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 2,
        AbilityScore.CON: 1,
        AbilityScore.INT: -1,
        AbilityScore.WIS: 3,
        AbilityScore.CHA: 0,
    },
)