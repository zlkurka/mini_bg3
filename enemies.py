from enums import EnemyType, Weapon, Encounter
from character import Enemy

GoblinGug = Enemy(name="Gug", 
               enemytype=EnemyType.goblin, 
               max_hp=8, 
               attacks={
        Weapon.shortsword: 6,
        Weapon.shortbow: 6,
    })
GoblinGurp = Enemy(name="Gurp", 
               enemytype=EnemyType.goblin, 
               max_hp=8, 
               attacks={
        Weapon.shortsword: 6,
        Weapon.shortbow: 6,
    })
GoblinGunk = Enemy(name="Gunk", 
               enemytype=EnemyType.goblin, 
               max_hp=8, 
               attacks={
        Weapon.shortsword: 6,
        Weapon.shortbow: 6,
    })
GoblinSkunk = Enemy(name="Skunk", 
               enemytype=EnemyType.goblin, 
               max_hp=8, 
               attacks={
        Weapon.shortsword: 6,
        Weapon.shortbow: 6,
    })

encounters = {
    
    Encounter.goblins_4x: [
        GoblinGug,
        GoblinGurp,
        GoblinGunk,
        GoblinSkunk,
    ]

}

enemy_enum_matcher = {

    EnemyType.goblin: None,

}