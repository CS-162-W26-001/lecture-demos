from dog import Dog
from sled import Sled

class Husky(Dog):
    _energy_level: int

    def __init__(self, name: str, energy_level: int) -> None:
        super().__init__(name)
        self._energy_level = energy_level
    
    def pull_sled(self, sled: Sled) -> None:
        if self._energy_level <= 0:
            print("The husky refusees to move")
        else:
            sled.move(10)
            self._energy_level -= 1
