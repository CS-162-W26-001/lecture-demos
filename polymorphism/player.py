class Player:
    _hp: int

    def __init__(self) -> None:
        self._hp = 100

    def get_hp(self) -> int:
        return self._hp

    def take_damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Cannot take negative damage")
        self._hp -= amount

        if self._hp < 0:
            self._hp = 0
