"""
Return the missing letter of alphabet

1. Define a variable called alphabet containing 26 English letters
2. Define a dictionary called hash_map
3. Iterate through the sentence: 
    Store the value into the hash_map with default value of 711
4. Iterate through the alphabet:
    1. If the letter is not in the hash_map:
        Continue to the next letter
       Else:
        Print out that letter and terminate the function
"""

def findMissingLetter(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hash_map= {}

    for element in sentence:
        hash_map[element] = 711
    
    for letter in alphabet:
        if letter not in hash_map.keys():
            print(letter)
            return 

    return

if __name__ == "__main__":
    sentence = "the quick brown box jumps over a lazy dog"
    findMissingLetter(sentence)