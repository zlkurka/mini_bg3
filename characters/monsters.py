from tools.enums import CharClass, Encounter, AbilityScore, CharacterType
from tools.character import Character
from random import sample

def get_monsters(encounter=Encounter):
    
    if encounter == Encounter.goblins_4x:
        
        names = sample(goblin_names,4)
        enemies = []

        for iter in range(4):
            enemies.append(Character(
            name = names[iter], 
            character_type = CharacterType.monster,
            charclass = CharClass.goblin, 
            ability_scores={
                AbilityScore.STR: 2,
                AbilityScore.DEX: 0,
                AbilityScore.CON: 1,
                AbilityScore.INT: -1,
                AbilityScore.WIS: 1,
                AbilityScore.CHA: 0,
            },))
        
        return enemies

    if encounter == Encounter.owlbear:
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
        return [Owlbear]
    

    if encounter == Encounter.training_dummy:
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
        return [TrainingDummy]


goblin_names = [
    "Gug",
    "Brung",
    "Gunk",
    "Skunk",
    "Bucket",
    "Haldron",
    "Cauldron",
    "Bingus Gringus",
    "Schlerb Holdonimthinkingofsomethinginteresting",
    "Bajesus Beezlebub"
]