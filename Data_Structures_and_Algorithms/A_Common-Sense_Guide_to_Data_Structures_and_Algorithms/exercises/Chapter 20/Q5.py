"""
Sort an array ranging from 97.0 to 99.0 in O(N) runtime

Use another data structure (Magical look up with 0(1))

1. Initialize a hash table
2. Iterate over the array:
    1. Store each element to the hash table
        key: element
        value: number of occurences
3. Iterate from 97.0 to 99.0 with increment of 0.1:
    1. If element exists in the hash table:
        1. while table[element]:
            1. Append the result to the list
            2. Decrease the table[element] by 1
4. Print out the list
"""

def sortArray(array):
    table = {}
    result = []

    for element in array:
        if table.get(element):
            table[element] += 1
        else:
            table[element] = 1

    for element in range(970, 991, 1):
        if table.get(element / 10):
            while table[element / 10]:
                result.append(element / 10)
                table[element / 10] -= 1
    
    print(result)

if __name__ == "__main__":
    array = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
    sortArray(array)