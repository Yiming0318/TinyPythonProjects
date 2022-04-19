from bintodeci import binary_to_decimal


def test_binary_to_decimal():
    assert(binary_to_decimal('010') == 2)
    assert(binary_to_decimal('0011') == 3)
    assert(binary_to_decimal('1111') == 15)
