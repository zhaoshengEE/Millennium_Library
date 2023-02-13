# Chapter 10. Recursively Recurse with Recursion


## Fundamentals

- *Recursion*: A function calling it self.
- *Base Case*: The case in which the function will not recurse

- Every recursive function needs at least one base case to prevent it from calling itself indefinitely.
- When reading a recursive code, start analyzing the base case first and building up upon that is a great way to reason about recursive code.

## Call Stack

`Call stack` is a stack used by computer to keep track of which functions it is in the middle of calling.

The function that is called last (or say, most recently), is the function we need to complete first.

### Stack Overflow

If the call stack grows indefinitely, the computer will reach a point where there is no more room in its short-term memory to hold the data. This error is known as `stack overflow`.

## Use Case

Recursion is a natural fit when we need to delve into multiple layers of a problem without knowing how many layers there are

*(Spoiler Alert: Depth-First Search)*
