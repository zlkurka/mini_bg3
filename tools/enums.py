from enum import Enum

class EnumWithValueRepr(Enum):

    def __repr__(self):
        return self.value
    
    def __str__(self):
        return self.value

class CharacterName(EnumWithValueRepr):
    
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

class CharClass(EnumWithValueRepr):

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

class Race(EnumWithValueRepr):

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

class EnemyType(EnumWithValueRepr):
    
    goblin = "goblin"
    bugbear = "bugbear"
    owlbear = "owlbear"

class Weapon(EnumWithValueRepr):
    
    # Weapons
    crossbow = "crossbow"
    dagger = "dagger"
    greataxe = "greataxe"
    longsword = "longsword"
    mace = "mace"
    shortbow = "shortbow"
    shortsword = "shortsword"
    unarmed = "unarmed strike"

    # Cantrips
    eldritch_blast = "eldritch blast"
    firebolt = "firebolt"
    shillelagh = "shillelagh"
    ray_of_frost = "ray of frost"

    # Enemy-specific attacks
    owlbear_claw = "claw"

class Spell(EnumWithValueRepr):

    cure_wounds = "cure wounds"
    
    # Class-specific
    barbarian_rage = "rage"

class Armor(EnumWithValueRepr):
    
    # Light
    leather = "leather armor"

    # Medium
    chain_shirt = "chain shirt"
    hide = "hide armor"
    scale_mail = "scale mail"

class Shield(EnumWithValueRepr):

    basic = "shield"

class Consumable(EnumWithValueRepr):
    
    # Ammunition
    arrow = "arrow"

    # Potions
    healing_potion = "healing potion"

class Encounter(EnumWithValueRepr):
    
    goblins_4x = "Four goblins"
    owlbear = "Owlbear"

class AbilityScore(EnumWithValueRepr):

    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    INT = "intelligence"
    WIS = "wisdom"
    CHA = "charisma"

    spellcasting = "spellcasting"
    finesse = "finesse"

class Dice(Enum):

    def __repr__(self):
        return self.name

    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20