"""
Write three different implementations of a function that finds the greatest number within an array,
which has time complexity of O(N^2), O(NlogN), O(N)
"""

# O(N^2)
def find_max_1(array):
    for i, element_i in enumerate(array):
        notChangeMax = True
        result = element_i
        for j, element_j in enumerate(array):
            if i == j:
                continue
            if element_i < element_j:
                result = element_j
                notChangeMax = False
        if notChangeMax:
            return result
    return result

# O(NlogN)
def partition(array, leftIndex, rightIndex):
    """
    :param array: an input array
    :param leftIndex: Index of the left pointer
    :param rightIndex: Index of the right pointer
    :return: the pivot index
    """ 
    pivotIndex = rightIndex
    pivotValue = array[pivotIndex]
    rightIndex -= 1

    while True:
        while array[leftIndex] < pivotValue:
            leftIndex += 1
        while array[rightIndex] > pivotValue and rightIndex != 0:
            rightIndex -= 1
        if leftIndex >= rightIndex:
            break
        else:
            array[leftIndex], array[rightIndex] = array[rightIndex], array[leftIndex]
            leftIndex += 1

    array[leftIndex], array[pivotIndex] = array[pivotIndex], array[leftIndex]

    return leftIndex

def quickSort(array, leftIndex, rightIndex):
    """
    :param array: an input array
    :param leftIndex: Index of the left pointer
    :param rightIndex: Index of the right pointer
    :return: an array sorted in ascending order
    """ 
    if rightIndex - leftIndex <= 0:
        return
    
    pivotIndex = partition(array, leftIndex, rightIndex)

    quickSort(array, leftIndex, pivotIndex - 1)
    quickSort(array, pivotIndex + 1, rightIndex)
    return array

def find_max_2(array):
    sorted_array = quickSort(array, 0, len(array) - 1)
    return sorted_array[-1]

# O(N)
def find_max_3(array):
    result = float('-inf')
    for element in array:
        if element > result:
            result = element
    return result

if __name__ == "__main__":
    array = [9,6,4,2,3,10,7,0,1]
    a = find_max_1(array)
    b = find_max_2(array)
    c = find_max_3(array)
    assert a == b
    assert b == c