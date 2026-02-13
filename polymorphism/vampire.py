from enemy import Enemy

class Vampire(Enemy):
    
    def __init__(self) -> None:
        super().__init__(50, "V")
