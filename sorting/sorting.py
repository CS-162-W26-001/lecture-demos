"""

for every element in the array:
    for every element before it:
        compare the element with the one that comes next
            if the left > right:
                swap them

"""
def swap(array: list[int], i: int, j: int) -> None:
    array[i], array[j] = array[j], array[i]

def bubble_sort(array: list[int]) -> None:
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)


"""
selection sort:
    for each element in the array:
        for each element after the sorted part:
            compare it to the minimum value
            if it is less than the minimum, store its index
        add it to the end of the sorted part by swapping index of the min value
        increment the sorted part by 1 

"""

def selection_sort(array: list[int]) -> None:
    for i in range(len(array) - 1):
        sorted_index = i
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        swap(array, sorted_index, min_index)
        # temp = array[sorted_index]
        # array[sorted_index] = array[min_index]
        # array[min_index] = temp



""""
insertion sort (array of integers):

    for each element in the array:
        find the next element
        for each preceding element:
            if the new value < preceding element:
                swap new value with preceding element

"""
def insertion_sort(array: list[int]) -> None:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                swap(array, j, j - 1)


def min(array: list[int]) -> int:
    mininum = 9999
    for element in array:
        if element < mininum:
            mininum = element
    return mininum

def main() -> None:
    array = [6, 14, 29, 3, 27, 7, 22, 0, 5]
    # print(min(array))
    insertion_sort(array)
    print(array)
    print(array[0])

if __name__ == "__main__":
    main()
