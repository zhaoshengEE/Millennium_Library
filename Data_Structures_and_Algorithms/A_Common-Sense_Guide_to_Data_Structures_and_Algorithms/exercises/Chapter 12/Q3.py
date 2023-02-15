"""
Optimize the code in comment with memoization
"""

# def unique_paths(rows, columns):
#     if rows == 1 or columns == 1:
#         return 1
#     return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)

def unique_paths(rows, columns, memo = {}):
    if rows == 1 or columns == 1:
        return 1
    if (rows, columns) not in memo:
        memo[(rows, columns)] = unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
    return memo[(rows, columns)]

if __name__ == "__main__":
    a = unique_paths(3, 7)
    print(a)