"""
Find the greatest product of any two numbers in an array

Greedy Algorithm

1. Assign 0 to three variables (pos, neg, product)
2. Iterate over the array:
    1. If the element is positive:
        1. If pos = 0:
            pos = element and continue to the next iteration
        2. If pos * element > product:
            product = pos * element
        3. If element > pos: pos = element
    2. Elif the element is negative:
        1. If neg = 0:
            neg = element and continue to the next iteration
        2. If neg * element > product:
            product = neg * element
        3. If element < neg: neg = element
3. Print out product
"""

def find_max_product(array):
    pos = 0
    neg = 0
    product = 0

    for element in array:
        if element > 0:
            if pos == 0:
                pos = element
                continue
            if pos * element > product:
                product = pos * element
            if pos < element:
                pos = element
        elif element < 0:
            if neg == 0:
                neg = element
                continue
            if neg * element > product:
                product = neg * element
            if element < neg:
                neg = element
    print(product)

if __name__ == "__main__":
    array = [5, -10, -6, -9 ,4]
    find_max_product(array)