from tools.enums import CharClass, Weapon, Armor, Consumable, Shield, Race, AbilityScore, CasterType
from actions.attacks import *
from actions.heal import *
from actions.summon import *
from actions.buff_debuff import *
from actions.action import PassAction

char_classes = [

    CharClass.barbarian,
    CharClass.bard,
    CharClass.cleric,
    CharClass.druid,
    CharClass.fighter,
    CharClass.monk,
    CharClass.paladin,
    CharClass.ranger,
    CharClass.rogue,
    CharClass.sorcerer,
    CharClass.warlock,
    CharClass.wizard,

]

char_races = [

    Race.dragonborn,
    Race.dwarf,
    Race.elf,
    Race.githyanki,
    Race.gnome,
    Race.half_elf,
    Race.half_orc,
    Race.halfling,
    Race.human,
    Race.tiefling,

]

ability_scores = [

    AbilityScore.STR,
    AbilityScore.DEX,
    AbilityScore.CON,
    AbilityScore.INT,
    AbilityScore.WIS,
    AbilityScore.CHA,
    
]

base_max_hp = {
    
    # Companion classes

    CharClass.barbarian: 12,
    CharClass.bard: 8,
    CharClass.cleric: 8,
    CharClass.druid: 8,
    CharClass.fighter: 10,
    CharClass.monk: 8,
    CharClass.paladin: 10,
    CharClass.ranger: 10,
    CharClass.rogue: 8,
    CharClass.sorcerer: 6,
    CharClass.warlock: 8,
    CharClass.wizard: 6,


    # Monster classes

    CharClass.goblin: 9,
    CharClass.owlbear: 90,
    CharClass.training_dummy: 1000

}

base_armor_class = {

    # Companion classes

    CharClass.barbarian: 13,
    CharClass.bard: 13,
    CharClass.cleric: 16,
    CharClass.druid: 14,
    CharClass.fighter: 16,
    CharClass.monk: 14,
    CharClass.paladin: 16,
    CharClass.ranger: 14,
    CharClass.rogue: 14,
    CharClass.sorcerer: 10,
    CharClass.warlock: 12,
    CharClass.wizard: 10,


    # Monster classes

    CharClass.goblin: 12,
    CharClass.owlbear: 14,
    CharClass.training_dummy: 10,

}

base_actions = {
    
    # Companion classes

    CharClass.barbarian: [Greataxe, BarbarianRage],
    CharClass.bard: [Shortsword, Crossbow, CureWounds],
    CharClass.cleric: [Mace, SacredFlame, HealingWord, CureWounds],
    CharClass.druid: [Shillelagh, PoisonSpray, Shortbow, CureWounds],
    CharClass.fighter: [Longsword, Shortbow],
    CharClass.monk: [MonkUnarmed],
    CharClass.paladin: [Longsword, Crossbow],
    CharClass.ranger: [Shortsword, Shortbow],
    CharClass.rogue: [Dagger, Shortbow, RogueSneakAttack],
    CharClass.sorcerer: [Firebolt, PoisonSpray, ChromaticOrb, BurningHands],
    CharClass.warlock: [EldritchBlast, PoisonSpray, ArmsOfHadar],
    CharClass.wizard: [Firebolt, PoisonSpray, ChromaticOrb, BurningHands],


    # Monster classes

    CharClass.goblin: [Shortsword, Shortsword],
    CharClass.owlbear: [OwlbearClaw],
    CharClass.training_dummy: [PassAction],

}

class_caster_types = {
  
   CharClass.barbarian: CasterType.nonCaster,
   CharClass.bard: CasterType.fullCaster,
   CharClass.cleric: CasterType.fullCaster,
   CharClass.druid: CasterType.fullCaster,
   CharClass.fighter: CasterType.nonCaster,
   CharClass.monk: CasterType.nonCaster,
   CharClass.paladin: CasterType.halfCaster,
   CharClass.ranger: CasterType.halfCaster,
   CharClass.rogue: CasterType.nonCaster,
   CharClass.sorcerer: CasterType.fullCaster,
   CharClass.warlock: CasterType.fullCaster,
   CharClass.wizard: CasterType.fullCaster,

}

spell_slot_counts = {

    # Caster Types

    CasterType.fullCaster: {
        # Char Levels
        1: {
            # Spell Levels
            1: 2,
        },
    },
    CasterType.halfCaster: {
        # Char Levels
        1: {
            # Spell Levels
            1: 0,
        },
    },
    CasterType.quarterCaster: {
        # Char Levels
        1: {
            # Spell Levels
            1: 0,
        },
    },
    CasterType.nonCaster: {
        # Char Levels
        1: {
            # Spell Levels
            1: 0,
        },
    },

}

empty_spell_slots = spell_slot_counts[CasterType.nonCaster][1]

base_equipment = {

    CharClass.barbarian: [Weapon.longsword],
    CharClass.bard: [Weapon.shortbow, Armor.leather, Consumable.arrow],
    CharClass.cleric: [Weapon.mace, Armor.chain_shirt, Shield.basic],
    CharClass.druid: [Weapon.shillelagh, Armor.hide],
    CharClass.fighter: [Weapon.longsword, Armor.scale_mail],
    CharClass.monk: [],
    CharClass.paladin: [Weapon.longsword, Armor.scale_mail, Shield.basic],
    CharClass.ranger: [Weapon.shortbow, Armor.leather, Consumable.arrow],
    CharClass.rogue: [Weapon.shortsword, Armor.leather],
    CharClass.sorcerer: [],
    CharClass.warlock: [Weapon.shortsword, Armor.leather],
    CharClass.wizard: [],

}

base_spells = {
    CharClass.barbarian: [],
    CharClass.bard: [CureWounds],
    CharClass.cleric: [CureWounds],
    CharClass.druid: [CureWounds],
    CharClass.fighter: [],
    CharClass.monk: [],
    CharClass.paladin: [],
    CharClass.ranger: [],
    CharClass.rogue: [],
    CharClass.sorcerer: [ChromaticOrb],
    CharClass.warlock: [], # Add spell
    CharClass.wizard: [ChromaticOrb],
}

armor_values = {

    # Light
    Armor.leather: 11,

    # Medium
    Armor.hide: 12,
    Armor.chain_shirt: 13,
    Armor.scale_mail: 14,

}