"""
Given a string, return the first index of 'x'
"""

def getFirstX(string, index = 0):
    if string[index] == 'x':
        return index
    else: return getFirstX(string, index + 1)

if __name__ == "__main__":
    print(getFirstX('abcdefghujklmnopqrstuvwxyz'))