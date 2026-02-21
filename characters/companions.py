from tools.character import Character
from tools.enums import CharacterName, CharClass, Race

Astarion = Character(name=CharacterName.astarion.value, 
                     charclass=CharClass.rogue, 
                     race=Race.elf, 
                     level=1)
Gale = Character(name=CharacterName.gale.value, 
                charclass=CharClass.wizard, 
                race=Race.human, 
                level=1)
Karlach = Character(name=CharacterName.karlach.value, 
                    charclass=CharClass.barbarian, 
                    race=Race.tiefling, 
                    level=1)
Laezel = Character(name=CharacterName.laezel.value, 
                   charclass=CharClass.fighter, 
                   race=Race.githyanki, 
                   level=1)
Shadowheart = Character(name=CharacterName.shadowheart.value, 
                        charclass=CharClass.cleric, 
                        race=Race.half_elf, 
                        level=1)
Wyll = Character(name=CharacterName.wyll.value, 
                 charclass=CharClass.warlock, 
                 race=Race.human, 
                 level=1)