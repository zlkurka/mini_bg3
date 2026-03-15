from random import choice, randint
from tools.menu import menu
from tools.enums import CharClass, Race, AbilityScore, CharacterType
from tools.defaults import base_hp, base_armor_class, base_actions, class_caster_types, spell_slot_counts, empty_spell_slots

class Character():
    
    def __init__(self, 
        
        name, 
        character_type=CharacterType, 
        charclass=CharClass, 
        race=Race, 
        level=int, 
        ability_scores=dict, 

        spell_slots=dict,
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

        # Level
        if level != int:
            self.level: int = level
        else: 
            self.level: int = 1
        
        # hp
        if max_hp != int:
            self.max_hp: int = max_hp
        else: 
            if character_type == CharacterType.companion:
                self.max_hp: int = int(base_hp[charclass] + (level * self.ability_scores[AbilityScore.CON]) + ((level - 1) * (base_hp[charclass] / 2 + 1)))
            elif character_type == CharacterType.monster:
                self.max_hp = base_hp[charclass] + round(base_hp[charclass] * ((randint(0,15)) / 100) * choice([-1, 1])) # +/- 15% of base_hp
            else:
                while True:
                    try:
                        self.max_hp = int(input("Unable to get max_hp. What should this character's max_hp be? ").strip())
                        break
                    except:
                        print("Invalid input!")
        self.current_hp: int = self.max_hp
        
        # AC
        if armor_class != int:
            self.armor_class: int = armor_class
        else: 
            self.armor_class: int = base_armor_class[self.charclass]
        
        # Actions
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

        self.lastAttack_isMelee: bool = False

    def __repr__(self):
        return str(self.name)
    
    def action(self, enemies=list, team=list, skipped_fighters=list):
        
        # Choosing action
        if len(self.actions) > 1:
            action_choice = self.choose_action()
        else:
           action_choice = self.actions[0]
        
        # Doing action
        if self.character_type == CharacterType.companion:
            self, enemies, team = action_choice.action(character=self, enemies=enemies, team=team)
        elif self.character_type == CharacterType.monster:
            self, team, enemies = action_choice.action(character=self, enemies=team, team=enemies)
        else:
            print("Error: unacceptable character type!")
        
        # Removing dead characters
        for char in enemies:
            if char.current_hp <= 0:
                skipped_fighters.append(char)
                enemies.remove(char)
        for char in team:
            if char.current_hp <= 0:
                skipped_fighters.append(char)
                team.remove(char)
        
        return enemies, team, skipped_fighters
    
    def choose_action(self):
        
        action_options = list(self.actions)

        for act in self.actions:
            if act.spell_slot_level > 0 and self.spell_slots == empty_spell_slots:
                action_options.remove(act)

        if self.character_type == CharacterType.monster:
            return choice(action_options)
        return menu(action_options, f"\nWhat would {self.name} like to do?")
    
    def choose_enemy(self, enemies):
        
        if self.character_type == CharacterType.monster:
            aggro_raffle = []

            for char in enemies:
                for tix in range(char.get_aggro()):
                    aggro_raffle.append(char)

            return choice(aggro_raffle)

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

    def cast_leveled_spell(self, spell_level):
        if not self.spell_slots[spell_level]:
           print("No spell slot available!")
           return False
        
        self.spell_slots[spell_level] -= 1
        return True
    
    def get_aggro(self):

        aggro = 1

        if self.lastAttack_isMelee:
            aggro += 2
        if self.charclass == CharClass.barbarian:
            aggro += 2
        
        return aggro