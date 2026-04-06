from characters.character_class import Character
from conditions.conditions import UndeadFortitude
from actions.attacks import CatScratch, Shortsword, Shortbow, ZombieSlam
from actions.buff_debuff import BajesusFreakOut
from tools.enums import CharClass, AbilityScore, CharacterType, SummonType

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
    },)
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
    actions = [Shortsword, Shortbow, BajesusFreakOut],
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
    actions=[Shortsword, Shortbow],
    )
Skeleton = Character(
    name = "skeleton", 
    character_type = CharacterType.monster,
    charclass = CharClass.skeleton, 
    base_max_hp = 13,
    armor_class = 14,
    ability_scores={
        AbilityScore.STR: 0,
        AbilityScore.DEX: 3,
        AbilityScore.CON: 2,
        AbilityScore.INT: -2,
        AbilityScore.WIS: -1,
        AbilityScore.CHA: -3,
    },
    actions=[Shortsword, Shortbow],
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
    "Bingus Gringus",
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