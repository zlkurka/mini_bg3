from tools.enums import ItemType, ArmorType

class Item():

    def __init__(self, name, item_type: ItemType, is_equippable: bool = False, is_consumable: bool = False, associated_actions: list = [], associated_conditions: list = [], number_of_uses: int = 0, value: int = 0, bonus_modifier: int = 0, armor_type: ArmorType = None):
        self.name = name
        self.item_type: ItemType = item_type
        self.is_equippable: bool = is_equippable
        self.is_consumable: bool = is_consumable
        self.associated_actions: list = list(associated_actions)
        self.associated_conditions: list = list(associated_conditions)
        self.number_of_uses: int = number_of_uses
        self.value: int = value
        self.armor_type: ArmorType = armor_type
        self.bonus_modifier: int = bonus_modifier

    def __repr__(self):
        if self.bonus_modifier:
            return "[underline]" + str(self.name) + f", +{self.bonus_modifier}" + "[/underline]"
        return "[underline]" + str(self.name) + "[/underline]"