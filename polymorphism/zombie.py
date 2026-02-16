from enemy import Enemy
from player import Player

from typing import override
import random

class Zombie(Enemy):

    def __init__(self) -> None:
        super().__init__(20, "Z")

    @override
    def encounter(self, player: Player) -> None:
        damage = random.randint(0, 3)
        player.take_damage(damage)

    @override
    def get_symbol(self) -> str:
        return "Z+"
