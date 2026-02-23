from tools.enums import Weapon, AbilityScore, Dice, CharClass
from tools.actions import Action
from random import randint

class Attack(Action):

    def __init__(self, name=Weapon, damage_dice=dict, modifier=AbilityScore, multi_attack=int):
        
        self.name: Weapon = name
        self.damage_dice: dict = damage_dice
        self.modifier: AbilityScore = modifier
        self.multi_attack: int = multi_attack

    def action(self, character, enemies, team):

        for iter in range(self.multi_attack):

            enemy_chosen = character.choose_enemy(enemies)

            if randint(1,20) >= enemy_chosen.armor_class:
                
                damage = self.roll_dice(self.damage_dice)
                
                print(f"\n{character.name} hits {enemy_chosen.name} with {self.name} for {damage} damage!")

                enemy_chosen.take_damage(damage)
                enemies[enemies.index(enemy_chosen)] = enemy_chosen
            
            else:
                damage = 0
                print(f"\n{character.name} misses {enemy_chosen.name} with {self.name}.")

        return character, enemies, team

# Weapons

Crossbow = Attack(
    name = Weapon.crossbow.value, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.DEX,
    multi_attack = 1
)
Dagger = Attack(
    name = Weapon.dagger.value, 
    damage_dice = {Dice.d4: 1},
    modifier = AbilityScore.DEX,
    multi_attack = 1
)
EldritchBlast = Attack(
    name = Weapon.eldritch_blast.value, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.CHA,
    multi_attack = 1
)
Firebolt = Attack(
    name = Weapon.firebolt.value, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.CHA,
    multi_attack = 1
)
Greataxe = Attack(
    name = Weapon.greataxe.value, 
    damage_dice = {Dice.d12: 1},
    modifier = AbilityScore.STR,
    multi_attack = 1
)
Longsword = Attack(
    name = Weapon.longsword.value, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.STR,
    multi_attack = 1
)
Mace = Attack(
    name = Weapon.mace.value, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.STR,
    multi_attack = 1
)
RayOfFrost = Attack(
    name = Weapon.ray_of_frost.value, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.INT,
    multi_attack = 1
)
Shillelagh = Attack(
    name = Weapon.shillelagh.value, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.WIS,
    multi_attack = 1
)
Shortbow = Attack(
    name = Weapon.shortbow.value, 
    damage_dice = {Dice.d6: 1},
    modifier = AbilityScore.DEX,
    multi_attack = 1
)
Shortsword = Attack(
    name = Weapon.shortsword.value, 
    damage_dice = {Dice.d6: 1},
    modifier = AbilityScore.DEX,
    multi_attack = 1
)
MonkUnarmed = Attack(
    name = Weapon.unarmed.value, 
    damage_dice = {Dice.d4: 1},
    modifier = AbilityScore.DEX,
    multi_attack = 2
)

# Enemy-specific

OwlbearClaw = Attack(
    name = Weapon.owlbear_claw.value, 
    damage_dice = {Dice.d8: 2},
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