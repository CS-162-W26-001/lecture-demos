
class Dog:
    name: str
    loudness: float

    def __init__(self, name: str, loudness: float) -> None:
        self.name = name
        self.loudness = loudness

    def print(self) -> None:
        print(f"Dog's name is {self.name}")

    def play(self, toy: str) -> None:
        print(f"{self.name} plays with {toy}")
