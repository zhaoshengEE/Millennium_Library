"""
Calculate the maximum profit that could be made from a single buy trasaction followed by a single sell transaction

Greedy Algorithm

1. Assign the first data to a variable called buy
2. Initialize a varibale called profit with value of 0
3. Iterate over the array from the 2nd element:
    1. If element - buy is less than 0:
        1. buy = element
    2. Elif element - buy is greater than profit:
        1. profit = element - buy
4. Print out profit
"""

def calculate_max_profit(array):
    buy = array[0]
    profit = 0
    for i in range(1, len(array)):
        if array[i] - buy < 0:
            buy = array[i]
        elif array[i] - buy > profit:
            profit = array[i] - buy
    print(profit)

if __name__ == "__main__":
    array = [10, 7, 5, 8, 11, 2, 6]
    calculate_max_profit(array)