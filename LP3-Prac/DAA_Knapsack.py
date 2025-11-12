def knapsack(weights, values, capacity):
    n = len(values)
    # dp[i][w] = max value for first i items and capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the dp table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Option 1: include the item
                include_value = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                # Option 2: exclude the item
                exclude_value = dp[i - 1][w]
                # Take the max
                dp[i][w] = max(include_value, exclude_value)
            else:
                # Can't include the item
                dp[i][w] = dp[i - 1][w]
    
    # Final answer: max value for all items and full capacity
    return dp[n][capacity], dp


def knapsack_optimized(weights, values, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]

# Example Usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, dp_table = knapsack(weights, values, capacity)

print(f"Maximum value that can be obtained: {max_value}")
