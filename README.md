So I asked my friend Goop if I should code or play Baldur's Gate and she said "code Baldur's Gate," so I did.

This is a simple, terminal-based game inspired by *Dungeons and Dragons 5e* and *Baldur's Gate 3*. You can choose characters to fight alongside or build your own and battle different groups of monsters.

I plan on adding a dungeon-crawler component and potentially RPG elements. My end vision is a procedurally generated dungeon crawler with *Slay the Spire*-inspired rooms (combat and events) and a *Binding of Isaac*-inspired dungeon layout and progression.

# To-do's


## Class-specific features
- Rogue: Sneak attack
- Barbarian: rage
- Druid: wildshape
- Bard: inspo
- Cleric: healing cantrip


## 1st lvl spells
Area of effect spells with deal damage to all enemies depending on a saving throw. Like attacks, they'll still be short or long range, which will impact aggro. So burning hands or arms of hadar would be short range, while fireball would be long range.

### Priority
  - Magic missile
  - Mage armor
  - Burning hands
  - Guiding bolt
  
### Add later
  - Armor of agathys
  - Witch bolt
  - Bless
  - Find familiar
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
- Keep from wasting action on empty spell slot 
  - Nevermind option if don’t want to upcast
- Add Nevermind to action targeting
- Add equipment; auto-equip during __init__
- Add visual combat in Godot
- Add race features
- Add action economy (action, bonus action, reaction, movement?)
- Migrate character saves to pickle
- Add reviving dead characters (Withers, spend gold; revivify)
- Add higher levels
  - Spell casters are reassigned spell slots with base_spell_slots[casterType][level]