import math
import random

def guessing_game() -> None:
    secret_number = random.randint(1, 10)
    print("Secret number: ", secret_number)
    user_number = int(input("Enter a number: "))
    
    if user_number == secret_number:
        print("You win!")
    elif user_number < secret_number:
        print("YOu entered a number < secret number")
    else:
        print("You entered a number > secret number")


def choose_value() -> float:
    number = float(input("Enter a float: "))
    if number < 3.14:
        return number
    else:
        return 0.0

def ask_for_value() -> None:
    number = float(input("Enter a positive float: "))
    # == 
    # < > 
    # <= >=
    # !=
    if number > 0:
        print("You entered a positive integer")
    elif number > 10:
        print("You entered > 10")
    elif number == 0:
        print("You entered zero")
    else: 
        print("You did not enter a positive integer")

def sqrt_of_input() -> None:
    number = int(input("Enter an integer: "))
    sqrt_of_number = math.sqrt(number)
    print(f"Square root of {number} is {sqrt_of_number}")

def main() -> None:
    #print("Hello world")

    #my_input = input("Enter a string: ")
    #print(f"You entered {my_input}")
    #print("You entered " + my_input)
    #print("You entered", my_input)

    #my_number = int(input("Enter a number: "))
    #print(f"You entered the number {my_number}")
    #sqrt_of_input()
    #ask_for_value()
    guessing_game()

if __name__ == "__main__":
    main()

