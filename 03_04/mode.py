def mode_presort(arr):
    arr.sort()  # Array must be sorted before we apply the algorithm.
    i = 0
    mode_frequency = 0
    while i < len(arr):
        run_length = 1
        run_value = arr[i]
        while i + run_length < len(arr) and arr[i + run_length] == run_value:
            run_length += 1
        if run_length > mode_frequency:
            mode_frequency = run_length
            mode_value = [run_value]  # Make it a list
        elif run_length == mode_frequency:  # Also deal with this case
            # Add alternative to existing list of modes
            mode_value.append(run_value)
        i += run_length
    return mode_value


arr = [1, 1, 1, 2, 2]
print(mode_presort(arr))
arr = [1, 1, 2, 2]
print(mode_presort(arr))
arr = [3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]
print(mode_presort(arr))
