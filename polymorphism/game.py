from player import Player
from enemy import Enemy
from vampire import Vampire

"""
1. player
2. set of enemies
    - each enemy will have a certain number of hit points
    - each enemy will do something different when they encounter the player
    - each enemy will have a different representation on the screen
3. in a loop, all the enemies will attack the player
    - player's hit points will decrease each attack
    - game ends when hp <= 0
    - if player has 1 or more hp at the end of a turn, go to the next turn
"""

def play_game(player: Player, enemies: list[Enemy]) -> None:
    # play the game in a loop
    turn_count = 0
    while turn_count < 10:
        # enemies attack player
        for enemy in enemies:
            enemy.encounter(player)
        turn_count += 1
        print(f"Turn {turn_count}: player's hp is at {player.get_hp()}")

    # after the loop, the game is over
    print("you lose :(")

def main() -> None:
    # initialize game elements
    player = Player()

    enemies = []
    for i in range(5):
        enemies.append(Enemy(15, "E"))
    enemies.append(Vampire())

    play_game(player, enemies)

if __name__ == "__main__":
    main()
