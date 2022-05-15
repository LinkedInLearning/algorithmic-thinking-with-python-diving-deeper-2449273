import random

PUZZLE_SIZE = 5


def number_placement_game():
    # random.sample ensures no duplicates.
    puzzle_nums = random.sample(range(100), PUZZLE_SIZE)
    puzzle = []

    for i in range(PUZZLE_SIZE - 1):
        puzzle.append("?")
        puzzle.append(">" if random.random() < .5 else "<")
    puzzle.append("?")

    print("### Number Placement Puzzle ###")
    print("Arrange the puzzle numbers so that the puzzle statement is true.\n")
    print("Puzzle numbers:", *puzzle_nums)  # Nifty unpacking operator
    print("Puzzle statement:", " ".join(puzzle))  # ?<?<?<?<?

    player_numbers = get_player_input(puzzle_nums)
    number_positions = list(range(0, 2 * PUZZLE_SIZE - 1, 2))
    for i in range(PUZZLE_SIZE):
        puzzle[number_positions[i]] = str(player_numbers[i])
    print("You answered:", " ".join(puzzle))

    if eval("".join(puzzle)):  # Eval is only evil if used carelessly.
        print("Yay, you are correct.")
    else:
        print("Too bad. Wrong this time.")


def get_player_input(puzzle_nums):
    is_valid_input = False
    while not is_valid_input:
        print("Enter the puzzle numbers in the correct order, separated by spaces.")
        player_values = input(": ")
        is_valid_input = validate_user_input(player_values, puzzle_nums)
    return list(map(int, player_values.split()))


def validate_user_input(player_values, puzzle_nums):
    try:
        user_input_processed = list(map(int, player_values.split()))
    except ValueError:
        print("There is a problem with your input.")
        return False
    if len(user_input_processed) != PUZZLE_SIZE:
        print(f"Please enter {PUZZLE_SIZE} numbers.")
        return False
    if sorted(user_input_processed) != sorted(puzzle_nums):
        print("The numbers do not match.")
        return False
    return True


def play_again():
    print()
    print("Would you like to play again (yes or no)?")
    return input().lower().startswith("y")


lets_play_again = True
while lets_play_again:
    number_placement_game()

    if not play_again():
        lets_play_again = False
print("Goodbye!")
