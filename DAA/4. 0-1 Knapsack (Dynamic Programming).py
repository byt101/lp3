# 4. 0-1 Knapsack using Recurrence Relation (Recursive)

def knapsack(n, capacity, profit, weight):
    # Base condition
    if n == 0 or capacity == 0:
        return 0

    # If item weight is more than remaining capacity, skip it
    if weight[n - 1] > capacity:
        return knapsack(n - 1, capacity, profit, weight)

    # Otherwise choose the better of two cases:
    # 1. Include current item
    # 2. Exclude current item
    else:
        include = profit[n - 1] + knapsack(n - 1, capacity - weight[n - 1], profit, weight)
        exclude = knapsack(n - 1, capacity, profit, weight)
        return max(include, exclude)


# Example input
profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
n = len(profit)

# Call the recursive function
max_profit = knapsack(n, capacity, profit, weight)
print("Maximum Profit =", max_profit)
