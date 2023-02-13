# Chapter 9. Crafting Elegant Code with Stacks and Queues


## Abstract Data Type

- Does not care about the data structure under the hood but caring about the theoretical rules are complied, such as `FILO` or `FIFO`
- Piece of code written on top of other built-in data structures.
- Example: Set, Stack, Queue

## Stack and Queue

`Stack` and `Queue` are simply arrays with restrictions (`FILO` and `FIFO`). They are serving as temporary container to handle temporary data in an algoirhtm.

### Stack

- *Top*: The end of the stack
- *Bottom*: The beginning of the stack
- *Push*: Inserting a new value into a stack
- *Pop*: Removing elements from the top of the stack

### Queue

- *Front*: The beginning of the queue
- *Back*: The end of the queue
- *Enqueue*: Inserting a new value into a queue
- *Dequeue*: Removing elements from a queue