So I asked my friend Goop if I should code or play Baldur's Gate and she said "code Baldur's Gate," so I did.

This is a simple, terminal-based game inspired by *Dungeons and Dragons 5e* and *Baldur's Gate 3*. You can choose characters to fight alongside or build your own and battle different groups of monsters.

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

## Game progression
Since I only have combat and character creation developed for this game, I'm not sure what I want the full adventure to look like. Right now, I can imagine a few things:
- Finding new companions (so the companion list isn't super long at the start)
  - Starting party: Shadowheart, Lae'zel, Gale, Astarion? How do I factor in potential custom character? Or should I work under the assumption that you start with a custom character? That might make more sense
- Dungeon crawl: move through different rooms and have different encounters. Maybe the rooms could be STS-style, with combat, events, or maybe merchants; rooms mapped out like in Isaac
- Treasure: gold and items!


## Other features
- Keep from wasting action on empty spell slot 
  - don’t display if no slots, 
  - Nevermind option if don’t want to upcast
- Add Nevermind to action targeting
- Add equipment; auto-equip during __init__
- Add visual combat in Godot
- Add race features
- Add action economy (action, bonus action, reaction, movement?)
- Migrate character saves to pickle
- Add reviving dead characters (Withers, spend gold; revivify)
- Add higher levels