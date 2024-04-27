def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


for i in range(8):
    print(fibonacci_recursive(i), end=", ")  # 0, 1, 1, 2, 3, 5, 8, 13
