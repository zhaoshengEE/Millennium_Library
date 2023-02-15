"""
Optimize the code in comment with memoization
"""

# def golomb(n):
#     if n == 1:
#         return 1
#     return 1 + golomb(n - golomb(golomb(n - 1)))

def golomb(n, memo = {}):
    if n == 1:
        return 1

    if n not in memo:
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    return memo[n]

if __name__ == "__main__":
    a = golomb(20)
    print(a)