from sizefinder import is_valid_measurement, get_size, \
    get_kids_size, get_womens_size, get_mens_size


def test_is_valid_measurement():
    assert(is_valid_measurement(0, 53, 26) is False)
    assert(is_valid_measurement(30, 36, 26) is True)
    assert(is_valid_measurement(42, 42, 30) is False)


def test_get_size():
    assert(get_size(31, 36, 26, 2) == "L")
    assert(get_size(34, 42, 30, 2) == "L")
    assert(get_size(42, 53, 34, 3) == "L")


def test_get_kids_size():
    assert(get_kids_size(22) == "Kids size: not available")
    assert(get_kids_size(32.5) == "Kids size: XL")
    assert(get_kids_size(35) == "Kids size: XXL")
    assert(get_kids_size(36) == "Kids size: not available")


def test_get_womens_size():
    assert(get_womens_size(22) == "Womens size: not available")
    assert(get_womens_size(32.5) == "Womens size: M")
    assert(get_womens_size(36) == "Womens size: XL")
    assert(get_womens_size(42) == "Womens size: not available")


def test_get_mens_size():
    assert(get_mens_size(22) == "Mens size: not available")
    assert(get_mens_size(32.5) == "Mens size: not available")
    assert(get_mens_size(36) == "Mens size: S")
    assert(get_mens_size(53) == "Mens size: not available")
