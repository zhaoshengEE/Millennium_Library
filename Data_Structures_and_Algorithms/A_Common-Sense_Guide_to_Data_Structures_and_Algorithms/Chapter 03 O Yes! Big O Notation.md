# Chapter 3. O Yes! Big O Notation


## Soul of Big O

- How the number of steps increase as the data changes


## Key Questions of O(N)

- If there are N data elements, how many steps will the algorithm take, or
- If passing in the number N, how many steps will the algorithm take.


## Three Types of Big O

> Big O notation generally refers to the worst-case scenario.

|   Type    | Description | Notes     | Example |
| :----:        |    :----:   |          :----: |    :----:   |
| `O(N)`      | If there are N elements in an array, an algorithm will take N steps.  | An algorithm is referred to as having `linear time`.  |  `Linear Search` |
| `O(1)`   | An algorthm always takes constant number of steps no matter what N is.   | An algorithm is referred to as having `constant time`.  |  `Read` |
| `O(logN)`   | An algorithm takes as many steps as it takes to keep halving data elements until ending up with one element only.    | An algorithm is referred to as having `log time`.   |  `Binary Search` |
