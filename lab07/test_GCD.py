from GCD import gcd, gcd_n_numbers


def test_gcd():
    assert(gcd(10, 20) == 10)
    assert(gcd(20, 10) == 10)
    assert(gcd(1, 1) == 1)


def test_n_numbers():
    assert(gcd_n_numbers([]) == [])
    assert(gcd_n_numbers([0]) == 0)
    assert(gcd_n_numbers([11, 22, 33]) == 11)
    assert(gcd_n_numbers([22, 11, 33]) == 11)
    assert(gcd_n_numbers([1, 2]) == 1)
