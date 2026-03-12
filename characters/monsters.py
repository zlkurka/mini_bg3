from tools.enums import EnemyType, Encounter, AbilityScore
from tools.character import Monster
from random import sample, randint, choice
from tools.attacks import Shortsword, Shortbow, OwlbearClaw

def get_monsters(encounter=Encounter):
    
    if encounter == Encounter.goblins_4x:
        
        names = sample(goblin_names,4)

        monsters = []
        for iter in range(4):
            monsters.append(
                Monster(
                    name = names[iter], 
                    enemytype = EnemyType.goblin, 
                    max_hp = randint(7,11), 
                    armor_class = 12,
                    actions = [
                        Shortsword,
                        Shortbow,
                    ],
                    ability_scores = {
                        AbilityScore.STR: 2,
                        AbilityScore.DEX: 0,
                        AbilityScore.CON: 1,
                        AbilityScore.INT: -1,
                        AbilityScore.WIS: 1,
                        AbilityScore.CHA: 0,
                    },))
                   
        return monsters

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


goblin_names = [
    "Gug",
    "Brung",
    "Gunk",
    "Skunk",
    "Bucket",
]