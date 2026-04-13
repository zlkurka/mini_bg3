from characters.character_class import Character
from items.weapons import *
from conditions.conditions import UndeadFortitude
from actions.attacks.attacks import CatScratch, ShortswordStrike, ShortbowStrike, ZombieSlam
from actions.buff_debuff.buffs import BajesusFreakOut
from tools.enums import CharClass, AbilityScore, CharacterType, SummonType

Bajesus = Character(
    name = "Bajesus", 
    character_type = CharacterType.monster,
    max_hp=12,
    ability_scores={
        AbilityScore.STR: 2,
        AbilityScore.DEX: 0,
        AbilityScore.CON: 2,
        AbilityScore.INT: -2,
        AbilityScore.WIS: -1,
        AbilityScore.CHA: -1,
    },
    equipped_items = [Shortsword, Shortbow],
    extra_actions = [BajesusFreakOut],
)
Cat = Character(
    name = "cat",
    character_type = CharacterType.monster,
    charclass = CharClass.cat, 
    max_hp=2,
    actions=[CatScratch],
    ability_scores={
        AbilityScore.STR: -4,
        AbilityScore.DEX: 2,
        AbilityScore.CON: 0,
        AbilityScore.INT: -4,
        AbilityScore.WIS: 1,
        AbilityScore.CHA: 0,
    },
    summon_type=SummonType.familiar,
)
Goblin = Character(
    name = "goblin", 
    character_type = CharacterType.monster,
    charclass = CharClass.goblin, 
    base_max_hp=9,
    ability_scores={
        AbilityScore.STR: 2,
        AbilityScore.DEX: 0,
        AbilityScore.CON: 1,
        AbilityScore.INT: -1,
        AbilityScore.WIS: 1,
        AbilityScore.CHA: 0,
    },
    equipped_items = [Shortsword, Shortbow],
)
Skeleton = Character(
    name = "skeleton", 
    character_type = CharacterType.monster,
    charclass = CharClass.skeleton, 
    base_max_hp = 10, # Decreased from 13 to 10 bc skeletons have crazy damage output
    armor_class = 14,
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 3,
        AbilityScore.CON: 2,
        AbilityScore.INT: -2,
        AbilityScore.WIS: -1,
        AbilityScore.CHA: -3,
    },
    equipped_items = [Shortsword, Shortbow],
)
Owlbear = Character(
    name = "owlbear",
    character_type = CharacterType.monster,
    charclass = CharClass.owlbear, 
    base_max_hp=90,
    ability_scores={
        AbilityScore.STR: 4,
        AbilityScore.DEX: 1,
        AbilityScore.CON: 3,
        AbilityScore.INT: -3,
        AbilityScore.WIS: 2,
        AbilityScore.CHA: 0,
    },)
TrainingDummy = Character(
    name = "training dummy", 
    character_type = CharacterType.monster,
    charclass = CharClass.training_dummy, 
    max_hp = 9999, 
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 0,
        AbilityScore.CON: 0,
        AbilityScore.INT: 0,
        AbilityScore.WIS: 0,
        AbilityScore.CHA: 0,
    },)
Zombie = Character(
    name = "zombie", 
    character_type = CharacterType.monster,
    charclass = CharClass.zombie, 
    base_max_hp = 22, 
    armor_class = 8,
    ability_scores={
        AbilityScore.STR: 1,
        AbilityScore.DEX: -2,
        AbilityScore.CON: 3,
        AbilityScore.INT: -4,
        AbilityScore.WIS: -2,
        AbilityScore.CHA: -3,
    },
    conditions=[UndeadFortitude],
    actions=[ZombieSlam]
)

goblin_names = [
    "Gug",
    "Brung",
    "Gunk",
    "Skunk",
    "Bucket",
    "Haldron",
    "Cauldron",
    "Schlerb",
    "Schug",
    "Brick",
    "Bronk",
    "Kronn",
    "Leg",
]

summon_types = {
    SummonType.familiar: [
        Cat,
    ],
}