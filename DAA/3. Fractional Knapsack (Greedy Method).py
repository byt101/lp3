# 3. Fractional Knapsack

def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    ratio = []
    for i in range(n):
        ratio.append(values[i] / weights[i])

    # sort items by ratio (value per weight)
    for i in range(n):
        for j in range(i + 1, n):
            if ratio[i] < ratio[j]:
                ratio[i], ratio[j] = ratio[j], ratio[i]
                weights[i], weights[j] = weights[j], weights[i]
                values[i], values[j] = values[j], values[i]

    total_value = 0
    for i in range(n):
        if capacity >= weights[i]:
            total_value += values[i]
            capacity -= weights[i]
        else:
            total_value += ratio[i] * capacity
            break
    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value in Knapsack =", fractional_knapsack(weights, values, capacity))
