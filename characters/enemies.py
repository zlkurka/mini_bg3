from tools.enums import EnemyType, Weapon, Encounter
from tools.character import Enemy

Goblin1 = Enemy(name="Gug", 
               enemytype=EnemyType.goblin, 
               max_hp=8, 
               attacks={
        Weapon.shortsword: 6,
        Weapon.shortbow: 6,
    })
Goblin2 = Enemy(name="Gurp", 
               enemytype=EnemyType.goblin, 
               max_hp=8, 
               attacks={
        Weapon.shortsword: 6,
        Weapon.shortbow: 6,
    })
Goblin3 = Enemy(name="Gunk", 
               enemytype=EnemyType.goblin, 
               max_hp=8, 
               attacks={
        Weapon.shortsword: 6,
        Weapon.shortbow: 6,
    })
Goblin4 = Enemy(name="Skunk", 
               enemytype=EnemyType.goblin, 
               max_hp=8, 
               attacks={
        Weapon.shortsword: 6,
        Weapon.shortbow: 6,
    })

Owlbear = Enemy(name="Owlbear", 
               enemytype=EnemyType.owlbear, 
               max_hp=91, 
               attacks={
        Weapon.owlbear_claw: 21,
    })

encounters = {
    
    Encounter.goblins_4x: [
        Goblin1,
        Goblin2,
        Goblin3,
        Goblin4,
    ],

    Encounter.owlbear: [
        Owlbear
    ]

}