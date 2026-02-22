from tools.enums import CharClass, Race, EnemyType
from tools.defaults import base_hp, base_equipment, armor_values, base_armor_class
from random import randint, choice
from tools.menu import menu
from tools.attacks import base_weapon

class Character():
    
    def __init__(self, name=str, charclass=CharClass, race=Race, level=int):
        
        self.name: str = name
        self.charclass: CharClass = charclass
        self.race: Race = race
        self.level: int = level
        # self.subclass = subclass
        # self.subrace = subrace
        
        self.max_hp: int = int(base_hp[charclass] + ((level - 1) * (base_hp[charclass] / 2 + 1)))
        self.current_hp: int = self.max_hp
        
        self.armor_class: int = base_armor_class[self.charclass]
        self.attacks: list = [base_weapon[self.charclass]]

        # self.equipment = base_equipment[self.charclass]
    
    def attack(self, enemies):
        
        if len(enemies) > 1:
            enemy_choice = menu(enemies, f"\nWho would {self.name} like to attack?")
        else:
            enemy_choice = enemies[0]
        
        if len(self.attacks) > 1:
            attack_choice = menu(list(self.attacks), "What attack would you like to use?")
        else:
            attack_choice = self.attacks[0]
        
        if randint(1,20) >= enemy_choice.armor_class:
            damage = attack_choice.get_damage()
            print(f"\n{self.name} hits {enemy_choice.name} with {attack_choice.name.value} for {damage} damage!")
        else:
            damage = 0
            print(f"\n{self.name} misses {enemy_choice.name} with {attack_choice.name.value}.")

        return damage, enemy_choice
    
    def take_damage(self, damage):

        self.current_hp -= damage

        if self.current_hp <= 0:
            self.current_hp = 0
            print(f"{self.name} has died!")

            return True
        
        print(f"{self.name} has {self.current_hp} health remaining.")
        return False
    
class Enemy():
    
    def __init__(self, name=str, enemytype=EnemyType, max_hp=int, armor_class=int, attacks=list):
        
        self.name: str = name
        self.enemytype: CharClass = enemytype
        
        self.max_hp: int = max_hp
        self.current_hp: int = self.max_hp
        self.armor_class: int = armor_class
        
        self.attacks: list = attacks
    
    def attack(self, party):
        
        enemy_choice = choice(party)
        attack_choice = choice(self.attacks)

        if randint(1,20) >= enemy_choice.armor_class:
            damage = attack_choice.get_damage()
            print(f"\n{self.name} hits {enemy_choice.name} with {attack_choice.name.value} for {damage} damage!")
        else:
            damage = 0
            print(f"\n{self.name} misses {enemy_choice.name} with {attack_choice.name.value}.")

        return damage, enemy_choice
    
    def take_damage(self, damage):

        self.current_hp -= damage

        if self.current_hp <= 0:
            self.current_hp = 0
            print(f"{self.name} has died!")

            return True
        
        print(f"{self.name} has {self.current_hp} health remaining.")
        return False
    
    def change_name(self, new_name=str):
        self.name = new_name
        return self