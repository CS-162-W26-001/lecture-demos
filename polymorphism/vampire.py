from enemy import Enemy
from player import Player

from typing import override

class Vampire(Enemy):
    _attack_power: int

    def __init__(self) -> None:
        super().__init__(50, "V")
        self._attack_power = 1

    @override
    def encounter(self, player: Player) -> None:
        player.take_damage(self._attack_power)
        self._attack_power += 1
