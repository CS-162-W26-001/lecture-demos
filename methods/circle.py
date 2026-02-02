class Circle:
    origin_x: int
    origin_y: int
    radius: float

    def __init__(self, x: int, y: int, radius: float) -> None:
        self.origin_x = x
        self.origin_y = y
        if radius < 0:
            raise ValueError("Cannot have a negative radius")
        self.radius = radius
    
    def print(self) -> None:
        print(f"x={self.origin_x}, y={self.origin_y}, radius={self.radius}")
