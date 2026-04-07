from items.item_class import Item
from actions.attacks.attacks import Longsword
from actions.heal.heal import Drink_MinorHealthPotion
from tools.enums import ItemType, ArmorType, Armor, Weapon, Potion

# Weapons
LongswordItem = Item(
    name=Weapon.dagger,
    item_type=ItemType.weapon,
    is_equippable=True,
    associated_actions=[Longsword]
)

# Armor
LeatherArmor = Item(
    name=Armor.leather,
    item_type=ItemType.armor, 
    is_equippable=True,  
    value=11, 
    armor_type=ArmorType.light
)

# Consumables
MinorHealthPotion = Item(
    name=Potion.minor_health,
    item_type=ItemType.consumable,
    is_equippable=True,
    is_consumable=True,
    associated_actions=[Drink_MinorHealthPotion]
)