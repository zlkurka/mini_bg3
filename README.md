This is a simple, terminal-based game inspired by *Dungeons and Dragons 5e* and *Baldur's Gate 3*. You can choose characters to fight alongside or build your own and battle different groups of monsters.

I only began learning Python a few months ago, and with it the ins and outs of computer stuff, so I apologize if some of my instructions are unclear, unoptimal, or don't work altogether. I also apologize that my code is disgusting, lol.

I plan on adding a dungeon-crawler component and potentially RPG elements. My end vision is a procedurally generated dungeon crawler (layout inspired by *The Binding of Isaac*) that gets more difficult the further you move from the starting room, and  *Slay the Spire*-inspired rooms (combat and events).




___

# How to play

Make sure you have Python 3.14 installed, along with Rich (use `pip install rich` or `python -m pip install rich`)

## Using executable

The game is executed from `main.exe` in the root project folder of the latest release. The executable was created using Pyinstaller, meaning that computers running different a operating system architectures from my own (Windows 11, 64 bit) may have trouble running it. If the .exe doesn't work, you can execute the code using your device's terminal or an installed IDE.

I’m working on a better way of making an exectuable, but I’m a beginner to software development and Python is a wacky language, so it’s taking some time.

## From your computer's terminal

* Download this repository. I will have releases soon where you can download it.
* Make sure you have Python installed on your computer.
* Copy the path to `main.py` in your file navigation system
* Enter `python` into your terminal (`python3` on Mac I believe), and paste the path to the file before hitting enter
  * Example: `python users/name/Downloads/mini_bg3/main.py`

## Using an IDE

* Download this repository. I will have releases soon where you can download it.
* If you already have an IDE like VS Code installed, this will be your easiest choice.
* Make sure you have Python installed on your computer and have an extension to execute Python code in your IDE
* Open this project's root folder in your IDE. Navigate to `main.py`
* Execute the code in `main.py`



___

# To-do's

## Priority

* Add armor and shields
* Add equipment management
* Add action economy (action, bonus action, reaction, movement?)
* Add buffs to events
* New monsters
* Druid spells

## Class-specific features

* Paladin: lay on hands
  * Can expend any amount from pool of 5 \* level
  * Removes poisoned condition
  * Bonus action
* Druid: wildshape (level 2?)

## 1st lvl spells

### Priority

* Magic missile
* Mage armor
* Guiding bolt
* Guidance
* Find familiar
  * Can be played automatically at the start of combat at the cost of a spell slot (or ability use for ranger)

### Add later

* Armor of agathys
* Witch bolt
* Bless
* Sleep
* Hunter's mark
* Shield
* Ensnaring strike

## Monsters

### New encounters

* Hobgoblin (with improved tactical targeting)
* Bugbear
* Goblin variants (warrior, archer, mage, healer); randomly sampled in goblin fight
* Giant spider
* Mimics
* Necromancer
  * Uses saves of two dead companion (or Tav/custom?) characters

### New combat styles

* Tactical levels: some enemies are smarter than others and will try to target squishier party members and healers

## Events

### Mimics

Either go for the big tantelizing chest and fight mimics for a cool item, or take something small

This feels kind of boring to experienced D&D players, who I think are my intended audience. It feels much more fun (and more like the silly events of STS2) to have, like, a whole room made of mimics. But that would probably be a higher-level encounter.

### Gelatinous Cube

## Magic items

### Potions

For now, I think it's simplest to have characters only be able to use potions on themselves? If I had an action economy I could make it more expensive to use it on others...

* Healing potion (each character gets one per combat)

## Game concept, story, and characters

### Concept

Dungeon crawler (roguelike?)

* *Binding of Isaac*-style room mapping- start from the dungeon's entrance. Can move from a cleared room to any adjacent room. If you enter an uncleared room, you will encounter a fight or an event (e.g., a trap or puzzle).
* Along the way, you find new companions, magic items, and, of course, gold.

### Characters

#### Companions

I currently use all the companions from *Baldur's Gate 3*, but if this becomes legit, I want to have non-licensed characters. I’d like to have one companion for each class.

* **Nightkill**: A halfling teenager turned emo rogue. She ran off from her parents who don't understand her and wound up in a dungeon.
* **Faylen**: A half-elf druid and cult escapee.
* **Bingus Gringus**: A goblin who recently discovered a sorcerous magic within himself.

#### Monsters

* A party of goblins led by a hobgoblin are prowling the dungeons looking for a runaway- and maybe some treasure while they're there. Watch out for their bugbear warrior!
* An artificer and their collection of constructs.

## Other features

* Add equipment; auto-equip during `__init__`
* Add action economy (action, bonus action, reaction, movement?)
* Add combat UI in Textual
* Add other options for setting ability scores (point buy, rolling scores)
* Add race features
* Add reviving dead characters (Withers, spend gold; revivify)
* Add higher levels
  * Spell casters are reassigned spell slots with base_spell_slots\[casterType\]\[level\]



___

# Copyright statement

© 2026 Zoey Kurka. All rights reserved.