from item import Item

class Furniture(Item):
    _color: str

    def __init__(self, price: int, name: str, color: str) -> None:
        super().__init__(price, name)
        self._color = color
    
    def print(self) -> None:
        super().print()
        print(f"Furniture color: {self._color}")
