def fib_tabulate(n):
    results_so_far = [0, 1]
    for i in range(2, n + 1):
        results_so_far.append(results_so_far[i - 1] + results_so_far[i - 2])
    return results_so_far[n]


for i in range(8):
    print(fib_tabulate(i))
