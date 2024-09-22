def fractional_knapsack(capacity, values, weights):
    # Create a list of (value, weight, value/weight) and sort by value-to-weight ratio
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0.0  # To store the total value of items taken
    for value, weight in items:
        if capacity >= weight:  # If the knapsack can carry the whole item
            capacity -= weight
            total_value += value
        else:  # If the knapsack can only carry a fraction of the item
            total_value += value * (capacity / weight)
            break
    return total_value

# Example usage
values = [60, 100, 120]  # Values of the items
weights = [10, 20, 30]   # Corresponding weights of the items
capacity = 50            # Knapsack capacity
max_value = fractional_knapsack(capacity, values, weights)
print(f"Maximum value in the knapsack = {max_value}")
