class Dog:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def print(self) -> None:
        print(f"Dog's name is {self._name}")

    def bark(self) -> None:
        print("Bark!")
