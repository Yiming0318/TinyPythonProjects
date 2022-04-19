from days_until_friday import greeting, days_until_friday


def test_greeting():
    assert(greeting("cc") == "Hello, cc")


def test_days_until_friday():
    assert(days_until_friday("F") == 0)
