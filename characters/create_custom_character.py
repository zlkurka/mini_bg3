from characters.character import Character
from copy import deepcopy
from tools.enums import CharacterType
from tools.menu import menu
from tools.defaults import char_classes, char_races, ability_scores, base_skill_options, base_skill_choice_number
from tools.save_handler import load_character, save_character

def create_custom_character():

    match menu(['Create character','Load character'], "Would you like to create a new character or load a pre-existing one?"):
        case 'Create character':
            pass
        case 'Load character':
            loaded_character = load_character()
            if loaded_character:
                return loaded_character
        case _: 
            print("Invalid option!")
            return None
    
    custom_character_name = input("Enter your character's name: ")
    custom_character_charclass = menu(char_classes, "Select your character's class.")
    custom_character_race = menu(char_races, "Select your character's race.")
    custom_character_level = 1

    # Ability scores
    custom_character_ability_scores = {}
    standard_array_scores = [3, 2, 1, 0, 0, -1]
    for score in ability_scores:
        score_assigned = menu(standard_array_scores, f"What score would you like to assign to {score}?")
        standard_array_scores.remove(score_assigned)
        custom_character_ability_scores.update({score: score_assigned})
    
    # Skills
    custom_character_skills = []
    skill_options = deepcopy(base_skill_options[custom_character_charclass])
    for skill in range(base_skill_choice_number[custom_character_charclass]):
        skill_choice = menu(menu_text=f"What skill should {custom_character_name} have? ({skill} remaining.)", options=skill_options)
        custom_character_skills.append(skill_choice)
        skill_options.remove(skill_choice)
    
    # Create character
    custom_character = Character(
        name=custom_character_name, 
        character_type=CharacterType.companion, 
        charclass=custom_character_charclass, 
        race=custom_character_race, 
        level=custom_character_level, 
        ability_scores=custom_character_ability_scores
    )
    
    match menu(['Yes', 'No'], "Would you like to save this character?"):
        case 'Yes':
            save_character(custom_character)
        case 'No':
            pass
        case _:
            print('Invalid option!')

    return custom_character

if __name__ == "__main__":
    create_custom_character()