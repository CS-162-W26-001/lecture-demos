from animals.cat import print_cat

class Dog:
    name: str
    loudness: float

def print_dog(dog: Dog) -> None:
    print(f"Dog's name is {dog.name}")
