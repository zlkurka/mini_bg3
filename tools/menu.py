from string import ascii_uppercase
from rich import print
from tools.rich_capitalize import rich_capitalize
from tools.enums import Skill, AbilityScore

def menu(options: list, menu_text: str, show_race: bool = False, show_class: bool = False, show_hp: bool = False, show_spell_level: bool = False, show_uses_left: bool = False, show_item_type: bool = False, show_ability_check_and_difficulty_class: bool = False, character = None):

    # Acceptable list item types:
        # str
        # Enum child class
        # int
        # float
        # Custom class or Enum with __repr__
    # List item types that would print but would be weird
        # array
        # tuple
        # dict
    
    # Multiple different types are acceptable!

    # Printing menu
    
    print(menu_text)
    for iter in range(len(options)):
        list_item = options[iter]

        print(f'{ascii_uppercase[iter]}) {rich_capitalize(list_item)}', end='')
        
        if show_race and show_class:
            try:
                print(f", {list_item.race} {list_item.charclass}", end='')
            except AttributeError:
                pass
        elif show_race:
            try:
                print(f", {list_item.race}", end='')
            except AttributeError:
                pass
        elif show_class:
            try:
                print(f", {list_item.char}", end='')
            except AttributeError:
                pass
        
        if show_hp:
            try:
                print(f", {list_item.current_hp} / {list_item.max_hp} HP", end='')
            except AttributeError:
                pass
        
        if show_spell_level:
            try:
                if list_item.spell_slot_level > 0:
                    print(f", level {list_item.spell_slot_level} spell", end='')
            except AttributeError:
                pass

        if show_uses_left:
            if not character:
                print("Character not known")
            try:
                if list_item in character.consumable_actions:
                    print(f", {character.consumable_actions[list_item]} uses left", end='')
                elif list_item.spell_slot_level:
                    print(f", {character.spell_slots[list_item.spell_slot_level]} spell slots left", end='')
            except AttributeError:
                pass
        
        if show_item_type:
            try:
                print(f", {list_item.item_type}", end='')
            except AttributeError:
                pass
        
        while True:
            if show_ability_check_and_difficulty_class:
                try:
                    if list_item.ability_check and list_item.difficulty_class:
                        print(f" [{rich_capitalize(list_item.ability_check)} ({skill_ability_scores[list_item.ability_check]}), DC {list_item.difficulty_class}]", end='')
                        break
                except AttributeError:
                    pass
                try:
                    if list_item.ability_check:
                        print(f" ({rich_capitalize(list_item.ability_check)})", end='')
                        break
                except AttributeError:
                    pass
                try:
                    if list_item.difficulty_class:
                        print(f" (DC {list_item.difficulty_class})", end='')
                        break
                except AttributeError:
                    pass
            break

        print()
        # Will print like "A) Squid"

    # Taking input and translating to list item
    while True:

        selection = input().upper().strip()

        if selection not in list(ascii_uppercase):
            print('Invalid input! Enter only the letter corresponding to your selection.')
            continue
        
        if list(ascii_uppercase).index(selection) > len(options) - 1:
            print('Invalid input! This letter does not correspond to an option.')
            continue
        
        return options[list(ascii_uppercase).index(selection)]
    
skill_ability_scores: dict = {

    # Strength
    Skill.athletics: "STR",
    
    # Dexterity
    Skill.acrobatics: "DEX",
    Skill.initiative: "DEX",
    Skill.sleight_of_hand: "DEX",
    Skill.stealth: "DEX",
    
    # Intelligence
    Skill.arcana: "INT",
    Skill.history: "INT",
    Skill.investigation: "INT",
    Skill.nature: "INT",
    Skill.religion: "INT",

    # Wisdom
    Skill.animal_handling: "WIS",
    Skill.insight: "WIS",
    Skill.medicine: "WIS",
    Skill.perception: "WIS",
    Skill.survival: "WIS",

    # Charisma
    Skill.deception: "CHA",
    Skill.intimidation: "CHA",
    Skill.performance: "CHA",
    Skill.persuasion: "CHA",

}