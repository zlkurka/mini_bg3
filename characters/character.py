from random import choice, randint
from actions.action import PassAction
from actions.attacks import RogueSneakAttack
from actions.buff_debuff import Buff, Hide
from actions.heal import Heal
from conditions.condition import Hiding, conditions_removed_on_action
from tools.menu import menu
from tools.roll_d20 import roll_d20
from tools.rich_capitalize import rich_capitalize
from tools.enums import CharClass, Race, AbilityScore, CharacterType, MenuOptions, Weapon, BuffCondition, Skill
from tools.defaults import base_max_hp, base_armor_class, base_actions, class_caster_types, spell_slot_counts, empty_spell_slots, skill_ability_scores
from rich import print

class Character():

    def __init__(self, 
        
        name, 
        character_type: CharacterType = CharacterType.monster, 
        charclass: CharClass = None, 
        race: Race = None, 
        level: int = 1, 
        ability_scores: dict = {
            AbilityScore.STR: 0,
            AbilityScore.DEX: 0,
            AbilityScore.CON: 0,
            AbilityScore.INT: 0,
            AbilityScore.WIS: 0,
            AbilityScore.CHA: 0,
        }, 
        skills: list = [],
        spell_slots: dict = None,
        base_hp: int = None,
        max_hp: int = None, 
        armor_class: int = None, 
        extra_actions: list = [],

    ):
        
        # I'm sorry this is disgusting

        self.name = name
        self.character_type: CharacterType = character_type
        self.charclass: CharClass = charclass
        self.race: Race = race
        self.ability_scores: dict = ability_scores
        self.skills: list = skills
        self.proficiency_bonus: int = 2
        self.level: int = level
        
        # hp
        if max_hp:
            self.max_hp: int = max_hp
        elif base_hp:
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
        if armor_class:
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
        self.actions += extra_actions
             
        # Spell slots
        if spell_slots:
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

    def __repr__(self) -> str:
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
    
    def action(self, enemies: list, team: list, fighters: list) -> tuple:

        while True:
            action_choice = self.choose_action(enemies=enemies, team=team)
            self, enemies, team, nevermindSelected = action_choice.action(character=self, enemies=enemies, team=team, fighters=fighters)
            if not nevermindSelected:
                break
        
        if action_choice != PassAction:
            for cond in self.conditions:
                if cond in conditions_removed_on_action:
                    try: 
                        if cond != action_choice.condition:
                            self.conditions.remove(cond)
                    except AttributeError:
                        self.conditions.remove(cond)
                    

        # Removing dead characters
        for char in enemies:
            if char.current_hp <= 0:
                enemies.remove(char)
        for char in team:
            if char.current_hp <= 0:
                team.remove(char)
        
        return enemies, team, fighters
    
    def choose_action(self, enemies: list, team: list):
        
        action_options = []

        for act in self.actions:
            
            # If no spell slots for leveled spell
            if act.spell_slot_level > 0 and self.spell_slots == empty_spell_slots:
                continue
            
            # If char already has self buff condition
            if type(act) == Buff:
                if act.targetSelf and act.condition in self.conditions:
                    continue
            
            # If sneak attack but not hiding
            if (act == RogueSneakAttack) and (Hiding not in self.conditions):
                continue
            
            # If heal but all allies have max hp
            if type(act) == Heal:
                team_missing_hp = 0
                for char in team:
                    team_missing_hp += char.max_hp - char.current_hp
                if team_missing_hp <= 0:
                    continue
            
            action_options.append(act)
        
        if self.character_type == CharacterType.companion:
            action_options.extend([Hide, PassAction])

        if self.character_type == CharacterType.monster:
            return choice(action_options)
        
        return menu(action_options, f"What would {str(self)} like to do?", show_spell_level=True)
    
    def choose_target(self, targets, action):
        
        possible_targets = list(targets)
        for char in possible_targets:
            if Hiding in char.conditions:
                possible_targets.remove(char)
        
        if len(possible_targets) == 0:
            print(f"{str(self)} was unable to target anyone.")
            return None
        if len(possible_targets) == 1:
            return possible_targets[0]

        if self.character_type == CharacterType.monster:
            aggro_raffle = []

            for char in possible_targets:
                for tix in range(char.get_aggro()):
                    aggro_raffle.append(char)

            return choice(aggro_raffle)

        options = possible_targets + [MenuOptions.nevermind]
        return menu(options, f"Who would {str(self)} like to target with {action}?", show_hp=True)

    def take_damage(self, damage: int = 0):
        
        if damage:
            
            for cond in self.conditions:
                damage = cond.reduce_damage(damage, self)

            self.current_hp -= damage

            if self.current_hp <= 0:
                self.current_hp = 0
                print(f"{self.name} has died!")

            else:
                print(f"{rich_capitalize(self)} has {self.current_hp} health remaining.")
        
        else:
            print("No damage dealt.")
    
    def heal(self, heal_amount: int = 0):
        
        if heal_amount > 0:
            
            if self.current_hp + heal_amount > self.max_hp:
                heal_amount = self.max_hp - self.current_hp
                self.current_hp = self.max_hp
            else:
                self.current_hp += heal_amount

            print(f"{str(self.name).capitalize()} was healed for {heal_amount} HP and now has {self.current_hp} HP.")
    
    def ability_check(self, ability_type, difficulty_class: int = None):
        
        # Get ability bonus
        ability_bonus = 0
        if type(ability_type) == Skill:
            if ability_type in self.skills:
                ability_bonus += self.proficiency_bonus
            ability_bonus += self.ability_scores[skill_ability_scores[ability_type]]
        elif type(ability_type) == AbilityScore:
            ability_bonus += self.ability_scores[ability_type]
        else:
            print("Unacceptable ability type!")

        # Roll
        roll = roll_d20(character=self, roll_bonus=ability_bonus)
        if difficulty_class == None:
            return roll
        # If no difficulty class set, returns roll (int)
        
        # Check successful
        checkSuccessful = roll >= difficulty_class
        print(f"{self} rolled a {roll} and ", end="")
        if checkSuccessful:
            print("succeeded!")
        else:
            print("failed.")
        
        return checkSuccessful

    def cast_leveled_spell(self, spell_level: int) -> bool:
        if not self.spell_slots[spell_level]:
           print("No spell slot available!")
           return False
        
        self.spell_slots[spell_level] -= 1
        return True
    
    def get_aggro(self) -> int:

        aggro = 1

        if self.lastAttack_isMelee:
            aggro += 2
        if self.charclass == CharClass.barbarian:
            aggro += 2
        
        return aggro
    
    def long_rest(self):
        self.current_hp: int = self.max_hp
        self.spell_slots: dict = dict(spell_slot_counts[class_caster_types[self.charclass]][self.level])