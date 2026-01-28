from animals.cat import Cat, print_cat
from animals.dog import Dog, print_dog
from animals import cat as kitty, dog as puppy
import animals


def main() -> None:
    my_cat = Cat()
    my_cat.name = "Clara"
    my_cat.weight = 14

    a_dog = Dog()
    a_dog.name = "Teche"
    a_dog.loudness = 10
    print_cat(my_cat)
    print_dog(a_dog)

    animals.helloworld()

if __name__ == "__main__":
    main()

