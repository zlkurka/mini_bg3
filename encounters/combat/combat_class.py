from characters.monsters import *
from conditions.condition_lists import conditions_removed_at_turn_end, conditions_removed_at_turn_start, conditions_removed_at_combat_end
from tools.enums import Skill, CharacterType
from tools.rich_capitalize import rich_capitalize
from random import shuffle, choice, sample, randint
from copy import deepcopy
from rich import print

class Combat():

    def __init__(
            self, 
            name, 
            description: str = "", 
            rewards: list = [], 
            
            monsters: list = [], 
            monster_names: list = [], 
            monster_sample_count: int = None, 
            rare_monster: Character = None, 
            rare_monster_chance: int = 0,
            
            allies: list = [], 
        ):
        
        self.name = name
        self.description: str = description
        self.rewards: list = list(rewards)
        self.allies: list = list(allies)

        # Getting monsters
        if monster_sample_count == None:
            self.monsters: list = list(monsters)
        else:
            self.monsters: list = []
            for iter in range(monster_sample_count):
                self.monsters.append(deepcopy(choice(monsters)).reset())
        
        # Applying monster names
        if monster_names:
            monster_name_options = sample(monster_names, len(self.monsters))
            for char in self.monsters:
                char.name = monster_name_options[self.monsters.index(char)]

        # Numbering enemies with duplicate names
        used_names = []
        for char in self.monsters: 
            if char.name in used_names:
                name_added_num = 2
                while True:
                    alt_name = str(char.name) + " " + str(name_added_num)
                    if alt_name in used_names:
                        name_added_num += 1
                        continue
                    char.name = alt_name
                    break
            used_names.append(char.name)

        # Adding rare monster
        if rare_monster:
            shuffle(self.monsters)
            if randint(1, 100) <= rare_monster_chance:
                self.monsters.pop(0)
                self.monsters.insert(0, rare_monster)
        
    def __repr__(self):
        return "[bold]" + str(self.name) + "[/bold]"

    def begin(self, party: list):
        print(str(self))
        if self.description:
            print("\n\n" + self.description + "\n")

        original_party = list(party)
        combat_party = list(party) + self.allies
        monsters = list(self.monsters)

        fighters = self.roll_initiative(fighters=(party + monsters + self.allies))
        initiative = 0
       
        while True:
        
            fighter = fighters[initiative]

            initiative += 1
            if initiative >= len(fighters):
                initiative = 0
            
            print()

            fighter_is_incapacitated = False
            for condition in fighter.conditions:
                if condition.incapacitated: 
                    fighter_is_incapacitated = True
                condition.ticking_health_alteration(fighter)
                if condition in conditions_removed_at_turn_start:
                    fighter.lose_condition(condition)
            
            if fighter_is_incapacitated or fighter.current_hp <= 0:
                continue

            # Do action
            if fighter.character_type == CharacterType.companion:
                monsters, combat_party, fighters = fighter.action(enemies=monsters, team=combat_party, fighters=fighters)
            elif fighter.character_type == CharacterType.monster:
                combat_party, monsters, fighters = fighter.action(enemies=combat_party, team=monsters, fighters=fighters)
            else:
                print("Error: unacceptable character type!")
                monsters, combat_party, fighters = fighter.action(enemies=monsters, team=combat_party, fighters=fighters)
            
            for condition in fighter.conditions:
                if condition in conditions_removed_at_turn_end:
                    fighter.lose_condition(condition)

            if not combat_party or not monsters:
                
                for char in combat_party:
                    for condition in char.conditions:
                        if condition in conditions_removed_at_combat_end:
                            char.lose_condition(condition)
                
                if not combat_party:
                    self.rewards = []
                
                if not monsters:
                    print("\nYou win!\n")

                    for char in original_party:
                        if char in combat_party:
                            print(f"{char.name}: {char.current_hp} HP remaining.")
                        else:
                            print(f"{char.name}: died in combat.")
                    
                    self.add_monsters_items_to_rewards()
            
                print()
                return self.rewards

    def roll_initiative(self, fighters: list):
        
        # Roll initiative
        initiative_rolls = {}
        for char in fighters:
            roll = char.ability_check(ability_type=Skill.initiative, print_feedback=False)
            if roll not in initiative_rolls:
                initiative_rolls.update({roll: [char]})
            else: 
                chars_at_initiative = initiative_rolls[roll]
                chars_at_initiative.append(char)
                initiative_rolls.update({roll: chars_at_initiative})
        
        fighters = list(initiative_rolls.keys())
        fighters.sort()
        fighters.reverse()

        for roll in list(fighters):
            chars = initiative_rolls[roll]
            if type(chars) != list:
                chars = [chars]
            else:
                shuffle(chars)
            for char in chars:
                fighters.append(char)
            fighters.remove(roll)

        # Print initiative
        print("\nInitiative: ")
        for fighter in fighters:
            print("- " + rich_capitalize(fighter))

        return fighters
    
    def add_monsters_items_to_rewards(self):
        for char in self.monsters:
            char.unequip_all(print_feedback=False)
            self.rewards.extend(char.items)