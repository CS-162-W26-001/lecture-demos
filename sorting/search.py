# array contains N elements (N is the length of the array)
# Looking for -1 in a 100,000 element array requires 100,000 iterations
def linear_search(array: list[int], search_value: int) -> bool:
    # for each element in the array,
    for element in array:
    # check to see if the element = search_value
        if element == search_value:
        # if it is, return True
            return True
    # otherwise if we go through the entire array, then return False
    return False

""""

binary search: takes a sorted array as input

cut the array in half
    - look for the element at the midpoint
    - compare which element is at the midpoint to our search value
    - if the element matches our search value, return True
    - if not, choose the lower or upper half of the array
    - repeat the process in this half

"""
# for the same 100,000 element array, how many iterations does binary search take?
# N/1 elements in our search space  - 2^0
# N/2 elements in the next iteration - 2^1
# N/4 elements in the next iteration    - 2^2
# N/8 elements in the next iteration    - 2^3
# N/16 elements in the next iteration   - 2^4
# ....                                  - 2^i (i is 16 or 17)
# 1 element (our base case)

# N = 2^i = (log_2 N = i)
def binary_search(array: list[int], search_value: int) -> bool:
    start = 0
    end = len(array) - 1

    # some kind of while loop
    while start <= end:
        mid = (end + start) // 2
        print(mid)
        if array[mid] == search_value:
            return True
        elif search_value < array[mid]:
            end = mid - 1
        elif search_value > array[mid]:
            start = mid + 1
    return False


def main() -> None:
    array = [1, 3, 6, 7, 2, 0, 5, 10]
    sorted_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(linear_search(sorted_array, 5))
    # print(linear_search(sorted_array, -1))

    big_sorted_array = list(range(100_000))
    print(binary_search(sorted_array, 3))
    print(binary_search(big_sorted_array, -1))



if __name__ == "__main__":
    main()
