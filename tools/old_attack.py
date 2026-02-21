from enums import Weapon, AbilityScore

class Attack():

    def __init__(self, weapon=Weapon):
        
        self.weapon = weapon
        self.damage = weapon_damage[self.weapon]
        self.modifier = weapon_modifier[self.weapon]
        self.multi_attack = weapon_multiattack[self.weapon]

weapon_damage = {
    
    Weapon.dagger: {1: 4},
    Weapon.eldritch_blast: {1: 10},
    Weapon.firebolt: {1: 10},
    Weapon.greataxe: {1: 12},
    Weapon.hand_crossbow: {1: 6},
    Weapon.longsword: {1: 10},
    Weapon.mace: {1: 8},
    Weapon.ray_of_frost: {1: 8},
    Weapon.shillelagh: {1: 8},
    Weapon.shortbow: {1: 6},
    Weapon.shortsword: {1: 6},
    Weapon.unarmed: {1: 4},

}

weapon_multiattack = {
    
    Weapon.dagger: 1,
    Weapon.eldritch_blast: 1,
    Weapon.firebolt: 1,
    Weapon.greataxe: 1,
    Weapon.hand_crossbow: 1,
    Weapon.longsword: 1,
    Weapon.mace: 1,
    Weapon.ray_of_frost: 1,
    Weapon.shillelagh: 1,
    Weapon.shortbow: 2,
    Weapon.shortsword: 1,
    Weapon.unarmed: 3,

}

weapon_modifier = {
    
    Weapon.dagger: AbilityScore.DEX,
    Weapon.eldritch_blast: AbilityScore.CHA,
    Weapon.firebolt: AbilityScore.CHA,
    Weapon.greataxe: AbilityScore.STR,
    Weapon.hand_crossbow: AbilityScore.DEX,
    Weapon.longsword: AbilityScore.STR,
    Weapon.mace: AbilityScore.STR,
    Weapon.ray_of_frost: AbilityScore.INT,
    Weapon.shillelagh: AbilityScore.WIS,
    Weapon.shortbow: AbilityScore.DEX,
    Weapon.shortsword: AbilityScore.DEX,
    Weapon.unarmed: AbilityScore.DEX,

}