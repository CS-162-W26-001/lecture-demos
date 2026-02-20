from abc import ABC, abstractmethod

class Item(ABC):
    _price: int
    _name: str

    def __init__(self, price: int, name: str) -> None:
        self._price = price
        self._name = name

    def get_price(self) -> int:
        return self._price
    
    def print(self) -> None:
        print(f"Name: {self._name}, price: {self._price}")
