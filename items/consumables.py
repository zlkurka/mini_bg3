from items.item_class import Item
from actions.heal.heal import Drink_MinorHealthPotion
from tools.enums import ItemType, Potion

MinorHealthPotion = Item(
    name=Potion.minor_health,
    item_type=ItemType.consumable,
    is_equippable=False,
    is_consumable=True,
    associated_actions=[Drink_MinorHealthPotion]
)