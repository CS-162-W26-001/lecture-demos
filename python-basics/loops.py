def ask_for_number(min: int, max: int) -> int:
    
    # while loops
    # for loops

    valid_input = False
    while True:
        number = int(input((f"Enter a number between "
                            f"{min} and {max}: ")))
        if number >= min and number <= max:
           return number
    return number

def while_loop_playground() -> None:
    count = 0
    while count < 5:
        print(count)
        count += 1

def list_playground() -> None:
    a_number = 50
    my_numbers:list[int] = [0, 1, a_number, 1000]
    empty_list = []
    print("my_numbers: ", my_numbers)
    print("empty list:", empty_list)

    interesting_numbers: list[float] = [3.14, 1.2, 9.8]
    string_list: list[str] = ["a", "b", "c"]

    print("pi is", interesting_numbers[0])
    print("gravity is ", interesting_numbers[2])

    interesting_numbers[0] = 2 ** 0.5

    for element in interesting_numbers:
        print(element)

    # list comprehension syntax:
   # my_list = [x * 2 for x in interesting_numbers]

def average(input_list:list[float]) -> float:
    sum = 0
    for value in input_list:
        sum += value
    print(f"Sum of values is {sum}")
    size = len(input_list)
    input_list[0] = -1
    input_list[2] = -2
    return sum / size

def main() -> None:
    #my_number = ask_for_number(1, 10)
    #print(my_number)
    #`while_loop_playground()
    #list_playground()
    my_numbers = [1.0, 2, 3, 4, 5, 6, 7]
    print(my_numbers)
    my_average = average(my_numbers)
    print(my_average)
    print(my_numbers)
    


if __name__ == "__main__":
    main()
