from player import Player

class Enemy:
    _hp: int
    _sprite: str

    def __init__(self, hp: int, sprite: str) -> None:
        self._hp = hp
        self._sprite = sprite
    
    def encounter(self, player: Player) -> None:
        player.take_damage(1)

    def get_symbol(self) -> str:
        return self._sprite
