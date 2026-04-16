from encounters.combat.combat_class import Combat
from characters.monsters import *
from tools.enums import Encounter

Goblins_4x = Combat(
    name=Encounter.goblins_4x, 
    monsters=[Goblin], 
    rewards=[], 
    monster_names=goblin_names, 
    monster_sample_count=4,
    rare_monster=Bajesus,
    rare_monster_chance=10,
)
InjuredAdventurerFight = Combat(
    name="Fight the Injured Adventurer", 
    monsters=[InjuredAdventurer], 
    rewards=[],
)
MurderHoboFight = Combat(
    name="Fight the Murder Hobo", 
    monsters=[MurderHobo], 
    rewards=[],
)
OwlbearMother = Combat(
    name=Encounter.owlbear, 
    monsters=[Owlbear], 
    rewards=[],
)
UndeadGroup = Combat(
    name=Encounter.undead_group, 
    monsters=[Skeleton, Zombie], 
    rewards=[],
    monster_sample_count=4,
)
Training = Combat(
    name=Encounter.training_dummy, 
    monsters=[TrainingDummy], 
    rewards=[],
)