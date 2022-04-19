from min_shift_list import shift_search


def test_shift_search():
    assert(shift_search([18, 25, 38, 1, 12, 13]) == 1)
    assert(shift_search([25, 38, 40, 12, 13]) == 12)
    assert(shift_search([12, 13, 25, 38]) == 12)
    assert(shift_search([25, 38, 12, 13]) == 12)
    assert(shift_search([25, 38, 38, 12, 13]) == 12)
    assert(shift_search([1]) == 1)
    assert(shift_search([2, 1]) == 1)
