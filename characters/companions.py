from tools.character import Companion
from tools.enums import CharacterName, CharClass, Race

Astarion = Companion(name=CharacterName.astarion.value, 
                     charclass=CharClass.rogue, 
                     race=Race.elf, 
                     level=1)
Gale = Companion(name=CharacterName.gale.value, 
                charclass=CharClass.wizard, 
                race=Race.human, 
                level=1)
Karlach = Companion(name=CharacterName.karlach.value, 
                    charclass=CharClass.barbarian, 
                    race=Race.tiefling, 
                    level=1)
Laezel = Companion(name=CharacterName.laezel.value, 
                   charclass=CharClass.fighter, 
                   race=Race.githyanki, 
                   level=1)
Shadowheart = Companion(name=CharacterName.shadowheart.value, 
                        charclass=CharClass.cleric, 
                        race=Race.half_elf, 
                        level=1)
Wyll = Companion(name=CharacterName.wyll.value, 
                 charclass=CharClass.warlock, 
                 race=Race.human, 
                 level=1)