"""
Return the total number of characters across all strings in an array.

Subproblem: Calculate the number of characters across all strings except the first element
we may need to use a variable to track the index

Base Case: When index is over the last index of the array

Function name: countChar
@param: array
@param: index, default value = 0
1. If index == len(array): return 0
2. Initialize a vairable named count
3. Iterate over the current index of the array and count the number of characters
4. Return the count + countChar(array, index + 1)
"""

def countChar(array, index = 0):
    if index == len(array): return 0
    count = 0
    for char in array[index]:
        count += 1
    return count + countChar(array, index + 1)

if __name__ == "__main__":
    array = ["ab", "c", "def", "ghij"]
    num = countChar(array)
    print(num)