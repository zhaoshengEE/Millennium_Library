# Chapter 8. Blazing Fast Lookup with Hash Tables

If the algorithm requires multiple searches (lookups), `Hash Table` would be the first priority data structure.

## Synonyms

- Hashes
- Maps
- Hash Maps
- Dictionaries
- Associative Arrays

Essentially, a hash table is a list of paired values.

## Search (Lookup) in Hash Tables

**If we know the key of the searched value**, searching in a hash table is typically O(1).

*Mechanism*: The computer hashes the key into a number, and jumps to the index with that number to retrieve the values stored there

The search works in one direction: we use the key to find the value, but the value does not determine the key's location.

## Collision

> In many languages, if we try to store a key-value pair where key already exists, it simply overwrites the old value while keeping the same key. And this is known as a collision.

To handle the collision, an approach called `separate chaining` comes up. Essentially, the approaches stores an array in each cell of the hash table, instead of storing a single value in each cell. But if all of the data ended up within a single cell of the hash table, the hash table is no better than an array.

To avoid collision and not consuming too much memory, a rule of thumb is develpoed in Computer Science: **For every 7 data elements stored in a hash table, it should have 10 cells**, which means the `load factor` (i.e., the ratio of data to cells) should be 0.7


## Usage of Hash Tables

### Simplify Conditional Logic

```python
def status_code_meaning(number):
    if number == 200: return "OK"
    elif number == 301: return "Moved Permanently"
    elif number == 401: return "Unauthorized"
    elif number == 404: return "Not Found"
    elif number == 500: return "Internet Server Error"
```

```python
STATUS_CODES = {"200": "OK", "301": "Moved Permanently", "401": "Unauthorized", "404": "Not Found", "500": "Internet Server Error"}
```

### Using It as an Index

Hash table tells us wheter a specific item is contained within the array. Please refer to the [exercise questions of this chapter](./exercises/Chapter%2008/)
