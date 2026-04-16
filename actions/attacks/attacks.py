from actions.attacks.attack_class import Attack
from conditions.positive_conditions import Hiding
from tools.enums import Weapon, AbilityScore, Dice, Spell
            
# Melee weapons
DaggerStrike = Attack(
    name = Weapon.dagger, 
    damage_dice = {Dice.d4: 1},
    ability_score_modifier = AbilityScore.finesse,
    multi_target = 1,
    ranged = False,
    use_damage_modifier = True,
)
GreataxeStrike = Attack(
    name = Weapon.greataxe, 
    damage_dice = {Dice.d12: 1},
    ability_score_modifier = AbilityScore.STR,
    multi_target = 1,
    ranged = False,
    use_damage_modifier = True,
)
GreatswordStrike = Attack(
    name = Weapon.greatsword, 
    damage_dice = {Dice.d6: 2},
    ability_score_modifier = AbilityScore.STR,
    multi_target = 1,
    ranged = False,
    use_damage_modifier = True,
)
LongswordStrike = Attack(
    name = Weapon.longsword, 
    damage_dice = {Dice.d10: 1},
    ability_score_modifier = AbilityScore.STR,
    multi_target = 1,
    ranged = False,
    use_damage_modifier = True,
)
MaceStrike = Attack(
    name = Weapon.mace, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.STR,
    multi_target = 1,
    ranged = False,
    use_damage_modifier = True,
)
ShortswordStrike = Attack(
    name = Weapon.shortsword, 
    damage_dice = {Dice.d6: 1},
    ability_score_modifier = AbilityScore.finesse,
    multi_target = 1,
    ranged = False,
    use_damage_modifier = True,
)
MonkUnarmed = Attack(
    name = Weapon.unarmed, 
    damage_dice = {Dice.d4: 1},
    ability_score_modifier = AbilityScore.finesse,
    multi_target = 3,
    ranged = False,
    use_damage_modifier = True,
)


# Ranged weapons
CrossbowStrike = Attack(
    name = Weapon.crossbow, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.DEX,
    multi_target = 1,
    ranged = True,
    use_damage_modifier = True,
)
ShortbowStrike = Attack(
    name = Weapon.shortbow, 
    damage_dice = {Dice.d6: 1},
    ability_score_modifier = AbilityScore.DEX,
    multi_target = 1,
    ranged = True,
    use_damage_modifier = True,
)


# Cantrips
EldritchBlast = Attack(
    name = Spell.eldritch_blast, 
    damage_dice = {Dice.d10: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_target = 1,
    ranged = True,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
Firebolt = Attack(
    name = Spell.firebolt, 
    damage_dice = {Dice.d10: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_target = 1,
    ranged = True,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
PoisonSpray = Attack(
    name = Spell.poison_spray, 
    damage_dice = {Dice.d12: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_target = 1,
    ranged = True,
    savingThrow_abilityScore=AbilityScore.CON,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
RayOfFrost = Attack(
    name = Spell.ray_of_frost, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_target = 1,
    ranged = True,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
SacredFlame = Attack(
    name = Spell.sacred_flame, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_target = 1,
    ranged = True,
    savingThrow_abilityScore=AbilityScore.DEX,
    use_damage_modifier = False,
    spell_slot_level = 0,
)
Shillelagh = Attack(
    name = Spell.shillelagh, 
    damage_dice = {Dice.d8: 1},
    ability_score_modifier = AbilityScore.spellcasting,
    multi_target = 1,
    ranged = False,
    use_damage_modifier = True,
    spell_slot_level = 0,
)


# Magic weapons
Longsword_plus1Strike = Attack(
    name = str(Weapon.longsword) + ", +1", 
    damage_dice = {Dice.d10: 1},
    ability_score_modifier = AbilityScore.STR,
    multi_target = 1,
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
    multi_target = 1,
    ranged = True,
    use_damage_modifier = False,
    spell_slot_level = 1,
)


# Special attacks
RogueSneakAttack = Attack(
    name = Weapon.rogue_sneak_attack,
    damage_dice = {Dice.d6: 2},
    ability_score_modifier = AbilityScore.finesse,
    multi_target = 1,
    ranged = False,
    use_damage_modifier = True,
    required_self_conditions = [Hiding]
)


# Enemy-specific
CatScratch = Attack(
    name = Weapon.owlbear_claw, 
    damage_dice = {Dice.d1: 1},
    ability_score_modifier = AbilityScore.finesse,
    multi_target = 1,
    ranged = False,
    use_damage_modifier = True,
)
OwlbearClaw = Attack(
    name = Weapon.owlbear_claw, 
    damage_dice = {Dice.d8: 2},
    ability_score_modifier = AbilityScore.STR,
    multi_target = 2,
    ranged = False,
    use_damage_modifier = True,
)
ZombieSlam =Attack(
    name="slam",
    damage_dice={Dice.d6: 1} ,
    ability_score_modifier=AbilityScore.STR,
    use_damage_modifier=True,
)

DevKillOne =Attack(
    name="kill one",
    damage_dice={Dice.d1: 999},
    ability_score_modifier=AbilityScore.spellcasting,
    use_damage_modifier=False,
)
DevKillAll =Attack(
    name="kill all",
    damage_dice={Dice.d1: 999},
    ability_score_modifier=AbilityScore.spellcasting,
    use_damage_modifier=True,
    area_of_effect=True,
    savingThrow_abilityScore=AbilityScore.WIS,
    halfDamage_onSave=True,
)