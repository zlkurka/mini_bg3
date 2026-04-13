from items.item_class import Item
from actions.attacks.attacks import *
from actions.heal.heal import Drink_MinorHealthPotion
from tools.enums import ItemType, Weapon, Potion

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

# Consumables
MinorHealthPotion = Item(
    name=Potion.minor_health,
    item_type=ItemType.consumable,
    is_equippable=True,
    is_consumable=True,
    associated_actions=[Drink_MinorHealthPotion]
)

# Magic weapons
Longsword_plus1 = Item(
    name=Weapon.longsword,
    item_type=ItemType.melee_weapon,
    is_equippable=True,
    associated_actions=[Longsword_plus1Strike],
    bonus_modifier=1,
)