# Chapter 11. Learning to Write in Recursive

Please be noticed, sometimes recursion can have a negative impact on the time complexity of an algorithm.

## Patterns of Recursive Problems

- Repetedly execute a function.
- Perform a calculation based on a subproblem.

## "Bottom-Up" and "Top-Down" Recursion Strategies

### Bottom-Up

- Build the solution from the bottom up.
- Oftentimes, **passing extra parameters** is involved when writing recursive functions in bottom-up strategy.
- **Typically, bottom-up strategy does not add much value over using a classic loop.**
- Example: [Exercise Question 1 in this chapter](./exercises/Chapter%2011/Q1.py)

### Top-Down

- Make calculation based on the problem's subproblem.
- Recursion is the only way to achieve a top-down strategy.

#### Top-Down Thought Process

1. Assume the recursive function we are writing is already there.
2. Identify the subproblem.
3. See what happens when we call the function on the subproblem and go from there.
4. Eventually, handle the base cases.

## The `Staircase` Problem and the `Unique Path` Problem

Both `Staircase` and `Unique Path` problems compute how many possible paths can one take to the destination.

`Staircase` problem is in 1D, whereas `Unique Path` problem is in 2D. Both of them implement *Top-Down* strategy.

For `Unique Path` problem, please refer to the [Exercise Question 5 in this chapter](./exercises/Chapter%2011/Q5.py)
