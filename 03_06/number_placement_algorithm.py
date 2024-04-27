import random

PUZZLE_SIZE = 10

# Create random puzzle
# random.sample ensures no duplicates
puzzle_nums = random.sample(range(100), PUZZLE_SIZE)
puzzle_symbols = []

# Randomly assign inequalities
for i in range(PUZZLE_SIZE - 1):
    puzzle_symbols.append(">" if random.random() < .5 else "<")

# print(puzzle_nums)
# print(puzzle_symbols)

# Sort puzzle numbers first
# Use largest remaining if greater than, smallest remaining if less than
sorted_puzzle_nums = sorted(puzzle_nums, reverse=True)

# Vars for the "two pointer" method
high = 0
low = PUZZLE_SIZE - 1

# store solution values
solution_values = []

# Your code goes here
# Iterate through the inequalities and apply solution algorithm to populate solution_values
# You may need to add the last value outside the loop
pass

# Convert solution_values to list of strings
solution_values = list(map(str, solution_values))

# Create a list to store the final solution representation
final_solution_representation = [None] * (len(solution_values) + len(puzzle_symbols))

# Create solution representation using nifty slicing with step parameter
final_solution_representation[::2] = solution_values
final_solution_representation[1::2] = puzzle_symbols

# Display final solution
# The join() method takes all items in an iterable and joins them into one string
print(" ".join(final_solution_representation))

# Evaluate whether solution is correct. Some say eval is evil!
print(eval(" ".join(final_solution_representation)))
