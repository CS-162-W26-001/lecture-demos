from store import Store
from furniture import Furniture
from liquor import Liquor


# def print[T](item: T) -> None:
#     print(item)

def main() -> None:
    ikea = Store[Furniture]()
    chair = Furniture(100, "chair", "white")
    sofa = Furniture(1000, "sofa", "grey")
    ikea.add_to_inventory(chair)
    ikea.add_to_inventory(sofa)

    liquor_store = Store[Liquor]()
    vodka = Liquor(50, "vodka", 750)
    liquor_store.add_to_inventory(vodka)

    sold_item = ikea.sell_item(0)
    sold_item.print()

    ikea.print()

if __name__ == "__main__":
    main()
