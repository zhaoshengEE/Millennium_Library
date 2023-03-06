# Chapter 18. Dealing with Space Constraints

The key question of Big O for space complexity:

> If there are N data elements, how many units of memory will the algorithm consume?

When using Big O to describe space complexity, we only focus on the extra space (or `auxiliary space`) the algorithm consumes, such as creating an array or hash table inside an algorithm.

When computing the space complexity of an algorithm with `recursion` involved, we need to figure out how big the call stack would be at its peak.
