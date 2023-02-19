"""
Find the Maximum Product of Three Positive Numbers
(A variation of LeetCode 628. Maximum Product of Three Numbers)
Implement a function running at O(NlogN) speed

1. Quicksort the array
2. Multiply the last three elements of the sorted array and print out the result

quickSort: (Use Recursion)
1. Base case: when subarray only has 0 or 1 element, return directly
2. Find the pivot index using partition
3. Since the pivot index is in the appropriate spot, quickSort the left subarray
4. Quicksort the right subarray

partition:
1. Choose the right most element as the pivot
2. Decrement the right index by 1
while true:
    1. Start moving the left index until it reachss a spot whose value is >= pivot value
    2. Start moving the right index until it reaches a spot whose value is <= pivot value
    3. If left index is >= right index: break the while loop
       Else: Swap the values that left index and right index are pointing to
3. Swap the values are left index and pivot index are pointing to
4. Return left index
"""

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


if __name__ == "__main__":
    array = [0,5,2,1,6,3]
    a = quickSort(array, 0, len(array) - 1)
    print(a[-1] * a[-2] * a[-3])