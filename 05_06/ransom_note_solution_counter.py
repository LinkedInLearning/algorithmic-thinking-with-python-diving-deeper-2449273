from collections import Counter


def ransom_note(magazine, note):
    mag_counter = Counter(magazine)
    note_counter = Counter(note)
    # intersection operator &. This returns the minimum of corresponding counts.
    return mag_counter & note_counter == note_counter


# # This criminal has no regard for punctuation
magazine = "give me one grand today night".split()
note = "give one grand today".split()
assert ransom_note(magazine, note) is True

magazine = "two times three is not four".split()
note = "two times two is four".split()
assert ransom_note(magazine, note) is False
