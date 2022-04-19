from problem3 import logarithm, bintodeci


def test_logarithm():
    assert(logarithm(0, 1) == 0)
    assert(logarithm(2, 1) == 0)
    assert(logarithm(2, 4) == 2)
    assert(logarithm(2, 5) == 2)


def test_bintodeci():
    assert(bintodeci('0101') == 5)
    assert(bintodeci('1') == 1)
    assert(bintodeci('1010') == 10)
    assert(bintodeci('101') == 5)
    assert(bintodeci('') == [])
