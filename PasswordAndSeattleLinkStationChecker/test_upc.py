from upc import is_valid_upc


def test_is_valid_upc():
    assert(is_valid_upc('9780128053904'))
    assert(is_valid_upc('aeiouxy00 8') is False)
    assert(is_valid_upc('') is False)
    assert(is_valid_upc('1') is False)
    assert(is_valid_upc('031'))
