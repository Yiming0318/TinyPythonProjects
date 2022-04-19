from hangman import underscore_word, complete_word, check_correctness


def test_underscore_word():
    assert(underscore_word("APPLE") == "_____")
    assert(underscore_word("OBVIOUS") == "_______")
    assert(underscore_word("XYLOPHONE") == "_________")


def test_complete_word():
    assert(complete_word("A", "APPLE", "_____") == "A____")
    assert(complete_word("O", "OBVIOUS", "_______") == "O___O__")
    assert(complete_word("S", "XYLOPHONE", "_________") == "_________")


def test_check_correctness():
    assert(check_correctness(True, "APPLE") == (1, "You win!"))
    assert(check_correctness(False, "APPLE") == (0, "You lose! The word was"
           + " APPLE"))
