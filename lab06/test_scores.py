from scores import average, median, lowest, highest


def test_average():
    assert(average([2, 4, 6]) == 4)
    assert(average([1, 3, 5]) == 3)
    assert(average([1, 2, 3]) == 2)
    assert(average([2, 3, 1]) == 2)
    assert(average([]) == 'empty list')


def test_median():
    assert(median([2, 4, 6]) == 4)
    assert(median([1, 3, 5]) == 3)
    assert(median([1, 2, 3]) == 2)
    assert(median([2, 3, 4, 1]) == 2.5)
    assert(median([]) == 'empty list')


def test_lowest():
    assert(lowest([2, 4, 6]) == 2)
    assert(lowest([1, 3, 5]) == 1)
    assert(lowest([1, 2, 3]) == 1)
    assert(lowest([2, 3, 1]) == 1)
    assert(lowest([]) == 'empty list')


def test_highest():
    assert(highest([2, 4, 6]) == 6)
    assert(highest([1, 3, 5]) == 5)
    assert(highest([1, 2, 3]) == 3)
    assert(highest([2, 3, 1]) == 3)
    assert(highest([]) == 'empty list')
