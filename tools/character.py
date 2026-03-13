from random import choice
from tools.menu import menu
from tools.enums import CharClass, Race, EnemyType, AbilityScore
from tools.defaults import base_hp, base_armor_class, base_actions, class_caster_types, spell_slot_counts, empty_spell_slots

class Character():
    
    def __init__(self, name, max_hp=int, armor_class=int, actions=list, ability_scores=dict, spell_slots=dict):
        
        self.name = name
        
        self.max_hp: int = max_hp
        self.current_hp: int = self.max_hp
        
        self.armor_class: int = armor_class
        self.actions: list = actions
        
        self.ability_scores: dict = ability_scores

        if spell_slots:
            self.spell_slots: dict = spell_slots
        else:
            self.spell_slots = empty_spell_slots

    def __repr__(self):
        return str(self.name)
    
    def action(self, monsters=list, party=list, skipped_fighters=list):
        
        # Choosing action
        if len(self.actions) > 1:
            action_choice = self.choose_action()
        else:
           action_choice = self.actions[0]
        
        # Doing action
        if type(self) == Companion:
            self, monsters, party = action_choice.action(character=self, enemies=monsters, team=party)
        elif type(self) == Monster:
            self, party, monsters = action_choice.action(character=self, enemies=party, team=monsters)
        else:
            print("Error: unacceptable character type!")
        
        # Removing dead characters
        for char in monsters:
            if char.current_hp <= 0:
                skipped_fighters.append(char)
                monsters.remove(char)
        for char in party:
            if char.current_hp <= 0:
                skipped_fighters.append(char)
                party.remove(char)
        
        return monsters, party, skipped_fighters
    
    def choose_action(self):
        return menu(self.actions, f"\nWhat would {self.name} like to do?")
    
    def choose_enemy(self, enemies):
        
        if len(enemies) > 1:
            return menu(enemies, f"\nWho would {self.name} like to attack?", show_race=False, show_class=False, show_hp=True)
        else:
            return enemies[0]

    def take_damage(self, damage):
        
        if damage:
            
            self.current_hp -= damage

            if self.current_hp <= 0:
                self.current_hp = 0
                print(f"{self.name} has died!")

            else:
                print(f"{str(self.name).capitalize()} has {self.current_hp} health remaining.")
        
        else:
            print("No damage dealt.")
    
    def heal(self, heal_amount):
        
        if heal_amount > 0:
            
            if self.current_hp + heal_amount > self.max_hp:
                heal_amount = self.max_hp - self.current_hp
                self.current_hp = self.max_hp
            else:
                self.current_hp += heal_amount

            print(f"{str(self.name).capitalize()} was healed for {heal_amount} HP and now has {self.current_hp} HP.")

    def cast_leveled_spell(self, level):
        if not self.spell_slots[level]:
           print("No spell slot available!")
           return False
        
        self.spell_slots[level] -= 1
        return True


class Companion(Character):
    
    def __init__(self, name, charclass=CharClass, race=Race, level=int, ability_scores=dict):
        
        self.name = name
        self.charclass: CharClass = charclass
        self.race: Race = race
        self.level: int = level
        self.ability_scores: dict = ability_scores
        self.spell_slots: dict = spell_slot_counts[class_caster_types[charclass]][level]
        # self.subclass = subclass
        # self.subrace = subrace
        
        self.max_hp: int = int(base_hp[charclass] + ((level - 1) * (base_hp[charclass] / 2 + 1)))
        self.current_hp: int = self.max_hp
        
        self.armor_class: int = base_armor_class[self.charclass]
        self.actions: list = base_actions[self.charclass]

        # self.equipment = base_equipment[self.charclass]

        self.lastAttack_isMelee: bool = False
        

    def get_aggro(self):
        
        # I want aggro to work kind of like raffle tickets. Party members will have a self.aggro / total party aggro chance to be attacked
        # Maybe dead characters will get 0 aggro so they aren't multi-attacked?

        aggro = 1

        if self.lastAttack_isMelee:
            aggro += 2
        if self.charclass == CharClass.barbarian:
            aggro += 2
        
        return aggro
    
    
class Monster(Character):
    
    def __init__(self, name=str, enemytype=EnemyType, max_hp=int, armor_class=int, actions=list, ability_scores=dict, spell_slots=dict):
        
        self.name = name
        self.enemytype: CharClass = enemytype
        
        self.max_hp: int = max_hp
        self.current_hp: int = self.max_hp
        self.armor_class: int = armor_class

        self.actions: list = actions

        self.ability_scores: dict = ability_scores
        if spell_slots:
            self.spell_slots: dict = spell_slots
        else:
            self.spell_slots: dict = empty_spell_slots
    
    def choose_enemy(self, enemies):
        
        aggro_raffle = []

        for char in enemies:
            for tix in range(char.get_aggro()):
                aggro_raffle.append(char)

        return choice(aggro_raffle)
    
    def choose_action(self):
        return choice(self.actions)