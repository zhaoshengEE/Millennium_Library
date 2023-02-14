"""
Unique Path Problem -- The Staircase Problem in 2D

[[S, A, w, w, w, w, w],
[B, w, w, w, w, w, P],
[w, w, w, w, w, Q, F]]

Result: countPath(S -> F)
Subproblem: countPath(S -> Q) + countPath(S -> P)

Base Case 1: When we are outside the grid, return 0
Base Case 2: When we are at A or B, return 1

def countPath(grid, row, col):
1. If row < 0 or col < 0: return 0
2. If grid[row, col - 1] == 'S' or grid[row - 1, col] == 'S': return 1
3. return countPath(row, col - 1) + countPath(row - 1, col)
"""

def countPath(grid, row, col):
    if row < 0 or col < 0: return 0
    if grid[row][col - 1] == 'S' or grid[row - 1][col] == 'S': return 1
    return countPath(grid, row - 1, col) + countPath(grid, row, col - 1)

if __name__ == "__main__":
    grid = [['S', 'A', 'w', 'w', 'w', 'w', 'w'],
            ['B', 'w', 'w', 'w', 'w', 'w', 'P'],
            ['w', 'w', 'w', 'w', 'w', 'Q', 'F']]
    print(countPath(grid, len(grid) - 1, len(grid[0]) - 1))
