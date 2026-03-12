from tools.enums import Weapon, AbilityScore, Dice, CharClass
from tools.actions import Action
from random import randint

class Attack(Action):

    def __init__(self, name=str, damage_dice=dict, modifier=AbilityScore, multi_attack=int, use_damage_modifier=bool):
        
        self.name: str = name
        self.damage_dice: dict = damage_dice
        self.modifier: AbilityScore = modifier
        self.multi_attack: int = multi_attack
        self.use_damage_modifier: bool = use_damage_modifier

    def __repr__(self):
        return self.name
    
    def action(self, character, enemies, team):

        attack_modifier = self.get_modifier(AbilityScore.STR, character)

        for iter in range(self.multi_attack):

            enemy_chosen = character.choose_enemy(enemies)

            if randint(1,20) + attack_modifier >= enemy_chosen.armor_class:
                
                damage = self.roll_dice(self.damage_dice)

                if self.use_damage_modifier:
                    damage += attack_modifier
                
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
    multi_attack = 1,
    use_damage_modifier = True,
)
Dagger = Attack(
    name = Weapon.dagger.value, 
    damage_dice = {Dice.d4: 1},
    modifier = AbilityScore.finesse,
    multi_attack = 1,
    use_damage_modifier = True,
)
EldritchBlast = Attack(
    name = Weapon.eldritch_blast.value, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.CHA,
    multi_attack = 1,
    use_damage_modifier = False,
)
Firebolt = Attack(
    name = Weapon.firebolt.value, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    use_damage_modifier = False,
)
Greataxe = Attack(
    name = Weapon.greataxe.value, 
    damage_dice = {Dice.d12: 1},
    modifier = AbilityScore.STR,
    multi_attack = 1,
    use_damage_modifier = True,
)
Longsword = Attack(
    name = Weapon.longsword.value, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.STR,
    multi_attack = 1,
    use_damage_modifier = True,
)
Mace = Attack(
    name = Weapon.mace.value, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.STR,
    multi_attack = 1,
    use_damage_modifier = True,
)
RayOfFrost = Attack(
    name = Weapon.ray_of_frost.value, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    use_damage_modifier = False,
)
Shillelagh = Attack(
    name = Weapon.shillelagh.value, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.WIS,
    multi_attack = 1,
    use_damage_modifier = True,
)
Shortbow = Attack(
    name = Weapon.shortbow.value, 
    damage_dice = {Dice.d6: 1},
    modifier = AbilityScore.DEX,
    multi_attack = 1,
    use_damage_modifier = True,
)
Shortsword = Attack(
    name = Weapon.shortsword.value, 
    damage_dice = {Dice.d6: 1},
    modifier = AbilityScore.finesse,
    multi_attack = 1,
    use_damage_modifier = True,
)
MonkUnarmed = Attack(
    name = Weapon.unarmed.value, 
    damage_dice = {Dice.d4: 1},
    modifier = AbilityScore.finesse,
    multi_attack = 2,
    use_damage_modifier = True,
)

# Enemy-specific

OwlbearClaw = Attack(
    name = Weapon.owlbear_claw.value, 
    damage_dice = {Dice.d8: 2},
    modifier = AbilityScore.STR,
    multi_attack = 2,
    use_damage_modifier = True,
)