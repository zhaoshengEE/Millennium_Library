"""
Program a function that
* Accepts an array of distinct integers from 0,1,2,3...up to N
* Run in O(N)

Recognize patterns by listing out a bunch of examples

1. Iterate over the array:
    1. Increment the sum of indices
    2. Increment the sum of elements
2. Substract the sum of indices from the sum of elements
"""

def find_missing_number(array):
    index_sum = 0
    element_sum = 0

    for index, element in enumerate(array):
        index_sum += (index + 1)
        element_sum += element
    
    print(index_sum - element_sum)


if __name__ == "__main__":
    array1 = [2, 3, 0, 6, 1, 5]
    array2 = [8, 2 ,3, 9, 4, 7, 5, 0, 6]

    find_missing_number(array1)
    find_missing_number(array2)