from enum import Enum

class EnumWithValueRepr(Enum):

    def __repr__(self):
        return self.value
    
    def __str__(self):
        return self.value

# Names
class CharacterName(EnumWithValueRepr):
    
    tav = "TAV"
    
    # Original characters
    nightkill = "Nightkill"
    faylen = "Faylen"

    # BG3 Characters
    astarion = "Astarion"
    gale = "Gale"
    karlach = "Karlach"
    laezel = "Lae'zel"
    shadowheart = "Shadowheart"
    wyll = "Wyll"
    minthara = "Minthara"
    halsin = "Halsin"
    jaheira = "Jaheira"
    minsc = "Minsc"

class Encounter(EnumWithValueRepr):
    
    goblins_4x = "four goblins"
    owlbear = "owlbear"
    training_dummy = "training dummy"


# Character attributes
class CharClass(EnumWithValueRepr):

    # Companion classes

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


    # Enemy classes
    
    cat = "cat"
    goblin = "goblin"
    bugbear = "bugbear"
    owlbear = "owlbear"
    training_dummy = "training dummy"

class Race(EnumWithValueRepr):

    dragonborn = "dragonborn"
    drow = "drow"
    dwarf = "dwarf"
    elf = "elf"
    githyanki = "githyanki"
    gnome = "gnome"
    half_elf = "half-elf"
    half_orc = "half-orc"
    halfling = "halfling"
    human = "human"
    tiefling = "tiefling"

class AbilityScore(EnumWithValueRepr):

    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    INT = "intelligence"
    WIS = "wisdom"
    CHA = "charisma"

    spellcasting = "spellcasting"
    finesse = "finesse"

class Skill(EnumWithValueRepr):

    # Strength
    athletics = "athletics"

    # Dexterity
    acrobatics = "acrobatics"
    initiative = "initiative"
    sleight_of_hand = "sleight of hand"
    stealth = "stealth"

    # Intelligence
    arcana = "arcana"
    history = "history"
    investigation = "investigation"
    nature = "nature"
    religion = "religion"
    
    # Wisdom
    animal_handling = "animal_handling"
    insight = "insight"
    medicine = "medicine"
    perception = "perception"
    survival = "survival"
    
    # Charisma
    deception = "deception"
    intimidation = "intimidation"
    performance = "performance"
    persuasion = "persuasion"

class CasterType(EnumWithValueRepr):

   fullCaster = "full caster"
   halfCaster = "half caster"
   quarterCaster = "quarter caster"
   nonCaster = "non-caster"

class CharacterType(EnumWithValueRepr):

    companion = "companion"
    monster = "monster"

class SummonType(EnumWithValueRepr):

    familiar = "familiar"

# Actions
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
    poison_spray = "poison spray"
    ray_of_frost = "ray of frost"
    sacred_flame = "sacred flame"
    shillelagh = "shillelagh"

    # Special attacks
    rogue_sneak_attack = "sneak attack"
    
    # Enemy-specific attacks
    owlbear_claw = "claw"

class Spell(EnumWithValueRepr):
    
    # Cantrips
    healing_word = "healing word"

    # 1st level
    arms_of_hadar = "arms of hadar"
    bless = "bless"
    burning_hands = "burning hands"
    cure_wounds = "cure wounds"
    chromatic_orb = "chromatic orb"

class SpecialAction(EnumWithValueRepr):

    # General
    hide = "hide"

    # Class-specific
    barbarian_rage = "rage"
    bardic_inspire = "bardic inspire"


# Equipment
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


# Other
class Dice(Enum):

    def __repr__(self):
        return self.name

    d0 = 0
    d1 = 1
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20

class MenuOptions(EnumWithValueRepr):

    nevermind = "nevermind"

class BuffCondition(EnumWithValueRepr):

    barbarian_raging = "raging"
    bardic_inspiration = "bardic inspiration"
    blessed = "blessed"
    hiding = "hiding"
    resistant = "resistant"

class RollAlteration(EnumWithValueRepr):

    advantage = "advantage"
    disadvantage = "disadvantage"
    dice_modifier = "dice modifier"
    flat_modifer = "flat modifier"