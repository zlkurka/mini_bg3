from tools.enums import CharClass, Encounter, AbilityScore, CharacterType, SummonType, Dice
from characters.character import Character
from conditions.condition import UndeadFortitude
from actions.attacks import Attack, CatScratch, Shortsword, Shortbow
from random import sample, choice
from copy import deepcopy

def get_monsters(encounter: Encounter) -> list:
    
    if encounter == Encounter.goblins_4x:
        
        names = sample(goblin_names,4)
        enemies = []

        for iter in range(4):
            new_enemy = deepcopy(Goblin)
            new_enemy.name = names[iter]
            new_enemy.reset()
            enemies.append(new_enemy)

    elif encounter == Encounter.owlbear:
        enemies = [deepcopy(Owlbear)]
    
    elif encounter == Encounter.training_dummy:
        enemies = [deepcopy(TrainingDummy)]
    
    elif encounter == Encounter.undead_group:
        enemies = []
        for iter in range(4):
            new_enemy = deepcopy(choice([Skeleton, Zombie]))
            new_enemy.reset()
            enemies.append(new_enemy)

    # Numbering enemies with duplicate names
    used_names = []
    for char in enemies: 
        if char.name in used_names:
            name_added_num = 2
            while True:
                alt_name = str(char.name) + " " + str(name_added_num)
                if alt_name in used_names:
                    name_added_num += 1
                    continue
                char.name = alt_name
                break
        used_names.append(char.name)
    
    return enemies

Cat = Character(
    name = "cat",
    character_type = CharacterType.monster,
    charclass = CharClass.cat, 
    max_hp=2,
    extra_actions=[CatScratch],
    ability_scores={
        AbilityScore.STR: -4,
        AbilityScore.DEX: 2,
        AbilityScore.CON: 0,
        AbilityScore.INT: -4,
        AbilityScore.WIS: 1,
        AbilityScore.CHA: 0,
    },)
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
    },)
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
    extra_actions=[Shortsword, Shortbow]
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
    extra_actions=[Attack(
        name="slam",
        damage_dice={Dice.d6: 1} ,
        ability_score_modifier=AbilityScore.STR,  
    )]
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
    "Bajesus"
]

summon_types = {
    SummonType.familiar: [
        Cat,
    ],
}