# Code quality

# Readability - how easy it is to understand code
# Modularity - how well compartmentalized is your codebase?
# Maintainability - how easy it is to fix bugs, add new features, and update code
# Performance - efficiency & speed
# Scalability - how well you handle increasing workloads, more data, more users at a time
import random

class Player:
    score: int
    losses: int

    def __init__(self) -> None:
        self.score = 0
        self.losses = 0
    
    def update_score(self, win: bool) -> None:
        if win:
            self.score += 1
        else:
            self.losses += 1

    def player_is_winning(self) -> bool:
        return self.score > self.losses

class Game:
    player: Player

    def __init__(self) -> None:
        self.player = Player()

    def coin_flip(self) -> bool:
        choice = input("Choose heads or tails: ")
        result = random.choice(["heads", "tails"])
        return choice == result
    
    def play(self, number_of_turns: int) -> None:
        for i in range(number_of_turns):
            result = self.coin_flip()
            self.player.update_score(result)
    
    def print_results(self) -> None:
        if self.player.player_is_winning():
            print("you win")
        else: 
            print("you lose")

def main() -> None:
    game = Game()
    game.play(5)
    game.print_results()


if __name__ == "__main__":
    main()
