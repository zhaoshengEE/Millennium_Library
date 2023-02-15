# Chapter 12. Dynamic Programming

Ironically, dynamic programming has nothing to do with dynamic technique.

## Unnecessary Recursive Calls and Solution

- Unnecessary recursive calls often drag out the algorithm execution speed.
- *Solution*: Store the intermediate result in a variable.
- Example: Let's say we want to find the maximum value in an array using recursion.(*why the hell we cannot use a for loop instead?*)

```python
def max(array):
    if len(array) == 1:
        return array[0]
    
    if array[0] > max(array[1:]):
        return array[0]
    else:
        return max(array[1:])
```

Bringing a temporary variable (`max_of_remainder`) to the table can ease up the running and speed up the function from O(2<sup>N</sup>) to O(N)

```python
def max(array):
    if len(array) == 1:
        return array[0]
    
    max_of_remainder = max(array[1:])

    if array[0] > max_of_remainder:
        return array[0]
    else:
        return max_of_remainder
```

## Overlapping Subproblems and Dynamic Programming

- *Overlapping Subproblems*: The subproblems end up calling many of the same recursive functions as each other. 
- Dynamic programming is the process of optimizing recursive problems that have overlapping subproblems.

### Dynamic Programming through Memoization

1. Get a hash table involved, which stores the computed results for quick reference
2. Pass the hash table as an extra parameter when calling recursive function.

For how to implement memoization, please refer to the [Exercise Question 2 in this chapter](./exercises/Chapter%2012/Q2.py) and [Exercise Question 3 in this chapter](./exercises/Chapter%2012/Q3.py)

> Because the hash table is a specific object in memory, we are abot to pass it from one recursive call to the next, even though we're modifying it as we go.

### Dynamic Programming through Bottom-Up

Ditch recursion and use some other approach (like a loop) to solve problems

### Memoization vs. Bottom-Up

> Generally speaking, goint bottm-up is often the better choice unless the recursive solution is more intuitive. Where recursion is more intuitive, you can keep the recursion and keep it fast by using memoization.
