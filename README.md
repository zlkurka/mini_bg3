This is a simple, terminal-based game inspired by *Dungeons and Dragons 5e* and *Baldur's Gate 3*. You can choose characters to fight alongside or build your own and battle different groups of monsters.

I plan on adding a dungeon-crawler component and potentially RPG elements. My end vision is a procedurally generated dungeon crawler (layout inspired by *The Binding of Isaac*) that gets more difficult the further you move from the starting room, and  *Slay the Spire*-inspired rooms (combat and events).

# How to play

This program can be run in a few different ways, none of which are particularly straightforward unfortunately (hoping to find a solution soon). Here are a few different ways:


## Using an IDE

- Download this repository. I will have releases soon where you can download it.
- If you already have an IDE like VS Code installed, this will be your easiest choice. 
- Make sure you have Python installed on your computer and have an extension to execute Python code in your IDE
- Open this project's root folder in your IDE. Navigate to `main.py`
- Execute the code in `main.py`


## From your computer's terminal

- Download this repository. I will have releases soon where you can download it.
- Make sure you have Python installed on your computer.
- Copy the path to `main.py` in your file navigation system
- Enter `python` into your terminal (`python3` on Mac I believe), and paste the path to the file before hitting enter
  - Example: `python users/name/Downloads/mini_bg3/main.py`


# To-do's


## Class-specific features
- Rogue: Sneak attack
- Barbarian: rage
- Druid: wildshape
- Bard: inspo
- Cleric: healing cantrip


## 1st lvl spells

### Priority
  - Magic missile
  - Mage armor
  - Guiding bolt
  - Find familiar
  
### Add later
  - Armor of agathys
  - Witch bolt
  - Bless
  - Sleep
  - Hunter's mark
  - Shield
  - Ensnaring strike


## Monsters

### New monsters
- Giant spider
- Goblin variants (warrior, archer, mage, healer); randomly sampled in goblin fight

### New combat styles
- Tactical levels: some enemies are smarter than others and will try to target squishier party members and healers


## Magic items

### Potions
For now, I think it's simplest to have characters only be able to use potions on themselves? If I had an action economy I could make it more expensive to use it on others...
- Healing potion (each character gets one per combat)

## Game concept, story, and characters

### Concept
Dungeon crawler (roguelike?)
- Isaac-style room mapping- start from the dungeon's entrance. Can move from a cleared room to any adjacent room. If you enter an uncleared room, you will encounter a fight or an event (e.g., a trap or puzzle).
- Along the way, you find new companions, magic items, and, of course, gold

### Characters

#### Companions
I currently use all the companions from *Baldur's Gate 3*, but if this becomes legit, I want to have non-licensed characters.
- **Nightkill**: A halfling teenager turned emo rogue. She ran off from her parents who don't understand her and wound up in a dungeon.
- **Faylen**: A half-elf druid and cult escapee.
- A runaway goblin (wizard?). 

#### Monsters
- A party of goblins led by a hobgoblin are prowling the dungeons looking for a runaway- and maybe some treasure while they're there. Watch out for their bugbear warrior!


## Other features
- Add Nevermind to action targeting
- Add equipment; auto-equip during __init__
- Add visual combat in Godot
- Add race features
- Add action economy (action, bonus action, reaction, movement?)
- Add reviving dead characters (Withers, spend gold; revivify)
- Add higher levels
  - Spell casters are reassigned spell slots with base_spell_slots[casterType][level]

# Copyright statement
© 2026 Zoey Kurka. All rights reserved.