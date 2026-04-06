from tools.enums import Weapon, AbilityScore, Dice, Spell, MenuOptions
from actions.action import Action
from conditions.conditions import Hiding
from random import randint
from rich import print
from tools.rich_capitalize import rich_capitalize
from tools.roll_d20 import roll_d20

class Attack(Action):
    
    def __init__(
        self, 
        name, 
        damage_dice: dict, 
        ability_score_modifier: AbilityScore, 
        multi_attack: int = 1, 
        ranged: bool = False, 
        area_of_effect: bool = False, 
        savingThrow_abilityScore: AbilityScore = None, 
        halfDamage_onSave: bool = False, 
        use_damage_modifier: bool = True, 
        spell_slot_level: int = 0,
        weapon_bonus: int = 0,
    ):
        
        self.name = name
        self.damage_dice: dict = damage_dice
        self.ability_score_modifier: AbilityScore = ability_score_modifier
        self.ranged: bool = ranged
        self.use_damage_modifier: bool = use_damage_modifier
        self.spell_slot_level: int = spell_slot_level
        self.savingThrow_abilityScore: AbilityScore = savingThrow_abilityScore
        self.weapon_bonus: int = weapon_bonus

        if area_of_effect == True:
            self.area_of_effect: bool = True
            self.multi_attack: int = 0
            self.halfDamage_onSave: bool = halfDamage_onSave
        else: 
            self.area_of_effect: bool = False
            self.multi_attack: int = multi_attack
            self.halfDamage_onSave: bool = False

    def action(self, character, enemies: list, team: list, fighters: list):
        
        nevermindSelected = False 

        # Expend spell slot
        if self.spell_slot_level > 0:
            if not character.cast_leveled_spell(self.spell_slot_level):
                nevermindSelected = True 
                return character, enemies, team, nevermindSelected

        # Sneak attack
        if self.name == Weapon.rogue_sneak_attack and Hiding not in character.conditions:
            nevermindSelected = True 
            return character, enemies, team, nevermindSelected
        
        # Area of effect
        if self.area_of_effect:
            for target in list(enemies):
                if self.check_if_hit(character, target):
                    target, enemies = self.deal_damage(character=character, target=target, enemies=enemies, halved_damage=False)
                else:
                    if self.halfDamage_onSave:
                        target, enemies = self.deal_damage(character=character, target=target, enemies=enemies, halved_damage=True)

        # Single-target
        for iter in range(self.multi_attack):
            if not enemies:
                break
            while True:
                
                target = character.choose_target(targets=enemies, action=self)
                if not target:
                    break
                if target == MenuOptions.nevermind:
                    nevermindSelected = True
                    return character, enemies, team, nevermindSelected
                
                if target.current_hp <= 0:
                    continue
                if self.check_if_hit(character, target):
                    target, enemies = self.deal_damage(character=character, target=target, enemies=enemies, halved_damage=False)
                break

        # Update lastAttack_isMelee
        if self.ranged:
            character.lastAttack_isMelee = False
        else: 
            character.lastAttack_isMelee = True

        # Return
        return character, enemies, team, nevermindSelected
    
    def check_if_hit(self, character, target):
        
        attack_modifier: int = character.get_modifier(ability_type=self.ability_score_modifier) + self.weapon_bonus
        
        if self.savingThrow_abilityScore:
            hitSuccessful = roll_d20(character=target, roll_bonus=target.ability_scores[self.savingThrow_abilityScore]) <= attack_modifier + 8 # change if I add proficiency bonuses
        else:
            hitSuccessful =  roll_d20(character=character, roll_bonus=attack_modifier) >= target.armor_class
        
        if not hitSuccessful and not self.halfDamage_onSave:
            print(f"{rich_capitalize(character)} misses {target} with {self.name}.")
        return hitSuccessful
    
    def deal_damage(self, character, target, enemies, halved_damage: bool):
        damage = self.roll_dice(self.damage_dice)

        for cond in character.conditions:
            damage = cond.alter_outgoing_damage(damage, character)

        if self.use_damage_modifier:
            damage += character.get_modifier(self.ability_score_modifier) + self.weapon_bonus
        
        if halved_damage:
            damage = damage // 2
            print(f"{rich_capitalize(target)} resists {character}'s {self.name}, but they still take {damage} damage!")
        else: 
            print(f"{rich_capitalize(character)} hits {target} with {self.name} for {damage} damage!")
        target.take_damage(damage)

        if target.current_hp <= 0:
            enemies.remove(target)
        else:
            enemies[enemies.index(target)] = target

        return target, enemies
        
            
