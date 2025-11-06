# 4. 0-1 Knapsack using Dynamic Programming (Top-Down)

def knapsack(n, capacity, profit, weight, dp):
    # Base condition
    if n == 0 or capacity == 0:
        return 0

    # If already calculated, return stored value
    if dp[n][capacity] != -1:
        return dp[n][capacity]

    # If current item is too heavy, skip it
    if weight[n - 1] > capacity:
        dp[n][capacity] = knapsack(n - 1, capacity, profit, weight, dp)
    else:
        # Option 1: include the item
        include = profit[n - 1] + knapsack(n - 1, capacity - weight[n - 1], profit, weight, dp)
        # Option 2: exclude the item
        exclude = knapsack(n - 1, capacity, profit, weight, dp)
        # Store max of both options
        dp[n][capacity] = max(include, exclude)

    return dp[n][capacity]


# Example input
profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
n = len(profit)

# DP table initialized with -1
dp = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Function call
print("Maximum Profit (DP) =", knapsack(n, capacity, profit, weight, dp))
