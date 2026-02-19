from enum import Enum

class CharacterName(Enum):
    
    tav = "TAV"
    
    # Origin companions
    astarion = "Astarion"
    gale = "Gale"
    karlach = "Karlach"
    laezel = "Lae'zel"
    shadowheart = "Shadowheart"
    wyll = "Wyll"

    # Non-origin companions
    minthara = "Minthara"
    halsin = "Halsin"
    jaheira = "Jaheira"
    minsc = "Minsc"

class CharClass(Enum):

    barbarian = "barbarian"
    bard = "bard"
    cleric = "cleric"
    druid = "druid"
    fighter = "fighter"
    monk = "monk"
    paladin = "paladin"
    ranger = "ranger"
    rogue = "rogue"
    sorcerer = "sorcerer"
    warlock = "warlock"
    wizard = "wizard"

class Race(Enum):

    dragonborn = "dragonborn"
    dwarf = "dwarf"
    elf = "elf"
    githyanki = "githyanki"
    gnome = "gnome"
    half_elf = "half-elf"
    half_orc = "half-orc"
    halfling = "halfling"
    human = "human"
    tiefling = "tiefling"

class EnemyType(Enum):
    
    goblin = "goblin"
    bugbear = "bugbear"
    owlbear = "owlbear"

class Weapon(Enum):
    
    # Weapons
    dagger = "dagger"
    greataxe = "greataxe"
    hand_crossbow = "hand crossbow"
    longsword = "longsword"
    mace = "mace"
    shortbow = "shortbow"
    shortsword = "shortsword"
    unarmed = "unarmed strike"

    # Cantrips
    eldritch_blast = "eldritch blast"
    firebolt = "firebolt"
    shillelagh = "shillelagh"

class Encounter(Enum):
    goblins_4x = "Four goblins"

class AbilityScore(Enum):

    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    INT = "intelligence"
    WIS = "wisdom"
    CHA = "charisma"