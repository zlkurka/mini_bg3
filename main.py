from tools.menu import menu
from characters.companions import Astarion, Gale, Karlach, Laezel, Shadowheart, Wyll
from tools.enums import CharacterName, Encounter
from random import shuffle
from tools.character import Character, Enemy
from characters.enemies import get_enemies

def main():
    
    DEV_MODE = False

    alt_companions = [CharacterName.astarion, CharacterName.gale, CharacterName.karlach, CharacterName.laezel, CharacterName.shadowheart, CharacterName.wyll] 
    companions = [Astarion, Gale, Karlach, Laezel, Shadowheart, Wyll] 
    
    if DEV_MODE:
        
        alt_party = [CharacterName.astarion, CharacterName.gale, CharacterName.karlach, CharacterName.shadowheart] 
        party = [Wyll, Gale, Karlach, Laezel]
        encounter = Encounter.goblins_4x
    
    else:
        
        party = pick_party(companions)
        encounter = menu([Encounter.goblins_4x, Encounter.owlbear], "Who would you like to fight?")

    party = combat(party, encounter)


def combat(party=list, encounter=Encounter):
    
    enemies = get_enemies(encounter)
    original_party = list(party)

    # Initiative
    fighters = party + enemies
    shuffle(fighters)
    
    print("\nInitiative: ")
    for fighter in fighters:
        print("- " + fighter.name.capitalize())
    
    initiative = 0
    skipped_fighters = []
    
    # Combat
    while True:
        
        fighter = fighters[initiative]

        initiative += 1
        if initiative >= len(fighters):
            initiative = 0

        if fighter in skipped_fighters:
            continue

        if type(fighter) == Character:
            damage, enemy_hit = fighter.attack(enemies)
            if enemy_hit.take_damage(damage):
                enemies.remove(enemy_hit)
                skipped_fighters.append(enemy_hit)


        if type(fighter) == Enemy:
            damage, enemy_hit = fighter.attack(party)
            if enemy_hit.take_damage(damage):
                party.remove(enemy_hit)
                skipped_fighters.append(enemy_hit)

        if not party:
            print("You lose!")
            return party
        if not enemies:
            print("You win!\n")

            for char in original_party:
                if char in party:
                    print(f"{char.name}: {char.current_hp} HP remaining.")
                else:
                    print(f"{char.name}: died in combat.")

            return party


def pick_party(companions=list):
    
    companions.append(None)
    party = []

    for x in range(4):
        
        while True:
            selection = menu(companions, f"Who would you like to in your party? ({4-x} slots remaining.)")
        
            if selection or party:
                break
            
            print("You must have at least one character in your party!")
        
        if not selection:
            break

        party.append(selection)
        companions.remove(selection)
    
    if len(party) == 1:
        print(f"You embark with {party[0].name}!")
        return party
    
    if len(party) == 2:
        print(f"You embark with {party[0].name} and {party[1].name}!")
        return party

    print("You embark with ", end="")
    for char in party:
        
        if (len(party) - 1) - party.index(char) >= 2:
            # e.g., member 0 or 1 of 4
            print(char.name, end=", ")
        
        if (len(party) - 1) - party.index(char) == 1:
            # e.g., member 2 of 3 or 3 of 4
            print(char.name, end=", and ")
        
        if (len(party) - 1) - party.index(char) == 0:
            # last member of party
            print(char.name, end="!\n")
    
    return party

main()