from random import choice, randint
from actions.action import PassAction
from actions.buff_debuff import Buff
from tools.menu import menu
from tools.rich_capitalize import rich_capitalize
from tools.enums import CharClass, Race, AbilityScore, CharacterType
from tools.defaults import base_max_hp, base_armor_class, base_actions, class_caster_types, spell_slot_counts, empty_spell_slots
from rich import print

class Character():

    def __init__(self, 
        
        name, 
        character_type=CharacterType, 
        charclass=CharClass, 
        race=Race, 
        level=int, 
        ability_scores=dict, 

        spell_slots=dict,
        base_hp=int,
        max_hp=int, 
        armor_class=int, 
        extra_actions=list,

    ):
        
        # I'm sorry this is disgusting

        self.name = name

        self.character_type: CharacterType = character_type
        self.charclass: CharClass = charclass
        self.race: Race = race
        self.ability_scores: dict = ability_scores
        self.proficiency_bonus: int = 2

        # Level
        if level != int:
            self.level: int = level
        else: 
            self.level: int = 1
        
        # hp
        if max_hp != int:
            self.max_hp: int = max_hp
        elif base_hp != int:
            self.max_hp: int = base_hp + round(base_max_hp[charclass] * ((randint(0,15)) / 100) * choice([-1, 1])) # +/- 15% of base_hp
        else: 
            if character_type == CharacterType.companion:
                self.max_hp: int = int(base_max_hp[charclass] + (level * self.ability_scores[AbilityScore.CON]) + ((level - 1) * (base_max_hp[charclass] / 2 + 1)))
            elif character_type == CharacterType.monster:
                self.max_hp: int = base_max_hp[charclass] + round(base_max_hp[charclass] * ((randint(0,15)) / 100) * choice([-1, 1])) # +/- 15% of base_max_hp
            else:
                print("Invalid character type!")
                self.max_hp: int = 1
        self.current_hp: int = self.max_hp
        
        # AC
        if armor_class != int:
            self.armor_class: int = armor_class
        else: 
            if self.charclass in base_armor_class:
                self.armor_class: int = base_armor_class[self.charclass]
            else:
                self.armor_class: int = 10 + self.ability_scores[AbilityScore.DEX]
        
        # Actions
        self.actions: list = []
        if self.charclass in base_actions:
            self.actions: list = base_actions[self.charclass]
        if extra_actions != list:
            self.actions += extra_actions
             
        # Spell slots
        if spell_slots != dict:
            self.spell_slots: dict = spell_slots
        else:
            if character_type == CharacterType.companion:
                self.spell_slots: dict = dict(spell_slot_counts[class_caster_types[charclass]][level])
            else:
                self.spell_slots = dict(empty_spell_slots)

        # self.equipment = base_equipment[self.charclass]

        self.conditions: list = []
        self.lastAttack_isMelee: bool = False

        # Saving other input for resets
        self.base_hp = base_hp

    def __repr__(self):
        if self.character_type == CharacterType.companion:
            return "[bold yellow]" + str(self.name) + "[/bold yellow]"
        if self.character_type == CharacterType.monster:
            return "[bold red]" + str(self.name) + "[/bold red]"
        return "[bold]" + str(self.name) + "[/bold]"
    
    def reset(self):
        if self.character_type == CharacterType.companion:
                self.max_hp: int = int(base_max_hp[self.charclass] + (self.level * self.ability_scores[AbilityScore.CON]) + ((self.level - 1) * (base_max_hp[self.charclass] / 2 + 1)))
        elif self.character_type == CharacterType.monster:
            self.max_hp: int = base_max_hp[self.charclass] + round(base_max_hp[self.charclass] * ((randint(0,15)) / 100) * choice([-1, 1])) # +/- 15% of base_hp
        else:
            print("Invalid character type!")
            self.max_hp: int = 1
        self.current_hp: int = self.max_hp
    
    def action(self, enemies=list, team=list, fighters=list):
        
        action_choice = self.choose_action()
        
        # Doing action
        if self.character_type == CharacterType.companion:
            self, enemies, team = action_choice.action(character=self, enemies=enemies, team=team, fighters=fighters)
        elif self.character_type == CharacterType.monster:
            self, team, enemies = action_choice.action(character=self, enemies=team, team=enemies, fighters=fighters)
        else:
            print("Error: unacceptable character type!")
        
        # Removing dead characters
        for char in enemies:
            if char.current_hp <= 0:
                enemies.remove(char)
        for char in team:
            if char.current_hp <= 0:
                team.remove(char)
        
        return enemies, team, fighters
    
    def choose_action(self):
        
        action_options = []

        for act in self.actions:
            if act.spell_slot_level > 0 and self.spell_slots == empty_spell_slots:
                continue
            if type(act) == Buff:
                if act.targetSelf and act.condition in self.conditions:
                    continue
            action_options.append(act)
        
        action_options.append(PassAction)

        if len(action_options) == 1:
            return action_options[0]

        if self.character_type == CharacterType.monster:
            return choice(action_options)
        return menu(action_options, f"\nWhat would {str(self)} like to do?")
    
    def choose_enemy(self, enemies):
        
        if self.character_type == CharacterType.monster:
            aggro_raffle = []

            for char in enemies:
                for tix in range(char.get_aggro()):
                    aggro_raffle.append(char)

            return choice(aggro_raffle)

        if len(enemies) > 1:
            return menu(enemies, f"\nWho would {str(self)} like to attack?", show_hp=True)
        else:
            return enemies[0]

    def take_damage(self, damage):
        
        if damage:
            
            for cond in self.conditions:
                damage = cond.reduce_damage(damage)

            self.current_hp -= damage

            if self.current_hp <= 0:
                self.current_hp = 0
                print(f"{self.name} has died!")

            else:
                print(f"{rich_capitalize(self)} has {self.current_hp} health remaining.")
        
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

    def cast_leveled_spell(self, spell_level):
        if not self.spell_slots[spell_level]:
           print("No spell slot available!")
           return False
        
        self.spell_slots[spell_level] -= 1
        return True
    
    def get_actions(self):
        pass

    def get_aggro(self):

        aggro = 1

        if self.lastAttack_isMelee:
            aggro += 2
        if self.charclass == CharClass.barbarian:
            aggro += 2
        
        return aggro
    
    def roll_initiative(self):
        return randint(1,20) + self.ability_scores[AbilityScore.DEX]