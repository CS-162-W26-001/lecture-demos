from enemy import Enemy
from player import Player

from typing import override

class Banshee(Enemy):
    def __init__(self) -> None:
        super().__init__(60, "B")
    
    @override
    def encounter(self, player: Player) -> None:
        player_hp = player.get_hp()
        if player_hp < 50:
            player.take_damage(10)
        else:
            player.take_damage(1)
