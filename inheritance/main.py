from dog import Dog
from husky import Husky
from sled import Sled
from pitbull import Pitbull

def main() -> None:
    kona = Dog("kona")
    kona.print()

    murphy = Dog("murphy")
    murphy.print()

    mochi = Husky("mochi", 5)
    mochi.print()

    # sled = Sled()
    # mochi.pull_sled(sled)
    # mochi.pull_sled(sled)
    # mochi.pull_sled(sled)
    # mochi.pull_sled(sled)
    # mochi.pull_sled(sled)
    # mochi.pull_sled(sled)

    fluffy = Pitbull("fluffy")
    fluffy.print()
    dogs_barking([fluffy, mochi, kona, murphy])


def dogs_barking(dogs: list[Dog]) -> None:
    for dog in dogs:
        dog.bark()

if __name__ == "__main__":
    main()
