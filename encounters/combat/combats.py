from encounters.combat.combat_class import Combat
from characters.monsters import *
from characters.companions import Rattlebones
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
SwarmedByBeasts = Combat(
    name="Swarmed by Beasts", 
    description="You find yourself suddenly swarmed by snarling beasts. As they corner you, a crossbow bolt thunks into one's back. As it falls, you see a skeleton in a cowboy hat holding a shortsword in one hand and a hand crossbow in the other.",
    monsters=[], 
    allies=[Rattlebones],
    rewards=[Rattlebones],
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