"""
Given an array of numbers and return a new array containing just the even number
(Use recursion)

Subproblem: The even numbers in the remaining array except the current element

Base Case: When there is no more number in the array

Function name: fetchEvenNum(array):
@param: array
@param: index, default value = 0
1. If array is empty: return 0
2. If first element is even:
    return first element + fetchEvenNum(array[1:])
   Else:
    return fetchEvenNum(array[1:])

"""

def fetchEvenNum(array):
    if len(array) == 0: return []
    
    if array[0] % 2 == 0:
        return [array[0]] + fetchEvenNum(array[1:])
    else:
        return fetchEvenNum(array[1:])

if __name__ == "__main__":
    array =[1,2,3,4,5,6,7,8,9,10]
    result = fetchEvenNum(array)
    print(result)