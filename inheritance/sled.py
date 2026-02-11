class Sled:
    _distance_travelled: int

    def __init__(self) -> None:
        self._distance_travelled = 0
    
    def move(self, distance: int) -> None:
        self._distance_travelled += distance
        print(f"Sled has moved {self._distance_travelled} feet")
