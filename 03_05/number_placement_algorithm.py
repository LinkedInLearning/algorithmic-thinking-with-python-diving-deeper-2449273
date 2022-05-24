import random

PUZZLE_SIZE = 10

# random.sample ensures no duplicates.
puzzle_nums = random.sample(range(100), PUZZLE_SIZE)
puzzle_symbols = []

for i in range(PUZZLE_SIZE - 1):
    puzzle_symbols.append(">" if random.random() < .5 else "<")

# Sort puzzle numbers first.
# Use largest remaining if greater than, smallest remaining if less than.

print(puzzle_nums)
print(puzzle_symbols)

sorted_puzzle_nums = sorted(puzzle_nums, reverse=True)
high = 0
low = PUZZLE_SIZE - 1
solution = []

for symbol in puzzle_symbols:
    if symbol == ">":
        solution.append(sorted_puzzle_nums[high])
        high += 1
    elif symbol == "<":
        solution.append(sorted_puzzle_nums[low])
        low -= 1
solution.append(sorted_puzzle_nums[high])

# Convert solution to strings
solution = list(map(str, solution))

puzzle = [None] * (len(solution) + len(puzzle_symbols))
puzzle[::2] = solution  # Nifty slicing with step
puzzle[1::2] = puzzle_symbols
print(" ".join(puzzle))
print(eval(" ".join(puzzle)))  # Some say eval is evil!
