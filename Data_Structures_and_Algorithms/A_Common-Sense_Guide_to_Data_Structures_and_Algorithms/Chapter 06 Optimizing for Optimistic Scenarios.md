# Chapter 6. Optimizing for Optimistic Scenarios


## Insertion Sort

- We temporarily remove the value at index 1 (or say store the value into a temporary variable) and leave a gap at index 1 in the first pass-through. 
    - In the subsequent pass-throughs, we initially remove the value at the subsequent index. That is, at the second pass-through, we remove the value at index 2 and leave a gap at index 2 initially.
- Take the value to the left of the gap and compare it with the temporarily removed value.
    - If the value is greater than the removed value, we shift the value to the right and decrement the index of the gap.
    - If the value is less than the removed value OR we touch the leftmost value of the array, we proceed to the next pass-through.
- Repeat the pass-through until we start at the final index of the array
    - *NOTE*: we need to finish conducting the shifting phase when we start at the final index.


## Another Big O Major Rule

> Big O Notation only takes into account the highest order of N when we have multiple orders added together.


## Demonstration of Optimizing Algorithm with Adding One Line of Code

Get the intersection between two arrays:

```js
function intersection(firstArray, secondArray){
    let result = [];

    for (let i = 0; i < firstArray.length; i++){
        for (let j = 0; j < secondArray.length; j++){
            if (firstArray[i] == secondArray[j]){
                result.push(firstArray[i]);
            }
        }
    }
    return result;
}
```

```js
function intersection(firstArray, secondArray){
    let result = [];

    for (let i = 0; i < firstArray.length; i++){
        for (let j = 0; j < secondArray.length; j++){
            if (firstArray[i] == secondArray[j]){
                result.push(firstArray[i]);
                break
            }
        }
    }
    return result;
}
```

With simply adding the `break` statement, we can eliminate tons of unnecessary comparison steps, thereby improve the algorithm performance.
