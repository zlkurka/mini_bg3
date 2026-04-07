from copy import deepcopy
from characters.character_class import Character
from actions.attacks.attacks import DevKillAll, DevKillOne
from tools.enums import CharacterName, CharClass, Race, AbilityScore, CharacterType, Skill

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
    skills=[
        Skill.acrobatics,
        Skill.investigation,
        Skill.sleight_of_hand,
        Skill.stealth,
    ],
)
Faylen = Character(
    name="Faylen",  
    character_type=CharacterType.companion,
    charclass=CharClass.druid, 
    race=Race.half_elf, 
    level=1,
    ability_scores={
        AbilityScore.STR: -1,
        AbilityScore.DEX: 1,
        AbilityScore.CON: 2,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 3,
        AbilityScore.CHA: 0,
    },
    skills=[
        Skill.religion,
        Skill.insight,
    ]
)
BingusGringus = Character(
    name="Bingus Gringus",  
    character_type=CharacterType.companion,
    charclass=CharClass.sorcerer, 
    race=Race.goblin, 
    level=1,
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 1,
        AbilityScore.CON: 2,
        AbilityScore.INT: 0,
        AbilityScore.WIS: -1,
        AbilityScore.CHA: 3,
    },
    skills=[
        Skill.deception,
        Skill.persuasion,
    ]
)


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
    skills=[
        Skill.deception,
        Skill.persuasion,
        Skill.sleight_of_hand,
        Skill.stealth,
    ],
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
    skills=[
        Skill.arcana,
        Skill.history,
    ],
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
    skills=[
        Skill.athletics,
        Skill.intimidation,
    ],
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
    skills=[
        Skill.athletics,
        Skill.insight,
    ],
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
    skills=[
        Skill.medicine,
        Skill.religion,
    ],
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
    skills=[
        Skill.history,
        Skill.investigation,
    ],
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
    skills=[
        Skill.intimidation,
        Skill.religion,
    ],
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
    skills=[
        Skill.nature,
        Skill.survival,
    ],
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
    skills=[
        Skill.insight,
        Skill.perception,
    ],
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
    skills=[
        Skill.animal_handling,
        Skill.athletics,
        Skill.survival,
    ],
)

# Test characters
TheDev = Character(
    name="The Developer",  
    character_type=CharacterType.companion,
    charclass=CharClass.bard, 
    race=Race.human, 
    level=1,
    max_hp=9999,
    ability_scores={
        AbilityScore.STR: 99,
        AbilityScore.DEX: 99,
        AbilityScore.CON: 99,
        AbilityScore.INT: 99,
        AbilityScore.WIS: 99,
        AbilityScore.CHA: 99,
    },
    skills=[
        Skill.arcana,
        Skill.perception,
        Skill.stealth,
    ],
    extra_actions=[DevKillAll, DevKillOne]
)
DexGod = Character(
    name="The DEX God",  
    character_type=CharacterType.companion,
    charclass=CharClass.rogue, 
    race=Race.tiefling, 
    level=1,
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 99,
        AbilityScore.CON: 0,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 0,
        AbilityScore.CHA: 0,
    },
    skills=[
        Skill.acrobatics,
        Skill.investigation,
        Skill.sleight_of_hand,
        Skill.stealth,
    ],
)
Brains = Character(
    name="The Brains",  
    character_type=CharacterType.companion,
    charclass=CharClass.wizard, 
    race=Race.tiefling, 
    level=1,
    ability_scores={
        AbilityScore.STR: -99,
        AbilityScore.DEX: 0,
        AbilityScore.CON: 0,
        AbilityScore.INT: 99,
        AbilityScore.WIS: 0,
        AbilityScore.CHA: 0,
    },
    skills=[
        Skill.arcana,
        Skill.history,
    ],
)
Brawn = Character(
    name="The Brawn",  
    character_type=CharacterType.companion,
    charclass=CharClass.barbarian, 
    race=Race.tiefling, 
    level=1,
    ability_scores={
        AbilityScore.STR: 99,
        AbilityScore.DEX: 0,
        AbilityScore.CON: 0,
        AbilityScore.INT: -99,
        AbilityScore.WIS: 0,
        AbilityScore.CHA: 0,
    },
    skills=[
        Skill.athletics,
        Skill.acrobatics,
    ],
)
Bard = Character(
    name="Bard",  
    character_type=CharacterType.companion,
    charclass=CharClass.bard, 
    race=Race.tiefling, 
    level=1,
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 2,
        AbilityScore.CON: 0,
        AbilityScore.INT: 1,
        AbilityScore.WIS: -1,
        AbilityScore.CHA: 3,
    },
    skills=[
        Skill.acrobatics,
        Skill.performance,
        Skill.persuasion,
    ],
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
    skills=[
        Skill.acrobatics,
        Skill.religion,
    ],
)