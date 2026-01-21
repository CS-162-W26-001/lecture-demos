def get_input() -> int:
    valid_input = False
    number = -1
    while not valid_input:
        try:
            number = int(input("Enter a number: "))
            valid_input = True
        except ValueError as exception:
            print("Invalid number", exception)
        except IndexError as indexException:
            print("Caught index error")

    return number

def sqrt(number: int) -> float:
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number")
    return number ** 0.5


def main() -> None:
    #user_input = get_input()
    #print(user_input)
    try:
      sqrt(-1)
    except ValueError as e:
        print("caught error")

if __name__ == "__main__":
    main()
