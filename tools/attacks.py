from tools.enums import Weapon, AbilityScore, Dice, CharClass
from random import randint

class Attack():

    def __init__(self, name=Weapon, dice=dict, modifier=AbilityScore, multi_attack=int):
        
        self.name: Weapon = name
        self.damage_dice: dict = dice
        self.modifier: AbilityScore = modifier
        self.multi_attack: int = multi_attack

    def action(self, character, enemies, team):

        for iter in range(self.multi_attack):

            enemy_chosen = character.choose_enemy(enemies)

            if randint(1,20) >= enemy_chosen.armor_class:
                
                damage = self.get_damage()
                
                print(f"\n{character.name} hits {enemy_chosen.name} with {self.name.value} for {damage} damage!")

                enemy_chosen.take_damage(damage)
                enemies[enemies.index(enemy_chosen)] = enemy_chosen
            
            else:
                damage = 0
                print(f"\n{character.name} misses {enemy_chosen.name} with {self.name.value}.")

        return character, enemies, team
    
    def get_damage(self):
        
        damage = 0
        
        for dice in self.damage_dice:
            for roll in range(dice):

                damage += randint(1, self.damage_dice[dice].value)
        
        return damage

# Weapons

Crossbow = Attack(
    name = Weapon.crossbow, 
    dice = {1: Dice.d10},
    modifier = AbilityScore.DEX,
    multi_attack = 1
)
Dagger = Attack(
    name = Weapon.dagger, 
    dice = {1: Dice.d4},
    modifier = AbilityScore.DEX,
    multi_attack = 1
)
EldritchBlast = Attack(
    name = Weapon.eldritch_blast, 
    dice = {1: Dice.d10},
    modifier = AbilityScore.CHA,
    multi_attack = 1
)
Firebolt = Attack(
    name = Weapon.firebolt, 
    dice = {1: Dice.d10},
    modifier = AbilityScore.CHA,
    multi_attack = 1
)
Greataxe = Attack(
    name = Weapon.greataxe, 
    dice = {1: Dice.d12},
    modifier = AbilityScore.STR,
    multi_attack = 1
)
Longsword = Attack(
    name = Weapon.longsword, 
    dice = {1: Dice.d10},
    modifier = AbilityScore.STR,
    multi_attack = 1
)
Mace = Attack(
    name = Weapon.mace, 
    dice = {1: Dice.d8},
    modifier = AbilityScore.STR,
    multi_attack = 1
)
RayOfFrost = Attack(
    name = Weapon.ray_of_frost, 
    dice = {1: Dice.d8},
    modifier = AbilityScore.INT,
    multi_attack = 1
)
Shillelagh = Attack(
    name = Weapon.shillelagh, 
    dice = {1: Dice.d8},
    modifier = AbilityScore.WIS,
    multi_attack = 1
)
Shortbow = Attack(
    name = Weapon.shortbow, 
    dice = {1: Dice.d6},
    modifier = AbilityScore.DEX,
    multi_attack = 1
)
Shortsword = Attack(
    name = Weapon.shortsword, 
    dice = {1: Dice.d6},
    modifier = AbilityScore.DEX,
    multi_attack = 1
)
MonkUnarmed = Attack(
    name = Weapon.unarmed, 
    dice = {1: Dice.d4},
    modifier = AbilityScore.DEX,
    multi_attack = 2
)

# Enemy-specific

OwlbearClaw = Attack(
    name = Weapon.owlbear_claw, 
    dice = {2: Dice.d8},
    modifier = AbilityScore.STR,
    multi_attack = 2
)

base_weapon = {
    
    CharClass.barbarian: Longsword,
    CharClass.bard: Shortbow,
    CharClass.cleric: Mace,
    CharClass.druid: Shortsword,
    CharClass.fighter: Longsword,
    CharClass.monk: MonkUnarmed,
    CharClass.paladin: Longsword,
    CharClass.ranger: Shortbow,
    CharClass.rogue: Shortsword,
    CharClass.sorcerer: Firebolt,
    CharClass.warlock: Firebolt,
    CharClass.wizard: Firebolt,

}