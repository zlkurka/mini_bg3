from tools.enums import Weapon, AbilityScore, Dice, CharClass
from tools.actions import Action
from random import randint

class Attack(Action):

    self.name = name


    self.damage_dice: dict = damage_dice
    self.modifier: AbilityScore = modifier
    self.multi_attack: int = multi_attack


    self.ranged: bool = ranged
    self.use_damage_modifier: bool = use_damage_modifier


    if spell_slot_level:
        self.spell_slot_level: int = spell_slot_level
    else:
        self.spell_slot_level: int = 0
    
    def action(self, character, enemies, team):
        
        if self.spell_slot_level > 0:
            if not character.cast_leveled_spell(spell_slot_level):
                return character, enemies, team

        attack_modifier = self.get_modifier(self.modifier, character)

        for iter in range(self.multi_attack):
            
            enemy_chosen = None
            while not enemy_chosen:
                enemy_chosen = character.choose_enemy(enemies)
                if enemy_chosen.current_hp <= 0:
                    enemy_chosen = None

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
        
        if self.ranged:
            try:
                character.lastAttack_isMelee = False
            except AttributeError:
                pass
        else:
            try:
                character.lastAttack_isMelee = True
            except AttributeError:
                pass

        return character, enemies, team

# Weapons

Crossbow = Attack(
    name = Weapon.crossbow, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.DEX,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = True,
)
Dagger = Attack(
    name = Weapon.dagger, 
    damage_dice = {Dice.d4: 1},
    modifier = AbilityScore.finesse,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = True,
)
EldritchBlast = Attack(
    name = Weapon.eldritch_blast, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = False,
)
Firebolt = Attack(
    name = Weapon.firebolt, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = False,
)
Greataxe = Attack(
    name = Weapon.greataxe, 
    damage_dice = {Dice.d12: 1},
    modifier = AbilityScore.STR,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = True,
)
Longsword = Attack(
    name = Weapon.longsword, 
    damage_dice = {Dice.d10: 1},
    modifier = AbilityScore.STR,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)
Mace = Attack(
    name = Weapon.mace, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.STR,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)
RayOfFrost = Attack(
    name = Weapon.ray_of_frost, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = False,
)
Shillelagh = Attack(
    name = Weapon.shillelagh, 
    damage_dice = {Dice.d8: 1},
    modifier = AbilityScore.WIS,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)
Shortbow = Attack(
    name = Weapon.shortbow, 
    damage_dice = {Dice.d6: 1},
    modifier = AbilityScore.DEX,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = True,
)
Shortsword = Attack(
    name = Weapon.shortsword, 
    damage_dice = {Dice.d6: 1},
    modifier = AbilityScore.finesse,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)
MonkUnarmed = Attack(
    name = Weapon.unarmed, 
    damage_dice = {Dice.d4: 1},
    modifier = AbilityScore.finesse,
    multi_attack = 2,
    ranged = False,
    use_damage_modifier = True,
)


# Leveled spells
ChromaticOrb = Attack(
   name = Spell.chromatic_orb,
   damage_dice = {Dice.d8: 3},
   modifier = AbilityScore.spellcasting,
   multi_attack = 1,
   ranged = True,
   use_damage_modifier = False,
   spell_slot_level = 1,
)


# Enemy-specific

OwlbearClaw = Attack(
    name = Weapon.owlbear_claw, 
    damage_dice = {Dice.d8: 2},
    modifier = AbilityScore.STR,
    multi_attack = 2,
    ranged = False,
    use_damage_modifier = True,
)