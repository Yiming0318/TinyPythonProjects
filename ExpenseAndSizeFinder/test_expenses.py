from expenses import is_valid_start_end, is_vaild_mpg_fuel, calculate_mileage,\
    get_reimbursement_amount, get_actual_mileage_rate, get_actual_trip_cost


def test_is_valid_start_end():
    assert(is_valid_start_end(0, 0) is False)
    assert(is_valid_start_end(1, 0) is False)
    assert(is_valid_start_end(3, 5) is True)


def test_is_valid_mpg_fuel():
    assert(is_vaild_mpg_fuel(1, 0) is True)
    assert(is_vaild_mpg_fuel(12, 10) is True)
    assert(is_vaild_mpg_fuel(-1, -1) is False)


def test_calculate_mileage():
    assert(calculate_mileage(3, 1) == 0)
    assert(calculate_mileage(100, 200) == 100)
    assert(calculate_mileage(0, 1000) == 0)


def test_get_reimbursement_amount():
    assert(get_reimbursement_amount(0) == 0.00)
    assert(get_reimbursement_amount(50) == 28.75)
    assert(get_reimbursement_amount(100) == 57.50)
    assert(get_reimbursement_amount(-100) == 0.00)


def test_get_actual_mileage_rate():
    assert(get_actual_mileage_rate(10, 1234) == 123.4000)
    assert(get_actual_mileage_rate(0, 0) == 0.0)
    assert(get_actual_mileage_rate(10, 0) == 0.0000)


def test_get_actual_trip_cost():
    assert(get_actual_trip_cost(3, 4, 10, 0) == 0.00)
    assert(get_actual_trip_cost(-1, 4, 10, 0) == 0.0)
    assert(get_actual_trip_cost(3, 4, 10, 10) == 1.00)
