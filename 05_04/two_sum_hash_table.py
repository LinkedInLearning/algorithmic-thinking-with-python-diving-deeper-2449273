# 2-Sum Interview Problem Solution

def two_sum_hash_table(arr, total):
    hash_table = {}
    for idx, val in enumerate(arr):
        complement = total - val
        if complement in hash_table:
            return idx, hash_table[complement]
        else:
            # The hash table stores the values from the array as keys, and the indices of
            # these values as the values in the table.
            print(f"Adding to hash table: key:{val}, value: {idx}")
        hash_table[val] = idx
    return None


assert two_sum_hash_table([1, 2, 3], 4) in [(0, 2), (2, 0)]
assert two_sum_hash_table([1234, 5678, 9012], 14690) in [(1, 2), (2, 1)]
assert two_sum_hash_table([2, 2, 3], 4) in [(0, 1), (1, 0)]
assert two_sum_hash_table([2, 2], 4) in [(0, 1), (1, 0)]
assert two_sum_hash_table([8, 7, 2, 5, 3, 1], 10) in [(0, 2), (2, 0), (1, 4), (4, 1)]