# Melee weapons
Dagger = Attack(
    name = Weapon.dagger, 
    damage_dice = {Dice.d4: 1},
    ability_score_modifier = AbilityScore.finesse,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = True,
)
Greataxe = Attack(
    name = Weapon.greataxe, 
    damage_dice = {Dice.d12: 1},
    ability_score_modifier = AbilityScore.STR,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = True,
)
Longsword = Attack(
    name = Weapon.longsword, 
    damage_dice = {Dice.d10: 1},
    ability_score_modifier = AbilityScore.STR,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)
Mace = Attack(
    name = Weapon.mace, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.STR,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)
Shortsword = Attack(
    name = Weapon.shortsword, 
    damage_dice = {Dice.d6: 1},
    ability_score_modifier = AbilityScore.finesse,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)
MonkUnarmed = Attack(
    name = Weapon.unarmed, 
    damage_dice = {Dice.d4: 1},
    ability_score_modifier = AbilityScore.finesse,
    multi_attack = 3,
    ranged = False,
    use_damage_modifier = True,
)


# Ranged weapons
Crossbow = Attack(
    name = Weapon.crossbow, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.DEX,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = True,
)
Shortbow = Attack(
    name = Weapon.shortbow, 
    damage_dice = {Dice.d6: 1},
    ability_score_modifier = AbilityScore.DEX,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = True,
)


# Cantrips
EldritchBlast = Attack(
    name = Weapon.eldritch_blast, 
    damage_dice = {Dice.d10: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
Firebolt = Attack(
    name = Weapon.firebolt, 
    damage_dice = {Dice.d10: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
PoisonSpray = Attack(
    name = Weapon.poison_spray, 
    damage_dice = {Dice.d12: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = True,
    savingThrow_abilityScore=AbilityScore.CON,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
RayOfFrost = Attack(
    name = Weapon.ray_of_frost, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
SacredFlame = Attack(
    name = Weapon.sacred_flame, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = True,
    savingThrow_abilityScore=AbilityScore.DEX,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
Shillelagh = Attack(
    name = Weapon.shillelagh, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
    spell_slot_level = 0,
)


# Magic weapons
Longsword_plus1 = Attack(
    name = str(Weapon.longsword) + ", +1", 
    damage_dice = {Dice.d10: 1},
    ability_score_modifier = AbilityScore.STR,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)


# Leveled spells
ArmsOfHadar = Attack(
    name = Spell.arms_of_hadar,
    damage_dice = {Dice.d6: 2},
    ability_score_modifier = AbilityScore.spellcasting,
    area_of_effect=True,
    savingThrow_abilityScore=AbilityScore.STR,
    halfDamage_onSave=True,
    ranged = False,
    use_damage_modifier = False,
    spell_slot_level = 1,
)
BurningHands = Attack(
    name = Spell.burning_hands,
    damage_dice = {Dice.d6: 2},
    ability_score_modifier = AbilityScore.spellcasting,
    area_of_effect=True,
    savingThrow_abilityScore=AbilityScore.DEX,
    halfDamage_onSave=True,
    ranged = False,
    use_damage_modifier = False,
    spell_slot_level = 1,
)
ChromaticOrb = Attack(
    name = Spell.chromatic_orb,
    damage_dice = {Dice.d8: 3},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_attack = 1,
    ranged = True,
    use_damage_modifier = False,
    spell_slot_level = 1,
)


# Special attacks
RogueSneakAttack = Attack(
    name = Weapon.rogue_sneak_attack,
    damage_dice = {Dice.d6: 2},
    ability_score_modifier = AbilityScore.finesse,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)


# Enemy-specific
CatScratch = Attack(
    name = Weapon.owlbear_claw, 
    damage_dice = {Dice.d1: 1},
    ability_score_modifier = AbilityScore.finesse,
    multi_attack = 1,
    ranged = False,
    use_damage_modifier = True,
)
OwlbearClaw = Attack(
    name = Weapon.owlbear_claw, 
    damage_dice = {Dice.d8: 2},
    ability_score_modifier = AbilityScore.STR,
    multi_attack = 2,
    ranged = False,
    use_damage_modifier = True,
)
ZombieSlam =Attack(
    name="slam",
    damage_dice={Dice.d6: 1} ,
    ability_score_modifier=AbilityScore.STR,
    use_damage_modifier=True,
)