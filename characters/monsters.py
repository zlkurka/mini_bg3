from tools.enums import CharClass, Encounter, AbilityScore, CharacterType
from tools.character import Character
from tools.attacks import CatScratch
from random import sample
from copy import deepcopy

def get_monsters(encounter=Encounter):
    
    if encounter == Encounter.goblins_4x:
        
        names = sample(goblin_names,4)
        enemies = []

        for iter in range(4):
            new_enemy = deepcopy(Goblin)
            new_enemy.name = names[iter]
            new_enemy.reset()
            enemies.append(new_enemy)
        
        return enemies

    if encounter == Encounter.owlbear:
        return [Owlbear]
    
    if encounter == Encounter.training_dummy:
        return [TrainingDummy]

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
    ability_scores={
        AbilityScore.STR: 2,
        AbilityScore.DEX: 0,
        AbilityScore.CON: 1,
        AbilityScore.INT: -1,
        AbilityScore.WIS: 1,
        AbilityScore.CHA: 0,
    },)
Owlbear = Character(
    name = "owlbear",
    character_type = CharacterType.monster,
    charclass = CharClass.owlbear, 
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