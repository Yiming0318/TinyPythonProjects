from buyhouse_fun import downpayment, saving, total_month
from pytest import approx


def test_downpayment():
    assert(downpayment(1000) == 250)


def test_saving():
    assert(saving(0.1, 12000) == 100)


def test_total_month():
    assert(total_month(1000, 0.1, 12000) ==
           "It will take 2.5 months to save enough for the down payment")
