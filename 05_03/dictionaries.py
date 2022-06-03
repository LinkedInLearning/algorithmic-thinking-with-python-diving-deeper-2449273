def letter_freqs(a_string):
    freqs = {}
    for ch in a_string:
        if ch in freqs:
            freqs[ch] += 1
        else:
            freqs[ch] = 1
    return freqs


# A test string
my_string = "supercalifragilisticexpialidocious"

# Get result
result = letter_freqs(my_string)

# Some ways of displaying the result
print(result)
print(result.keys())
print(result.values())

for (key, value) in letter_freqs(my_string).items():
    print("Character", key, "count: ", value)
