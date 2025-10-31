# 4. 0-1 Knapsack using Dynamic Programming

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print("Maximum value =", knapsack(values, weights, capacity))
