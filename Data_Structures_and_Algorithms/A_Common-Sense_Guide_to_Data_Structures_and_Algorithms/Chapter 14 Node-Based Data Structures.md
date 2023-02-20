# Chapter 14. Node-Based Data Structures

## Node
- Connected data that is dispersed throughout the computer's memory are known as `nodes`.
- Each node consists of two cells. One for the actual data, the other holds the link to the next node's memory address.
- A linked list's first node can be referred to as its `head`, and its final node as its `tail`.


## Linked List

Typically, a linked list keeps track of the first node of the list.

- For read and search, the linked list has a worst case of O(N)
    - For read, array has an efficiency of O(1), which outperforms the linked list.
- For insertion and deletion, the linked list has a best case of O(1). The best case is when inserting and deleting at the beginning of the list.
    - When inserting or deleting at the beginning of the list, unlike array, the linked list is not required to shift any data. This leads the linked list outperforming array in this case.
    - Arrays favor insertions and deletions at the end, while linked lists favor insertions and deletions at the beginning.
- Linked list is an appropriate choice of data structure when iterating over an entire list while makeing insertions or deletions.


## Doubly Linked List

> A doubly linked list is like a lined list except that each node has two links.

Typically, a doubly linked list keeps track of both the first and last nodes.

- A doubly linked list allows us to move both forward and backward through the list. Hence, insertion or deletion on either side has an efficiency of O(1).

- Doubly linked list is the perfect underlying data structure for a queue.
