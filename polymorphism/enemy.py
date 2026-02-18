from player import Player
from abc import abstractmethod, ABC

class Enemy(ABC):
    _hp: int
    _sprite: str

    def __init__(self, hp: int, sprite: str) -> None:
        self._hp = hp
        self._sprite = sprite
    
    @abstractmethod
    def encounter(self, player: Player) -> None:
        pass

    def get_symbol(self) -> str:
        return self._sprite
