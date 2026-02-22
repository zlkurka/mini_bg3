from tools.enums import EnemyType, Weapon, Encounter
from tools.character import Enemy
from random import sample, randint
from tools.attacks import Shortsword, Shortbow, OwlbearClaw

def get_enemies(encounter=Encounter):
    
    if encounter == Encounter.goblins_4x:
        
        names = sample(goblin_names,4)

        Goblin1 = Enemy(name = names[0], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 12,
            attacks = [
                Shortsword,
                Shortbow,
            ])
        
        Goblin2 = Enemy(name = names[1], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 12,
            attacks = [
                Shortsword,
                Shortbow,
            ])
        
        Goblin3 = Enemy(name = names[2], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 12,
            attacks = [
                Shortsword,
                Shortbow,
            ])
        
        Goblin4 = Enemy(name = names[3], 
            enemytype = EnemyType.goblin, 
            max_hp = randint(7,11), 
            armor_class = 12,
            attacks = [
                Shortsword,
                Shortbow,
            ])
        
        return [Goblin1, Goblin2, Goblin3, Goblin4]
    

    if encounter == Encounter.owlbear:
        Owlbear = Enemy(name = "Owlbear", 
               enemytype = EnemyType.owlbear, 
               max_hp = randint(85,100), 
               armor_class = 14,
               attacks = [
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