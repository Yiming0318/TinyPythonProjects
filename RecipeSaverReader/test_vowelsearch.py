from vowelsearch import contains_vowel, word_contains_vowel


def test_word_contains_vowel():
    assert(word_contains_vowel("aeiou") is True)
    assert(word_contains_vowel("") is False)
    assert(word_contains_vowel("    ") is False)
    assert(word_contains_vowel("affu") is True)
    assert(word_contains_vowel("ffff") is False)
    assert(word_contains_vowel("aFFu#!") is True)
    assert(word_contains_vowel("FF123") is False)


def test_contains_vowel():
    assert(contains_vowel(["garage", "this", "man"]) is True)
    assert(contains_vowel(["ffff", "this", "man"]) is False)
    assert(contains_vowel([]) is False)
    assert(contains_vowel([""]) is False)
    assert(contains_vowel(["  ", "  "]) is False)
    assert(contains_vowel(["Garage", "This", "maN123"]) is True)
    assert(contains_vowel(["FFF123$%", "this", "man"]) is False)
