"""
Reverse a string

1. Initialize a stack object
2. Iterate over the string:
    1. Push each character into the stack
3. While the stack is not empty:
        1. Pop out the top value from the stack
        2. Store that popped value into the result
4. Return the result
"""

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        self.value = self.stack[-1]
        self.stack.remove(self.value)
        return self.value
    
    def len(self):
        return len(self.stack)

def reverseString(str):
    result = ''
    stack = Stack()

    for char in str:
        stack.push(char)
    
    while stack.len() != 0:
        result += stack.pop()

    return result

if __name__ == "__main__":
    str = "abcde"
    result = reverseString(str)
    print(result)