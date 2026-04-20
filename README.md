This is a simple, terminal-based game inspired by *Dungeons and Dragons 5e* and *Baldur's Gate 3*. You can choose characters to fight alongside or build your own and battle different groups of monsters.

I only began learning Python a few months ago, and with it the ins and outs of computer stuff, so I apologize if some of my instructions are unclear, unoptimal, or don't work altogether. I also apologize that my code is disgusting, lol.

I plan on adding a dungeon-crawler component and potentially RPG elements. My end vision is a procedurally generated dungeon crawler (layout inspired by *The Binding of Isaac*) that gets more difficult the further you move from the starting room, and  *Slay the Spire*-inspired rooms (combat and events).


___

# How to play

Make sure you have Python 3.14 installed, along with Rich (use `pip install rich` or `python -m pip install rich`)

## Using executable

The game is executed from `main.exe` in the root project folder of the latest release. The executable was created using Pyinstaller, meaning that computers running different a operating system architectures from my own (Windows 11, 64 bit) may have trouble running it. If the .exe doesn't work, you can use one of the other methods to run the game.

I’m working on a better way of making an exectuable, but I’m a beginner to software development and Python is a wacky language, so it’s taking some time.

## From your computer's terminal

* Download this repository. I will have releases soon where you can download it.
* Copy the path to `main.py` from your file navigation system
* Enter `python` into your terminal (`python3` on Mac), and paste the path to the file before hitting enter
  * Example: `python ~/Downloads/mini_bg3/main.py`

## Using an IDE

* Download this repository’s source code.
* If you already have an IDE like VS Code installed, this will be your easiest choice.
* Make sure you have Python installed on your computer and have an extension to execute Python code in your IDE
* Open this project's root folder in your IDE. Navigate to `main.py`
* Execute the code in `main.py`


___

# To-do's

## Priority

* Add disadvantage on stealth for medium and heavy armor
* Add bleeding condition; give to Injured Adventurer
* Add potions (used from Party items?)
* Fix bug where Bard loses spell slots when long resting after being added to party from Injured Adventurer event
* Add insight check option for injured adventurer event, maybe I’ll give the medicine check one to Nightkill’s join-up event
* Add item proficiencies (Character has list of things they’re proficient with; check if Item in Character.item_proficiencies)
  * If proficient with weapon, give proficiency bonus
  * If not proficient with armor, give a debuff
* Add more spells, especially for druid and bard
* Add action economy (action, bonus action, reaction, movement?)
* Balance encounters
  * Come to think of it, I don’t think encounters are supposed to kill the party that often. The problem is this game is so RNG dependent. Maybe my goblins are too strong
* Add ability to use buffs to events
* Add Event options locked behind certain prereqs (e.g. an Action that deals a certain amount of damage, having an ability score of a certain threshold, having a particlar item, )
* Work out FindFamiliar
  * Add more familiars
  * Figure out what I want familiars to do (attack? Extend spell range? Probably the latter. Might need reactions for this)
* Add racial features
  * Halfling: reroll nat 1s once
  * Tiefling: resistant to fire
  * Dwarf: resistant to poison
* Add backgrounds with additional skills and maybe a feature

## Class-specific features

* Paladin: lay on hands
  * Ways I might implement it:
    * Have a certain number of uses to give a rolled or flat amount of healing (like BG3)
    * Can expend any amount from pool of 5 \* level (like 5e)
  * Removes poisoned condition
  * Bonus action
* Druid: wildshape (level 2?)

## 1st lvl spells

### Priority

* Guiding bolt (an attack that gives a debuff)
* Magic missile (an attack with a guaranteed hit)
* Mage armor
* Guidance

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

* Add action economy (action, bonus action, reaction, movement?)
* Add ability to cast spells at camp (e.g., FindFamiliar, MageArmor)
* Add combat UI in Textual
* Add other options for setting ability scores (point buy, rolling scores)
* Add race features
* Add reviving dead characters (Withers, spend gold; revivify)
* Add higher levels
  * Spell casters are reassigned spell slots with base_spell_slots\[casterType\]\[level\]

## Notes on changes

* I think events might be too easy to fail. Since it’s an ability check, there’s a chance you can fail and get nothing out of the event. So maybe I need to lower DCs or have different levels of difficulty for different options


___

# Copyright statement

© 2026 Zoey Kurka. All rights reserved.