from tabulate import tabulate


def knapsack(max_capacity, weights, values):
    num_items = len(values)
    results_table = [[0 for _ in range(max_capacity + 1)] for _ in range(num_items + 1)]

    # Build results table in bottom-up manner
    for i in range(num_items + 1):
        for j in range(max_capacity + 1):
            # This initial empty rows and columns
            if i == 0 or j == 0:
                results_table[i][j] = 0
            # The rest of the cells
            elif weights[i - 1] <= j:
                results_table[i][j] = max(results_table[i - 1][j], values[i - 1]
                                          + results_table[i - 1][j - weights[i - 1]])
            else:
                results_table[i][j] = results_table[i - 1][j]

    # Display results table
    print(tabulate(results_table, tablefmt="pretty"))

    # for row in results_table:
    #     for el in row:
    #         print(el, end=",")
    #     print()

    return results_table[num_items][max_capacity]


values = [10, 5, 20, 35]
weights = [1, 2, 3, 5]
max_capacity = 6

print(knapsack(max_capacity, weights, values))
