from tools.enums import CharClass, Weapon, Armor, Consumable, Shield
from tools.attacks import Longsword, Shortbow, Mace, Shortsword, MonkUnarmed, Firebolt
from tools.actions import CureWounds

base_hp = {
    
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

base_armor_class = {

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

}

base_actions = {
    
    CharClass.barbarian: [Longsword],
    CharClass.bard: [Shortbow],
    CharClass.cleric: [Mace, CureWounds],
    CharClass.druid: [Shortsword],
    CharClass.fighter: [Longsword, Shortbow],
    CharClass.monk: [MonkUnarmed],
    CharClass.paladin: [Longsword],
    CharClass.ranger: [Shortbow],
    CharClass.rogue: [Shortsword],
    CharClass.sorcerer: [Firebolt],
    CharClass.warlock: [Firebolt],
    CharClass.wizard: [Firebolt],

}

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

base_spells = {}

armor_values = {

    # Light
    Armor.leather: 11,

    # Medium
    Armor.hide: 12,
    Armor.chain_shirt: 13,
    Armor.scale_mail: 14,

}