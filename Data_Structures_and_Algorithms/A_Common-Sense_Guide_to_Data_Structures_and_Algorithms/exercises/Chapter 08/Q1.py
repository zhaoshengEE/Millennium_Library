"""
Return the intersection of two arrays

1. Define an empty list, named result, storing the common values of the two arrays
2. Iterate through the first array: 
    1. Store each value into a dictionary with default value of 711
3. Iterate through the second array:
    1. If the value exists in the keys of dictionary:
        1. Store this value into the result list
4. Print out the result list
"""

def getIntersection(first_array, second_array):
    result = []
    index = {}

    for element in first_array:
        index[element] = 711
    
    for element in second_array:
        if element in index.keys():
            result.append(element)
    
    print(result)

if __name__ == "__main__":
    first_array = [1,2,3,4,5]
    second_array = [0,2,4,6,8]
    getIntersection(first_array, second_array)