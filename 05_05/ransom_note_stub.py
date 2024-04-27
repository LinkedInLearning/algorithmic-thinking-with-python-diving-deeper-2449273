def ransom_note(magazine, note):
    pass


magazine = "give me one grand today night".split()
note = "give one grand today".split()
assert ransom_note(magazine, note) is True

magazine = "two times three is not four".split()
note = "two times two is four".split()
assert ransom_note(magazine, note) is False
