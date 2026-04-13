from items.item_class import Item
from tools.enums import ItemType, ArmorType, Armor

# Light
LeatherArmor = Item(
    name=Armor.leather,
    item_type=ItemType.armor, 
    is_equippable=True,  
    value=11, 
    armor_type=ArmorType.light
)

# Medium
ChainShirt = Item(
    name=Armor.chain_shirt,
    item_type=ItemType.armor, 
    is_equippable=True,  
    value=13, 
    armor_type=ArmorType.medium
)
HideArmor = Item(
    name=Armor.hide,
    item_type=ItemType.armor, 
    is_equippable=True,  
    value=12, 
    armor_type=ArmorType.medium
)
ScaleMail = Item(
    name=Armor.scale_mail,
    item_type=ItemType.armor, 
    is_equippable=True,  
    value=14, 
    armor_type=ArmorType.medium
)

# Heavy
ChainMail = Item(
    name=Armor.chain_mail,
    item_type=ItemType.armor, 
    is_equippable=True,  
    value=16, 
    armor_type=ArmorType.heavy
)