from tools.enums import EnemyType, Encounter, AbilityScore
from tools.character import Monster
from random import sample, randint
from tools.attacks import Shortsword, Shortbow, OwlbearClaw
from tools.actions import PassAction

def get_monsters(encounter=Encounter):
    
    if encounter == Encounter.goblins_4x:
        
        names = sample(goblin_names,4)

        Goblin1 = Monster(
            name = names[0], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 12,
            actions = [
                Shortsword,
                Shortbow,
            ],
            ability_scores={
                AbilityScore.STR: 2,
                AbilityScore.DEX: 0,
                AbilityScore.CON: 1,
                AbilityScore.INT: -1,
                AbilityScore.WIS: 1,
                AbilityScore.CHA: 0,
            },)
        Goblin2 = Monster(
            name = names[1], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 12,
            actions = [
                Shortsword,
                Shortbow,
            ],
            ability_scores={
                AbilityScore.STR: 2,
                AbilityScore.DEX: 0,
                AbilityScore.CON: 1,
                AbilityScore.INT: -1,
                AbilityScore.WIS: 1,
                AbilityScore.CHA: 0,
            },)
        Goblin3 = Monster(
            name = names[2], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 12,
            actions = [
                Shortsword,
                Shortbow,
            ],
            ability_scores={
                AbilityScore.STR: 2,
                AbilityScore.DEX: 0,
                AbilityScore.CON: 1,
                AbilityScore.INT: -1,
                AbilityScore.WIS: 1,
                AbilityScore.CHA: 0,
            },)
        Goblin4 = Monster(
            name = names[3], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 12,
            actions = [
                Shortsword,
                Shortbow,
            ],
            ability_scores={
                AbilityScore.STR: 2,
                AbilityScore.DEX: 0,
                AbilityScore.CON: 1,
                AbilityScore.INT: -1,
                AbilityScore.WIS: 1,
                AbilityScore.CHA: 0,
            },)
        
        return [Goblin1, Goblin2, Goblin3, Goblin4]

    if encounter == Encounter.owlbear:
        Owlbear = Monster(
            name = "Owlbear", 
            enemytype = EnemyType.owlbear, 
            max_hp = randint(85,100), 
            armor_class = 14,
            actions = [
                OwlbearClaw,
            ],
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
        TrainingDummy = Monster(
            name = "training dummy", 
            enemytype = EnemyType.training_dummy, 
            max_hp = 9999, 
            armor_class = 10,
            actions = [PassAction],
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
]