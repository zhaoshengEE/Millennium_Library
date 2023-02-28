# Chapter 17. It Doesn't Hurt to Trie

## Fundamentals of Trie

- Also known as `Prefix Tree` or `Digital Tree`.
- `Trie` is not a binary tree, which means a trie node can have any number of child nodes.
- We need to implement `*` in the trie to indicate when parts of a word are also words themselves.


### Trie Search

*Time Complexity:* O(K), where K is the size of the input.

Here using O(N) is kind of misleading, since N usually refers to the number of data contained in a data structure.

> 1. Assign the root node to the `currentNode`
> 2. Iterate over each character of the search string:
>     1. Check if the `currentNode` has a child with that character as a key.
>     2. If it does not, return None. That means our serach string does not exist in the trie.
>     3. Otherwise, update the `currentNode` to become that child.
> 3. Return `currentNode`. This means we found our search string within our trie. The reason for returning `currentNode` here instead of `True` is to help accomplish autocomplete feature.

For the implementation of trie search, please refer to the [Exercise Question in this chapter](./exercises/Chapter%2017/Q3%2C4.py)


### Trie Insertion

*Time Complexity:* O(K)

> 1. Assign the root node to the `currentNode`
> 2. Iterate over each character of the search string:
>     1. Check if the `currentNode` has a child with that character as a key.
>     2. If it does not, create such a child node and update the `currentNode` to become that child.
>     3. Otherwise, update the `currentNode` to become that child.
> 3. Add a `"*"` child to the last node to indicate the word is complete.

For the implementation of trie insertion, please refer to the [Exercise Question in this chapter](./exercises/Chapter%2017/Q3%2C4.py)


## Takeaway

> An array can be passed up and down a call stack is because the array remains the same object in memory even when we add new values to it.
> When a string is modified, on the other hand, the computer actually creates a new string instead of truly modifying the original string object.
