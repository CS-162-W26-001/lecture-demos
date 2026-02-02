from animals.cat import Cat
from animals.dog import Dog
from animals import cat as kitty, dog as puppy
import animals
from circle import Circle

def main() -> None:
    fiona = Dog("Fiona", 5)
    fiona.play("ball")

    spike = Dog("Spike", 50)
    spike.print()

    fluffy = Cat("Fluffy", "orange")
    fluffy.print()

    circle = Circle(1, 2, 5.5)
    print(circle)
    circle.print()
    
if __name__ == "__main__":
    main()

