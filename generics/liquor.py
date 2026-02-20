from item import Item

class Liquor(Item):
    _volume: float

    def __init__(self, price: int, name: str, volume: float) -> None:
        super().__init__(price, name)
        self._volume = volume

    def print(self) -> None:
        super().print()
        print(f"Liquor volume: {self._volume}")
