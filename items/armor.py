from items.item_class import Item
from tools.enums import ItemType, ArmorType, Armor

# Armor
LeatherArmor = Item(
    name=Armor.leather,
    item_type=ItemType.armor, 
    is_equippable=True,  
    value=11, 
    armor_type=ArmorType.light
)