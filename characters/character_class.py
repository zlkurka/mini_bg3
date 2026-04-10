from random import choice, randint
from actions.action_class import PassAction
from actions.attacks.attacks import Attack, RogueSneakAttack
from actions.buff_debuff.buffs import Buff, Hide
from actions.heal.heal import Heal
from items.item_class import Item
from conditions.conditions import Hiding
from conditions.condition_lists import conditions_removed_on_action
from tools.menu import menu
from tools.roll_d20 import roll_d20
from tools.rich_capitalize import rich_capitalize
from tools.enums import CharClass, Race, AbilityScore, CharacterType, MenuOptions, Skill, ItemType, RollType
from tools.defaults import base_hp_charclass, base_armor_class, base_actions, class_caster_types, spell_slot_counts, empty_spell_slots, skill_ability_scores, class_spellcasting_ability_scores, base_consumable_actions, char_classes, empty_equipment, base_equipped_items
from rich import print
from copy import copy

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
        base_max_hp: int = None,
        max_hp: int = None, 
        armor_class: int = None, 
        actions: list = [],
        consumable_actions: dict = {},
        extra_actions: list = [],
        conditions: list = [],
        equipment: dict = empty_equipment,
        equipped_items: list = [],

    ):
        
        # I'm sorry this is disgusting

        self.name = name
        self.character_type: CharacterType = character_type
        self.charclass: CharClass = charclass
        self.race: Race = race
        self.ability_scores: dict = dict(ability_scores)
        self.skills: list = list(skills)
        self.proficiency_bonus: int = 2
        self.level: int = level
        
        # hp
        if max_hp:
            self.max_hp: int = max_hp
        elif base_max_hp:
            self.max_hp: int = base_max_hp + round(base_max_hp * ((randint(0,15)) / 100) * choice([-1, 1])) # +/- 15% of base_max_hp
        elif charclass in base_hp_charclass:
            self.max_hp: int = int(base_hp_charclass[charclass] + (level * self.ability_scores[AbilityScore.CON]) + ((level - 1) * (base_hp_charclass[charclass] / 2 + 1)))
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
        if actions:
            self.actions: list = list(actions)
        else:
            self.actions: list = []
            if self.charclass in base_actions:
                self.actions: list = base_actions[self.charclass]
            self.actions += list(extra_actions)
        
        # Set consumable actions
        self.consumable_actions: dict = dict(consumable_actions)
        if charclass in base_consumable_actions:
            self.consumable_actions.update(base_consumable_actions[charclass])
        for act in self.consumable_actions:
            val = self.consumable_actions[act]
            if type(val) == AbilityScore:
                self.consumable_actions.update({act: self.ability_scores[val]})

        # Spell slots
        if spell_slots:
            self.spell_slots: dict = spell_slots
        else:
            if character_type == CharacterType.companion:
                self.spell_slots: dict = dict(spell_slot_counts[class_caster_types[charclass]][level])
            else:
                self.spell_slots = dict(empty_spell_slots)

        # Equipment
        self.equipment: dict = dict(equipment)
        if not equipped_items and charclass in base_equipped_items:
            equipped_items = base_equipped_items[charclass]
        for item in equipped_items:
            self.equip_item(item, skip_if_slot_filled=True, print_feedback=False)

        self.conditions: list = list(conditions)
        self.lastAttack_isMelee: bool = False

        # For reset
        if base_max_hp:
            self.original_base_max_hp = base_max_hp
        else:
            self.original_base_max_hp = self.max_hp

    def __repr__(self) -> str:
        if self.character_type == CharacterType.companion:
            return "[bold yellow]" + str(self.name) + "[/bold yellow]"
        if self.character_type == CharacterType.monster:
            return "[bold red]" + str(self.name) + "[/bold red]"
        return "[bold]" + str(self.name) + "[/bold]"
    
    def reset(self):
        if self.character_type in base_hp_charclass:
                self.max_hp: int = int(base_hp_charclass[self.charclass] + (self.level * self.ability_scores[AbilityScore.CON]) + ((self.level - 1) * (base_hp_charclass[self.charclass] / 2 + 1)))
        elif self.original_base_max_hp:
            self.max_hp: int = self.original_base_max_hp + round(self.original_base_max_hp * ((randint(0,15)) / 100) * choice([-1, 1])) # +/- 15% of base_hp
        else:
            print("Invalid character type!")
            self.max_hp: int = 1
        self.current_hp: int = self.max_hp

        return self
    
    def action(self, enemies: list, team: list, fighters: list) -> tuple:

        while True:
            action_choice, action_is_consumable = self.choose_action(enemies=enemies, team=team)
            self, enemies, team, nevermindSelected = action_choice.action(character=self, enemies=enemies, team=team, fighters=fighters)
            if not nevermindSelected:
                break
        if action_is_consumable:
            if self.consumable_actions[action_choice] <=0:
                print("All out of uses for this action!")
            self.consumable_actions[action_choice] -= 1
        
        if action_choice != PassAction:
            for cond in self.conditions:
                if cond in conditions_removed_on_action:
                    try: 
                        if cond == action_choice.condition:
                            continue
                    except AttributeError:
                        pass
                    self.conditions.remove(cond)

        # Removing dead characters
        for char in enemies:
            if char.current_hp <= 0:
                enemies.remove(char)
        for char in team:
            if char.current_hp <= 0:
                team.remove(char)
        
        return enemies, team, fighters
    
    def choose_action(self, enemies: list, team: list) -> tuple:
        
        action_options = []
        consumable_action_set = False
        action_is_consumable = False
        for action_set in (self.actions, self.consumable_actions):
            for act in action_set:
                
                if consumable_action_set:
                    if self.consumable_actions[act] <= 0:
                        continue

                # If no spell slots for leveled spell
                if act.spell_slot_level > 0 and self.spell_slots == empty_spell_slots:
                    continue
                
                # If char already has self buff condition
                if type(act) == Buff:
                    if act.targetSelf and act.condition in self.conditions:
                        continue
                
                # If sneak attack but not hiding
                action_condition_met = True
                for cond in act.required_self_conditions:
                    if cond not in self.conditions:
                        action_condition_met = False
                        break
                if not action_condition_met:
                    continue
                
                # If heal but all allies have max hp
                if type(act) == Heal:
                    team_missing_hp = 0
                    for char in team:
                        team_missing_hp += char.max_hp - char.current_hp
                    if team_missing_hp <= 0:
                        continue
            
                action_options.append(act)
            consumable_action_set = True

        if self.character_type == CharacterType.companion:
            action_options.extend([Hide, PassAction])

        if self.character_type == CharacterType.monster:
            chosen_action = choice(action_options)
            return chosen_action, chosen_action in self.consumable_actions
        
        action_choice = menu(options=action_options, menu_text=f"What would {str(self)} like to do?", show_spell_level=True, show_uses_left=True, character=self)
        
        if action_choice in self.actions and action_choice in self.consumable_actions:
            match menu(options=["Regular version","Consumable version"], menu_text="You have two versions of this spell. Which would you like to use?"):
                case "Regular version":
                    pass
                case "Consumable version":
                    action_is_consumable = True
                case _:
                    print("Invalid option!")
        elif action_choice in self.consumable_actions:
            action_is_consumable = True

        return action_choice, action_is_consumable
    
    def choose_target(self, targets, action):
        
        target_options = list(targets)
        if len(target_options) == 0:
            print(f"{str(self)} was unable to target anyone.")
            return None

        for char in target_options:
            if char and Hiding in char.conditions:
                target_options.remove(char)
        
        if len(target_options) == 0:
            print(f"{str(self)} was unable to target anyone.")
            return None
        if len(target_options) == 1:
            return target_options[0]

        if self.character_type == CharacterType.monster:
            if type(action) == Attack:
                aggro_raffle = []

                for char in target_options:
                    for tix in range(char.get_aggro()):
                        aggro_raffle.append(char)

                return choice(aggro_raffle)
            return choice(targets)

        options = target_options + [MenuOptions.nevermind]
        return menu(options, f"Who would {str(self)} like to target with {action}?", show_hp=True)

    def take_damage(self, damage: int = 0) -> None:
        
        if damage:
            
            for cond in self.conditions:
                damage = cond.alter_incoming_damage(damage, self)

            self.current_hp -= damage

            if self.current_hp <= 0:
                self.current_hp = 0
                print(f"{rich_capitalize(self)} has died!")

            else:
                print(f"{rich_capitalize(self)} has {self.current_hp} health remaining.")
        
        else:
            print("No damage dealt.")
    
    def heal(self, heal_amount: int = 0) -> None:
        
        if heal_amount > 0:
            
            if self.current_hp + heal_amount > self.max_hp:
                heal_amount = self.max_hp - self.current_hp
                self.current_hp = self.max_hp
            else:
                self.current_hp += heal_amount

            print(f"{str(self.name).capitalize()} was healed for {heal_amount} HP and now has {self.current_hp} HP.")
    
    def gain_condition(self, condition) -> None:
        if condition not in self.conditions:
            print(f"{self} gained condition {condition}.")
            self.conditions.append(condition)

    def ability_check(self, ability_type, difficulty_class: int = None, print_feedback: bool = True) -> int | bool:
        
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
        roll = roll_d20(character=self, roll_bonus=ability_bonus, print_feedback=print_feedback, roll_type=RollType.ability_check)
        if difficulty_class == None:
            return roll
        # If no difficulty class set, returns roll (int)
        
        # Check successful
        checkSuccessful = roll >= difficulty_class
        if not print_feedback:
            return checkSuccessful
        print(f"{rich_capitalize(self)} rolled a {roll} and ", end="")
        if checkSuccessful:
            print("succeeded!")
        else:
            print("failed.")
        
        return checkSuccessful
    
    def get_modifier(self, ability_type, exclude_proficiency_bonus: bool = False) -> int:
        
        ability_bonus: int = 0

        if type(ability_type) == Skill:
            ability_bonus: int = self.ability_scores[skill_ability_scores[ability_type]]
            if ability_type in self.skills and not exclude_proficiency_bonus:
                ability_bonus += self.proficiency_bonus
        
        elif type(ability_type) == AbilityScore:
            
            if ability_type == AbilityScore.finesse:
                ability_bonus: int = max(self.ability_scores[AbilityScore.STR], self.ability_scores[AbilityScore.DEX])
            elif ability_type == AbilityScore.spellcasting:
                for ability in class_spellcasting_ability_scores:
                    if self.charclass in class_spellcasting_ability_scores[ability]:
                        ability_bonus: int = self.ability_scores[ability]
                        break
            else:
                ability_bonus: int = self.ability_scores[ability_type]
            
            if not exclude_proficiency_bonus:
                ability_bonus += self.proficiency_bonus
        
        else:
            print("Unacceptable ability type!")
        
        return ability_bonus
        
    def cast_leveled_spell(self, spell_level: int) -> bool:
        if not self.spell_slots[spell_level]:
           print("No spell slot available!")
           return False
        
        self.spell_slots[spell_level] -= 1
        return True
    
    def equip_item(self, item: Item = None, skip_if_slot_filled: bool = False, print_feedback: bool = True) -> Item:
        if not item or not item.is_equippable:
            return item
        
        for itm in self.equipment:
            if itm != item.item_type:
                continue
            if self.equipment[itm] and skip_if_slot_filled:
                if print_feedback:
                    print(f"Slot already filled by {self.equipment[itm]}.")
                return item
            removed_item = self.unequip_item(item=self.equipment[itm], print_feedback=print_feedback)
            self.equipment.update({item.item_type: item})
            if print_feedback:
                print(f"{self} equipped {item}.")
            break
        
        for act in item.associated_actions:
            if act not in self.actions:
                self.actions.append(act)
        
        return removed_item
    
    def unequip_item(self, item: Item = None, print_feedback: bool = True) -> Item:
        if not item:
            return item
        
        if not item.is_equippable:
            print("Item is not equippable, but will still be removed.")
        
        for itm in list(self.equipment):
            if item == self.equipment[itm]:
                removed_item = self.equipment.pop(itm)
                self.equipment.update({item.item_type: None})
                if print_feedback:
                    print(f"{self} unequipped {item}.")
        
        if removed_item:
            for act in removed_item.associated_actions:
                self.actions.remove(act)
                if print_feedback:
                    print(f"{self} lost action {act}.")
        
        return removed_item

    def unequip_all(self, print_feedback: bool = True) -> list:
        removed_items = []
        for item_type in self.equipment:
            if self.equipment[item_type]:
                removed_items.append(self.unequip_item(item=self.equipment[item_type], print_feedback=print_feedback))
        return removed_items

    def get_aggro(self) -> int:

        aggro = 1

        if self.lastAttack_isMelee:
            aggro += 2
        if self.charclass == CharClass.barbarian:
            aggro += 2
        
        return aggro
    
    def long_rest(self) -> None:
        self.current_hp: int = self.max_hp
        self.spell_slots: dict = dict(spell_slot_counts[class_caster_types[self.charclass]][self.level])