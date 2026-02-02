class Cat:
    name: str
    weight: float
    color: str

    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color
        #self.weight = -1

    def print(self) -> None:
        print(f"Cat's name is {self.name}")
