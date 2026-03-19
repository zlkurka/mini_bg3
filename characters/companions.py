from characters.character import Character
from tools.enums import CharacterName, CharClass, Race, AbilityScore, CharacterType

# BG3 companions

Astarion = Character(
    name=CharacterName.astarion, 
    character_type=CharacterType.companion,
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
Gale = Character(
    name=CharacterName.gale,  
    character_type=CharacterType.companion,
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
Karlach = Character(
    name=CharacterName.karlach,  
    character_type=CharacterType.companion,
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
Laezel = Character(
    name=CharacterName.laezel,  
    character_type=CharacterType.companion,
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
Shadowheart = Character(
    name=CharacterName.shadowheart,  
    character_type=CharacterType.companion,
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
Wyll = Character(
    name=CharacterName.wyll,  
    character_type=CharacterType.companion,
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
Minthara = Character(
    name=CharacterName.minthara,  
    character_type=CharacterType.companion,
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
Halsin = Character(
    name=CharacterName.halsin,  
    character_type=CharacterType.companion,
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
Jaheira = Character(
    name=CharacterName.jaheira,  
    character_type=CharacterType.companion,
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
Minsc = Character(
    name=CharacterName.minsc,  
    character_type=CharacterType.companion,
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

# Original characters

Nightkill = Character(
    name="Nightkill",  
    character_type=CharacterType.companion,
    charclass=CharClass.rogue, 
    race=Race.halfling, 
    level=1,
    ability_scores={
        AbilityScore.STR: -1,
        AbilityScore.DEX: 3,
        AbilityScore.CON: 0,
        AbilityScore.INT: 1,
        AbilityScore.WIS: 2,
        AbilityScore.CHA: 0,
    },
)
Faylen = Character(
    name="Faylen",  
    character_type=CharacterType.companion,
    charclass=CharClass.druid, 
    race=Race.half_elf, 
    level=1,
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 1,
        AbilityScore.CON: 2,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 3,
        AbilityScore.CHA: 0,
    },
)
Monk = Character(
    name="Monk",  
    character_type=CharacterType.companion,
    charclass=CharClass.monk, 
    race=Race.elf, 
    level=1,
    ability_scores={
        AbilityScore.STR: 1,
        AbilityScore.DEX: 3,
        AbilityScore.CON: 0,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 2,
        AbilityScore.CHA: -1,
    },
)