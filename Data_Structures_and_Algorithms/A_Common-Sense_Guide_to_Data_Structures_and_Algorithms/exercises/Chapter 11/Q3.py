"""
Get the triangular number (Given an integer, 
return the corresonding index of value in the triangular numbers series, 
i.e., the sum of that integer and the previous number)

Subproblem: Find the triangular number in the previous index

Base Case: When index == 1

def getTriangularNum(index):
1. If index == 1: return 1
2. return index + getTriangularNum(index - 1)
"""

def getTriangularNum(index):
    if index == 1: 
        return 1
    return index + getTriangularNum(index - 1)

if __name__ == "__main__":
    print(getTriangularNum(7))