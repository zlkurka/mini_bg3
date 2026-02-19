from enums import CharClass, Race, Weapon, EnemyType
from defaults import base_weapon, base_hp, weapon_damage
from random import randint, choice
from menu import menu

class Character():
    
    def __init__(self, name=str, charclass=CharClass, race=Race, level=int):
        
        self.name: str = name
        self.charclass: CharClass = charclass
        self.race: Race = race
        self.level: int = level
        # self.subclass = subclass
        # self.subrace = subrace
        
        self.max_hp: int = int(base_hp[charclass] + ((level - 1) * (base_hp[charclass] / 2 + 1)))
        self.attacks: dict = {
            base_weapon[charclass]: weapon_damage[base_weapon[charclass]],
        }
    
    def attack(self, enemies):
        
        if len(enemies) > 1:
            enemy_choice = menu(enemies, "Who would you like to attack?")
        else:
            enemy_choice = enemies[0]
        
        if len(self.attacks) > 1:
            attack_choice = menu(list(self.attacks), "What attack would you like to use?")
        else:
            attack_choice = list(self.attacks)[0]

        damage = randint(1, self.attacks[attack_choice])
        print(f"{self.name} hits {enemy_choice.name} for {damage} damage!")
        return damage, enemy_choice
    
class Enemy():
    
    def __init__(self, name=str, enemytype=EnemyType, max_hp=int, attacks=dict):
        
        self.name: str = name
        self.enemytype: CharClass = enemytype
        
        self.max_hp: int = max_hp
        self.attacks: dict = attacks
    
    def attack(self, party):
        
        enemy_choice = choice(party)
        attack_choice = choice(list(self.attacks))

        damage = randint(1, self.attacks[attack_choice])
        print(f"{self.name} hits {enemy_choice.name} for {damage} damage!")
        return damage, enemy_choice
    
    def change_name(self, new_name=str):
        self.name = new_name
        return self