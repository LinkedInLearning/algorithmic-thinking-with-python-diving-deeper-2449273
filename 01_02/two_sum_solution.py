# 2-Sum Interview Problem

# Brute force solution
def two_sum_problem(arr, target):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
    return None


assert two_sum_problem([1, 2, 3], 4) == (0, 2)
assert two_sum_problem([1234, 5678, 9012], 14690) == (1, 2)
assert two_sum_problem([2, 2, 3], 4) in [(0, 1), (1, 0)]
assert two_sum_problem([2, 2], 4) in [(0, 1), (1, 0)]
assert two_sum_problem([8, 7, 2, 5, 3, 1], 10) in [(0, 2), (2, 0), (1, 4), (4, 1)]
