from os import path, scandir, makedirs
from pickle import dump, load, HIGHEST_PROTOCOL
from tools.menu import menu
from rich import print

character_save_path = 'characters/saved_characters/'


def save_character(character):
    
    file_name = "character_" + str(character.name) + ".pkl"
    complete_fileName = path.join(character_save_path, file_name)

    if not path.exists(character_save_path):
        makedirs(character_save_path)

    with open(complete_fileName, 'wb') as character_file:
        dump(character, character_file, protocol=HIGHEST_PROTOCOL)
        character_file.close()
    
    print("Character successfully saved!")


def load_character():
    
    # Get save files
    if not path.exists(character_save_path):
        makedirs(character_save_path)
    save_files = scandir(character_save_path)
    saved_characters = {}

    for entry in save_files:
        if entry.is_dir() or entry.is_file():
            saved_characters.update({str(entry.name).lstrip("character_").replace(".pkl",""): entry.name})
    save_files.close()
    
    if not saved_characters:
        print('You have no readable saves!')
        return None

    # Get data from chosen save
    selectedCharacter_fileName = saved_characters[menu(list(saved_characters), "Select character to load: ")]
    complete_fileName = character_save_path + selectedCharacter_fileName

    with open(complete_fileName, 'rb') as character_file:
        character = load(character_file)
        character_file.close
    
    print("Character successfully loaded!")
    return character