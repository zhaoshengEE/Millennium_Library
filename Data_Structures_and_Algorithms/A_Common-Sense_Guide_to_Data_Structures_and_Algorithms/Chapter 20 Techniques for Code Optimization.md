# Chapter 20. Techniques for Code Optimization

Prerequisite:
- Determine the Big O of the current algorithm.
- Determine the best-imaginable Big O the task could possibly take.

> It is not always possible to achive the best-imaginable Big O. After all, just because you can dream of something doesn't mean it can become reality.


## Magical Lookups

> If I could magically find a desired piece of information in O(1) time, can I make my algorithm faster.

Use hash table to make that magic happen.


## Recoginizing Patterns

Find patterns through generating numerous examples.


## Greedy Algorithms

In each step, we choose what appears to be the best option based on the information available at that moment in time.

> We are basically like a child in a candy shop grabbing the first candy we see, but as soon as we see a bigger candy, we drop the first one and grab the bigger one.


## Change the Data Structure

Store the data in an alternative data structure.

**Magical Lookups** is a special case of this optimization method.

> Hash table turns out very often to be a great choice, so that's a good place to start.
