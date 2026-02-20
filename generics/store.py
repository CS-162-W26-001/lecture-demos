from furniture import Furniture
from item import Item

class Store[T: Item]:
    _inventory: list[T]
    _revenue: int

    def __init__(self) -> None:
        self._inventory = []
        self._revenue = 0

    def add_to_inventory(self, item: T) -> None:
        self._inventory.append(item)
    
    def sell_item(self, index: int) -> T:
        item = self._inventory[index]
        del self._inventory[index]
        self._revenue += item.get_price()
        return item

    def print(self) -> None:
        print(f"Revenue: {self._revenue}")
        print("Inventory:")
        for item in self._inventory:
            item.print()
