"""
Return the length of the longest consecutive sequence in an array in O(N) runtime

Use another data structure (Magical look up with 0(1)) + Greedy Algorithm

1. Initialize a hash table
2. Initialize length and max_length with value of 1
3. Iterate over the array:
    1. length = 1
    2. Assign {"element": True} to the hash table
    3. while table.get(element - 1):
        1. length += 1
        2. Decrement the element by 1
    4. while table.get(element + 1):
        1. length += 1
        2. Increment the element by 1
    5. If length > max_length:
        1. max_length = length
4. Print out max_length
"""

def find_max_length(array):
    table = {}
    length, max_length = 1, 1

    for element in array:
        length = 1
        table[element] = True
        
        temp = element - 1
        while table.get(temp):
            length += 1
            temp -= 1
        
        temp = element + 1
        while table.get(temp):
            length += 1
            temp += 1
        
        if length > max_length:
            max_length - length
    
    print(length)
    

if __name__ == "__main__":
    array1 = [10, 5, 12, 3, 55, 30, 4, 11, 2]
    array2 = [19, 13, 15, 12, 18, 14, 17, 11]
    find_max_length(array1)
    find_max_length(array2)