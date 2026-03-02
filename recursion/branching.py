# fibonacci sequence = each number is the sum of the previous two numbers


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ....
def fib(n: int) -> int:
    # base case
    if n <= 1:
        return 1

    # recursive call
    # each recursive call needs to get closer to the base case
    return fib(n - 1) + fib(n - 2)


# given a list of numbers and a target sum, determine if any combination of numbers
# sum to the target_sum
def sublist_sum(input_list:list[int], target_sum: int) -> bool:
    # base case 1
    if target_sum == 0:
        return True
    # base case 2
    if len(input_list) == 0:
        return False
    if target_sum < 0:
        return False
    first_number = input_list[0]
    rest_of_numbers = input_list[1:]
    # recursion with the first_number included
    # a + b = target_sum
    # target_sum - a - b = 0
    print("first number", first_number)
    if sublist_sum(rest_of_numbers, target_sum - first_number):
        return True

    # recursion without the first_number included    
    return sublist_sum(rest_of_numbers, target_sum)

def coin_change_helper(amount: int) -> list[int]:
    coins = []
    coin_change(amount, coins)
    return coins

def coin_change(amount: int, coins: list[int]) -> bool:
    # base case
    if amount == 0:
        return True
    if amount < 0:
        return False
    
    # 25
    if coin_change(amount - 25, coins):
        coins.append(25)
        return True

    # 10
    if coin_change(amount - 10, coins):
        coins.append(10)
        return True

    # 5
    if coin_change(amount - 5, coins):
        coins.append(5)
        return True

    return False

def main() -> None:
    # print(fib(1))
    # print(fib(3))
    # print(fib(5))
    # print(sublist_sum([1, 3, 5, 10], 8), "should be True")
    # print(sublist_sum([1, 3, 5, 10], 12), "should be False")
    print(coin_change_helper(0) ,"should be true")
    print(coin_change_helper(10), "should be true")
    print(coin_change_helper(115), "should be true")
    print(coin_change_helper(18), "should be false")
    
if __name__ == "__main__":
    main()
