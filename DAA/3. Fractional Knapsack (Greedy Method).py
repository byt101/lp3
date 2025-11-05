# 3. Fractional Knapsack Problem (using inbuilt sort)

# Input data
weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50  # total capacity M

# Combine all items as (profit, weight, ratio)
items = []
for i in range(len(weights)):
    ratio = profits[i] / weights[i]
    items.append((profits[i], weights[i], ratio))

# Sort items by ratio (high to low)
items.sort(key=lambda x: x[2], reverse=True)

P = 0  # total profit
M = capacity

# Apply your given logic
for profit, weight, ratio in items:
    if M > 0 and weight <= M:
        M = M - weight
        P = P + profit
    else:
        break

# If capacity still left, take fractional part
if M > 0:
    P = P + profit * (M / weight)

print("Maximum Profit =", P)
