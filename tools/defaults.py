from tools.enums import CharClass, Weapon, Armor, Consumable, Shield, Race, AbilityScore, CasterType, Skill
from actions.attacks.attacks import *
from actions.heal.heal import *
from actions.summon.summon import *
from actions.buff_debuff.buffs import *
from actions.action_class import PassAction

# Character building blocks
char_classes: list = [

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

char_races: list = [

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

ability_scores: list = [

    AbilityScore.STR,
    AbilityScore.DEX,
    AbilityScore.CON,
    AbilityScore.INT,
    AbilityScore.WIS,
    AbilityScore.CHA,
    
]

class_caster_types: dict = {
  
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


# Bases
base_hp_charclass: dict = {
    
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

}

base_armor_class: dict = {

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

base_actions: dict = {
    
    # Companion classes

    CharClass.barbarian: [Greataxe],
    CharClass.bard: [Shortsword, Crossbow, CureWounds],
    CharClass.cleric: [Mace, SacredFlame, HealingWord, CureWounds, Bless],
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

base_consumable_actions: dict = {
    
    # Companion classes

    CharClass.barbarian: {BarbarianRage: 2,},
    CharClass.bard: {BardicInspire: AbilityScore.CHA,},
    CharClass.cleric: {},
    CharClass.druid: {},
    CharClass.fighter: {},
    CharClass.monk: {},
    CharClass.paladin: {},
    CharClass.ranger: {},
    CharClass.rogue: {},
    CharClass.sorcerer: {},
    CharClass.warlock: {},
    CharClass.wizard: {},

}

base_skill_options: dict = {
  
    CharClass.barbarian: [
        Skill.athletics,
        Skill.animal_handling,
        Skill.intimidation,
        Skill.nature,
        Skill.perception,
        Skill.survival,
    ],
    CharClass.bard: [
        Skill.athletics,
        Skill.acrobatics,
        Skill.initiative,
        Skill.sleight_of_hand,
        Skill.stealth,
        Skill.arcana,
        Skill.history,
        Skill.investigation,
        Skill.nature,
        Skill.religion,
        Skill.animal_handling,
        Skill.insight,
        Skill.medicine,
        Skill.perception,
        Skill.survival,
        Skill.deception,
        Skill.intimidation,
        Skill.performance,
        Skill.persuasion,
    ],
    CharClass.cleric: [
        Skill.history,
        Skill.insight,
        Skill.medicine,
        Skill.persuasion,
        Skill.religion,
    ],
    CharClass.druid: [
        Skill.animal_handling,
        Skill.arcana,
        Skill.insight,
        Skill.medicine,
        Skill.nature,
        Skill.perception,
        Skill.religion,
        Skill.survival,
    ],
    CharClass.fighter: [
        Skill.acrobatics,
        Skill.animal_handling,
        Skill.athletics,
        Skill.history,
        Skill.insight,
        Skill.intimidation,
        Skill.persuasion,
        Skill.perception,
        Skill.survival,
    ],
    CharClass.monk: [
        Skill.acrobatics,
        Skill.athletics,
        Skill.history,
        Skill.insight,
        Skill.religion,
        Skill.stealth,
    ],
    CharClass.paladin: [
        Skill.athletics,
        Skill.insight,
        Skill.intimidation,
        Skill.medicine,
        Skill.persuasion,
        Skill.religion,
    ],
    CharClass.ranger: [
        Skill.animal_handling,
        Skill.athletics,
        Skill.athletics,
        Skill.insight,
        Skill.investigation,
        Skill.nature,
        Skill.perception,
        Skill.stealth,
        Skill.survival,
    ],
    CharClass.rogue: [
        Skill.acrobatics,
        Skill.athletics,
        Skill.deception,
        Skill.insight,
        Skill.intimidation,
        Skill.investigation,
        Skill.perception,
        Skill.persuasion,
        Skill.sleight_of_hand,
        Skill.stealth,
    ],
    CharClass.sorcerer: [
        Skill.arcana,
        Skill.deception,
        Skill.insight,
        Skill.intimidation,
        Skill.persuasion,
        Skill.religion,
    ],
    CharClass.warlock: [
        Skill.arcana,
        Skill.deception,
        Skill.history,
        Skill.intimidation,
        Skill.investigation,
        Skill.nature,
        Skill.religion,
    ],
    CharClass.wizard: [
        Skill.arcana,
        Skill.history,
        Skill.insight,
        Skill.investigation,
        Skill.medicine,
        Skill.nature,
        Skill.religion,
    ],

}

base_skill_choice_number: dict = {
  
    CharClass.barbarian: 2,
    CharClass.bard: 3,
    CharClass.cleric: 2,
    CharClass.druid: 2,
    CharClass.fighter: 2,
    CharClass.monk: 2,
    CharClass.paladin: 2,
    CharClass.ranger: 3,
    CharClass.rogue: 4,
    CharClass.sorcerer: 2,
    CharClass.warlock: 2,
    CharClass.wizard: 2,

}

spell_slot_counts: dict = {

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
empty_spell_slots: dict = spell_slot_counts[CasterType.nonCaster][1]

base_equipment: dict = {

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

base_spells: dict = {
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

# Values
skill_ability_scores: dict = {

    # Strength
    Skill.athletics: AbilityScore.STR,
    
    # Dexterity
    Skill.acrobatics: AbilityScore.DEX,
    Skill.initiative: AbilityScore.DEX,
    Skill.sleight_of_hand: AbilityScore.DEX,
    Skill.stealth: AbilityScore.DEX,
    
    # Intelligence
    Skill.arcana: AbilityScore.INT,
    Skill.history: AbilityScore.INT,
    Skill.investigation: AbilityScore.INT,
    Skill.nature: AbilityScore.INT,
    Skill.religion: AbilityScore.INT,

    # Wisdom
    Skill.animal_handling: AbilityScore.WIS,
    Skill.insight: AbilityScore.WIS,
    Skill.medicine: AbilityScore.WIS,
    Skill.perception: AbilityScore.WIS,
    Skill.survival: AbilityScore.WIS,

    # Charisma
    Skill.deception: AbilityScore.CHA,
    Skill.intimidation: AbilityScore.CHA,
    Skill.performance: AbilityScore.CHA,
    Skill.persuasion: AbilityScore.CHA,

}

class_spellcasting_ability_scores: dict = {
    AbilityScore.INT: [
        CharClass.wizard,
    ],
    AbilityScore.WIS: [
        CharClass.cleric,
        CharClass.druid,
        CharClass.ranger,
    ],
    AbilityScore.CHA: [
        CharClass.bard,
        CharClass.paladin,
        CharClass.sorcerer,
        CharClass.warlock,
    ],
}

armor_values: dict = {

    # Light
    Armor.leather: 11,

    # Medium
    Armor.hide: 12,
    Armor.chain_shirt: 13,
    Armor.scale_mail: 14,

}