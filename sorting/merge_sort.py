""""
Divide-and-conquer

- given two sorted lists, can we merge them into one bigger sorted list?

Divide:
- split an array in half, we end up with two lists
     - split each of those in half, we have four lists
     - split each of those in half, we have eight lists
        - ... eventually a list will have just 1 element
        - [1], [2], [3], [4], [5], [6]
- base case: 
    - a list with a single element

    
Conquer:
- merge of those lists
    - merge([1], [2]) -> [1, 2]
    - merge([3], [4]) -> [3, 4]
    - merge([5], [6]) -> [5, 6]
        - merge([1, 2], [3, 4]) -> [1, 2, 3, 4]
            - merge([1, 2, 3, 4], [5, 6]) -> [1, 2, 3, 4, 5, 6]

                [5, 3, 2, 1, 4]
                /               \\
        [5, 3, 2]            [1, 4]     
        /         \\           /   \\
    [5, 3]         [2]        [1]   [4]
    /   \\
  [5]    [3]  

merge(a, b)
    c = new list

    while index of a < length of a and index of b < length of b:
        if a[index of a] < b[index of b]:
            add a[index of a] to c
            increment index of a
        else:
            add b[index of b] to c
            increment index of b
    
    while index of a < length of a:
        add next element in a to c
        increment index of a
    
    while index of b < length of b:
        add next element in b to c
        increment index of b

    return c

"""
def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    left_index = 0
    right_index = 0

    # logic goes here
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1


    return result

"""
merge_sort(unsorted list):
    if length of list <= 1:
        return list
    midpoint = length of list  / 2 
    recurse on left half of the list
    recurse on right half of the list
    return merge(left half, right half)
"""

def merge_sort(unsorted_list: list[int]) -> list[int]:
    if len(unsorted_list) <= 1:
        return unsorted_list
    midpoint = len(unsorted_list) // 2
    left = merge_sort(unsorted_list[0:midpoint])
    right = merge_sort(unsorted_list[midpoint:])
    return merge(left, right)

def main() -> None:
    result = merge([1, 2, 3], [4, 5, 6])
    assert result == [1, 2, 3, 4, 5, 6], f"{result} was not in sorted order"

    result2 = merge_sort([1])
    assert result2 == [1], "base case did not return the expected result"

    result3 = merge_sort([7, 3, 1, 9, 11, 0])
    print(result3)
    assert result3 == [0, 1, 3, 7, 9, 11], "results were not in correct order"

    result4 = merge_sort([3, 2, 1])
    assert result4 == [1, 2, 3], "results were not in correct order"

if __name__ == "__main__":
    main()
