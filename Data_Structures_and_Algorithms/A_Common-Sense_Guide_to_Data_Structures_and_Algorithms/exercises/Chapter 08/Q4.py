"""
Findd the first non-duplicated character

1. Define a dictionary called hash_map
2. Iterate through the word:
    1. If the character already exists in the hash_map:
        Increment its value by 1
       Else:
        Insert this character into the hash_map with value of 1
3. Iterate through the word:
    1. If the letter in the hash_map has a value of 1:
        Print out that letter and terminate the function
"""

def findFirstNonDuplicate(word):
    hash_map= {}

    for element in word:
        if element in hash_map.keys():
            hash_map[element] += 1
        else: hash_map[element] = 1
    
    for element in word:
        if hash_map[element] == 1:
            print(element)
            return 

    return

if __name__ == "__main__":
    word = "minimum"
    findFirstNonDuplicate(word)