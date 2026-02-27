"""'

GCD:
2 numbers, a and b
-> find x such that a/x and b/x, 

a = 99
b = 33
x = 1, 3, 11, 33


a = 56
b = 24
x = 8
56 / 8 = 7
24/ 8 = 3

(56 % 24) /x 
"""
def gcd(a: int, b: int) -> int:
    # base case
    if a % b == 0:
        return b

    # recursive case

    # a % b < b, b < a
    c = b
    d = a % b
    return gcd(c, d)

# input gets closer to base case
# move the first letter of the string to the end
# remove that letter from the string
# recurse on the remaining letters
def reverse(string: str) -> str:
    if len(string) == 0:
        return ""
    first_letter = string[0]
    rest_of_string = string[1:]
    print(rest_of_string, first_letter)
    return reverse(rest_of_string) + first_letter

"""
1. Function needs to call itself
2. Stop recursion at some point (base case)
3. Get closer to the base case every recursive call

"""

def recursive(n: int) -> None:
    if n == 0:
        return
    if n == 1:
        print("n = 1")
        return
    print("Before", n)
    recursive(n - 1)
    print("After", n)

# n!   = 5! -> 5 * 4 * 3 * 2 * 1
# 6!        -> 6 * 5 * 4 * 3 * 2 * 1
def factorial(n: int) -> int:
    # factorial = n * factorial(n - 1)
    if n == 0:
        return 1
    if n == 1:
        return 1
    product = n * factorial(n - 1)
    return product

# 0 -> 0
# 1 -> 1
# 2 -> 10
# 3 -> 11
# 4 -> 100
def decimal_to_binary(number: int) -> str:
    if number == 0:
        return "0"
    current_digit = number % 2
    rest_of_number = number // 2
    return decimal_to_binary(rest_of_number) + str(current_digit)
    

def main() -> None:
    # print("1!", factorial(1))
    # print("2!", factorial(2))
    # print("5!", factorial(5))
    # print("6!", factorial(6))
    # print(decimal_to_binary(0))
    # print(decimal_to_binary(1))
    # print(decimal_to_binary(2))
    # print(decimal_to_binary(4))
    # print(decimal_to_binary(5))

    print(gcd(8, 2))
    print(gcd(8, 4))
    print(gcd(56, 24))

if __name__ == "__main__":
    main()
