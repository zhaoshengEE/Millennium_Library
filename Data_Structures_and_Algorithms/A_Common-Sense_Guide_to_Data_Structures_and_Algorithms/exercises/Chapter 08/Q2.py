"""
Find the first duplicate value in an array
(Assume there is one pair of duplicates within the array)
1. Define a dictionary named hash_map which records the occurence of each character
2. Iterate through the array: 
    1. If the value exists in the key of hash_map:
        1. Print out this value directly and terminate the function
        Else: 
        Store the value into the hash_map with default value of 711
"""

def findFirstDuplicateValue(array):
    hash_map = {}

    for element in array:
        if element in hash_map.keys():
            print(element)
            return
        else:
            hash_map[element] = 711
    
    return

if __name__ == "__main__":
    array = ['a', 'b', 'c', 'd', 'c', 'e', 'f']
    findFirstDuplicateValue(array)