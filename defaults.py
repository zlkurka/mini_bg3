from enums import CharClass, Weapon, EnemyType, Encounter, CharacterName

base_weapon = {
    
    CharClass.barbarian: Weapon.greataxe,
    CharClass.bard: Weapon.hand_crossbow,
    CharClass.cleric: Weapon.mace,
    CharClass.druid: Weapon.shillelagh,
    CharClass.fighter: Weapon.longsword,
    CharClass.monk: Weapon.unarmed,
    CharClass.paladin: Weapon.longsword,
    CharClass.ranger: Weapon.shortbow,
    CharClass.rogue: Weapon.dagger,
    CharClass.sorcerer: Weapon.firebolt,
    CharClass.warlock: Weapon.eldritch_blast,
    CharClass.wizard: Weapon.firebolt,

}

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

weapon_damage = {
    
    Weapon.dagger: 4,
    Weapon.eldritch_blast: 10,
    Weapon.firebolt: 10,
    Weapon.greataxe: 12,
    Weapon.hand_crossbow: 6,
    Weapon.longsword: 10,
    Weapon.mace: 8,
    Weapon.shillelagh: 8,
    Weapon.shortbow: 6,
    Weapon.shortsword: 6,
    Weapon.unarmed: 4,

}