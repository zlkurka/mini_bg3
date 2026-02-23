from tools.enums import EnemyType, Encounter
from tools.character import Monster
from random import sample, randint
from tools.attacks import Shortsword, Shortbow, OwlbearClaw

def get_monsters(encounter=Encounter):
    
    if encounter == Encounter.goblins_4x:
        
        names = sample(goblin_names,4)

        Goblin1 = Monster(
            name = names[0], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 1,
            actions = [
                Shortsword,
                Shortbow,
            ])
        Goblin2 = Monster(
            name = names[1], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 1,
            actions = [
                Shortsword,
                Shortbow,
            ])
        Goblin3 = Monster(
            name = names[2], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 1,
            actions = [
                Shortsword,
                Shortbow,
            ])
        Goblin4 = Monster(
            name = names[3], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 1,
            actions = [
                Shortsword,
                Shortbow,
            ])
        
        return [Goblin1, Goblin2, Goblin3, Goblin4]

    if encounter == Encounter.owlbear:
        Owlbear = Monster(
            name = "Owlbear", 
            enemytype = EnemyType.owlbear, 
            max_hp = randint(85,100), 
            armor_class = 14,
            actions = [
                OwlbearClaw,
            ])
        return [Owlbear]


goblin_names = [
    "Gug",
    "Brung",
    "Gunk",
    "Skunk",
    "Bucket",
]