import os
from tools.character import Companion
from tools.enums import AbilityScore, CharClass, Race
from tools.menu import menu


character_save_path = 'saved_characters/'


def save_character(character):
    
    file_name = "character_" + str(character.name) + ".txt"
    complete_fileName = os.path.join(character_save_path, file_name)
    character_file = open(complete_fileName, "w")

    character_data = {
        "name": str(character.name),
        "charclass": str(character.charclass),
        "race": str(character.race),
        "level": str(character.level),
        "ability_scores": {
            "STR": character.ability_scores[AbilityScore.STR],
            "DEX": character.ability_scores[AbilityScore.DEX],
            "CON": character.ability_scores[AbilityScore.CON],
            "INT": character.ability_scores[AbilityScore.INT],
            "WIS": character.ability_scores[AbilityScore.WIS],
            "CHA": character.ability_scores[AbilityScore.CHA],
        },
    }
    
    file_text = ""

    for data_category in character_data:
        if data_category != "ability_scores":
            file_text += f"{data_category}: {character_data[data_category]}\n"
        else:
            file_text += "ability_scores:\n"
            for score in character_data[data_category]: 
                file_text += f"- {score}: {character_data[data_category][score]}\n"
    
    character_file.write(file_text)
    character_file.close()


def load_character():
    
    # Get save files
    save_files = os.scandir(character_save_path)
    saved_characters = {}

    for entry in save_files:
        if entry.is_dir() or entry.is_file():
            saved_characters.update({str(entry.name).lstrip("character_").rstrip(".txt"): entry.name})
    save_files.close()
    
    if not saved_characters:
        print('You have no readable saves!')
        return None

    # Get data from chosen save
    selectedCharacter_fileName = saved_characters[menu(list(saved_characters), "Select character to load: ")]
    completeFileName = character_save_path + selectedCharacter_fileName

    character_file = open(completeFileName, "r")
    file_text = character_file.readlines()

    # Translating character data to dict
    character_data ={}
    for line in list(file_text):
        data_set = line.rstrip("\n").split(': ')
        file_text.remove(line)
        
        if 'ability_scores' in line:
            break

        data_type = data_set[0]
        if data_set[1] in list(characterData_translation):
            datum = characterData_translation[data_set[1]]
        else:
            datum = data_set[1]
        
        character_data.update({data_type: datum})
    
    ability_scores = {}
    for line in list(file_text):
        data_set = line.rstrip("\n").lstrip('- ').split(': ')
        file_text.remove(line)
        
        data_type = characterData_translation[data_set[0]]
        datum = int(data_set[1])

        ability_scores.update({data_type: datum})
    
    character_data.update({'ability_scores': ability_scores})
    
    return Companion(name=character_data['name'], charclass=character_data['charclass'], race=character_data['race'], level=int(character_data['level']), ability_scores=character_data['ability_scores'])

characterData_translation = {

    # Race
    "dragonborn": Race.dragonborn,
    "dwarf": Race.dwarf,
    "elf": Race.elf,
    "githyanki": Race.githyanki,
    "gnome": Race.gnome,
    "half-elf": Race.half_elf,
    "half_orc": Race.half_orc,
    "halfling": Race.halfling,
    "human": Race.human,
    "tiefling": Race.tiefling,

    # Class
    "barbarian": CharClass.barbarian,
    "bard": CharClass.bard,
    "cleric": CharClass.cleric,
    "druid": CharClass.druid,
    "fighter": CharClass.fighter,
    "monk": CharClass.monk,
    "paladin": CharClass.paladin,
    "ranger": CharClass.ranger,
    "rogue": CharClass.rogue,
    "sorcerer": CharClass.sorcerer,
    "warlock": CharClass.warlock,
    "wizard": CharClass.wizard,

    # Abiility Score
    "STR": AbilityScore.STR, 
    "DEX": AbilityScore.DEX, 
    "CON": AbilityScore.CON, 
    "INT": AbilityScore.INT, 
    "WIS": AbilityScore.WIS, 
    "CHA": AbilityScore.CHA, 

}