def ransom_note(magazine, note):
    mag_words = {}
    for word in magazine:
        if word in mag_words:
            mag_words[word] += 1
        else:
            mag_words[word] = 1
    for word in note:
        if mag_words.get(word, 0) < 1:
            return False
        else:
            mag_words[word] -= 1
    return True


# # This criminal has no regard for punctuation
magazine = "give me one grand today night".split()
note = "give one grand today".split()
assert ransom_note(magazine, note) is True

magazine = "two times three is not four".split()
note = "two times two is four".split()
assert ransom_note(magazine, note) is False
