from palindrome import is_palindrome


def test_is_palindrome():
    assert(is_palindrome("a") is False)
    assert(is_palindrome("madam  Im adam") is True)
    assert(is_palindrome("RADar") is True)
    assert(is_palindrome("!RADar!") is True)
    assert(is_palindrome("R  AD  ar") is True)
    assert(is_palindrome("taco cat") is True)
    assert(is_palindrome("   afk   ") is False)
    assert(is_palindrome("   z   ") is False)
