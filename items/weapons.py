from items.item_class import Item
from actions.attacks.attacks import *
from tools.enums import ItemType, Weapon

Crossbow = Item(
    name = Weapon.crossbow, 
    item_type=ItemType.ranged_weapon,
    is_equippable=True,
    associated_actions=[CrossbowStrike]
)
Dagger = Item(
    name=Weapon.dagger, 
    item_type=ItemType.melee_weapon,
    is_equippable=True,
    associated_actions=[DaggerStrike]
)
Greataxe = Item(
    name=Weapon.greataxe, 
    item_type=ItemType.melee_weapon,
    is_equippable=True,
    associated_actions=[GreataxeStrike]
)
Greatsword = Item(
    name=Weapon.greatsword,
    item_type=ItemType.melee_weapon,
    is_equippable=True,
    associated_actions=[GreatswordStrike]
)
Longsword = Item(
    name=Weapon.longsword,
    item_type=ItemType.melee_weapon,
    is_equippable=True,
    associated_actions=[LongswordStrike]
)
Mace = Item(
    name=Weapon.mace, 
    item_type=ItemType.melee_weapon,
    is_equippable=True,
    associated_actions=[MaceStrike]
)
Shortbow = Item(
    name = Weapon.shortbow, 
    item_type=ItemType.ranged_weapon,
    is_equippable=True,
    associated_actions=[ShortbowStrike]
)
Shortsword = Item(
    name = Weapon.shortsword, 
    item_type=ItemType.melee_weapon,
    is_equippable=True,
    associated_actions=[ShortswordStrike]
)

# Magic weapons
Longsword_plus1 = Item(
    name=Weapon.longsword,
    item_type=ItemType.melee_weapon,
    is_equippable=True,
    associated_actions=[Longsword_plus1Strike],
    bonus_modifier=1,
)