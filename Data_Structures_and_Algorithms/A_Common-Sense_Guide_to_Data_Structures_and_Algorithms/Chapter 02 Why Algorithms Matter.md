# Chapter 2. Why Algorithms Matter


> An algorithm is simply a set of instructions for completing a specific task.


## Ordered Array
- When inserting into an ordered array, it is necessary to conduct a search and determine the right spot for the insertion before the actual insertion.
    - This makes ordered array has more time complexity than classic array in the `insertion` scenario.
- The advantage of an ordered array over the classic array lies in the `serach` scenario, since ordered array has the alternative option: `binary serach`.


## Binary Search

- In each seraching step, we find the middle point of an ordered array and compare the `middle value` with our `seraching value`. 
    - If the `middle value` equals to the `searching value`: return the index of `middle value`
    - Else, split the ordered array into two partitions, with all the elements less then the `middle value` as left partition and the elements greater than the `middle value` as right partition.
        - If the `middle value` is greater than the `searching value`: conduct binary serach on the left partition.
        - Else: conduct binary serach on the right partition.
- **Binary serach is only possible within an ordered array**.
- With linear search, there are as many steps as there are elements, whereas for binary search, each time we double the size of the array, we only need to add one more step.

