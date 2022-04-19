'''
Yiming Ge
CS 5001, Fall 2021
HW03 -- Problem 1

This is a program that
is able to help users to get their size
according to the company's three size charts: kids, women, and men
based on given chest measurement.
'''


'''
    Function -- is_valid_measurement
        determine whether the given chest measurement is valid
    Parameters:
        chest_measurement -- The given chest measurement from user,
                             a float number
        max_measurement -- The given maximum chest measurement, an integer
        min_measurement -- The given minimum chest measurement, an integer
    Return:
        Return true if the given chest measurement is valid, otherwise false,
        a boolean
'''


def is_valid_measurement(chest_measurement, max_measurement, min_measurement):
    return chest_measurement < max_measurement \
       and chest_measurement >= min_measurement


'''
    Function -- get_size
        get the user's size based on given chest measurement, the chart's max,
        min and interval value
    Parameters:
        chest_measurement -- The given chest measurement from user,
                             a float number
        max_measurement -- The given maximum chest measurement
                           according to three size charts, an integer
        min_measurement -- The given minimum chest measurement
                           according to three size charts, an integer
        interval -- The chest inches interval between the change of two size
                    in the size chart, an integer
    Return:
        The size based on given chest measurement, the chart's max, min
        and interval value, a string
'''


def get_size(chest_measurement, max_measurement, min_measurement, interval):
    S = 1
    M = 2
    L = 3
    XL = 4
    XXL = 5
    if is_valid_measurement(chest_measurement, max_measurement,
                            min_measurement):
        if chest_measurement >= min_measurement \
                and chest_measurement < min_measurement + S * interval:
            return "S"
        elif chest_measurement >= min_measurement + S * interval \
                and chest_measurement < min_measurement + M * interval:
            return "M"
        elif chest_measurement >= min_measurement + M * interval \
                and chest_measurement < min_measurement + L * interval:
            return "L"
        elif chest_measurement >= min_measurement + L * interval \
                and chest_measurement < min_measurement + XL * interval:
            return "XL"
        elif chest_measurement >= min_measurement + XL * interval \
                and chest_measurement < min_measurement + XXL * interval:
            return "XXL"
        else:
            return "XXXL"
    else:
        return "not available"


'''
    Function -- get_kid_size
        get the user's size based on given chest measurement
        and the kids size chart
    Parameters:
        chest_measurement -- The given chest measurement from user,
                             a float number
    Return:
        The size from the kids size chart, a string
'''


def get_kids_size(chest_measurement):
    # KID SIZE CHART MAX, MIN & INTERVAL
    MAX = 36
    MIN = 26
    INTERVAL = 2
    return "Kids size: " + get_size(chest_measurement, MAX, MIN, INTERVAL)


'''
    Function -- get_womens_size
        get the user's size based on given chest measurement
        and the womens size chart
    Parameters:
        chest_measurement -- The given chest measurement from user,
        a float number
    Return:
        The size from the womens size chart, a string
'''


def get_womens_size(chest_measurement):
    # WOMENS SIZE CHART MAX, MIN & INTERVAL
    MAX = 42
    MIN = 30
    INTERVAL = 2
    return "Womens size: " + get_size(chest_measurement, MAX, MIN, INTERVAL)


'''
    Function -- get_mens_size
        get the user's size based on given chest measurement
        and the mens size chart
    Parameters:
        chest_measurement -- The given chest measurement from user,
        a float number
    Return:
        The size from the mens size chart, a string
'''


def get_mens_size(chest_measurement):
    # MENS SIZE CHART MAX, MIN & INTERVAL
    MAX = 53
    MIN = 34
    INTERVAL = 3
    return "Mens size: " + get_size(chest_measurement, MAX, MIN, INTERVAL)


def main():
    # The maximum and minimum chest measurement of
    # the three size charts together
    CHARTS_MAX = 53
    CHARTS_MIN = 26
    chest_measurement = float(input("Chest measurement in inches: "))
    if is_valid_measurement(chest_measurement, CHARTS_MAX, CHARTS_MIN) \
            is False:
        print("Sorry, we don't carry your size")
    else:
        print("Your size choices:")
        print(get_kids_size(chest_measurement),
              get_womens_size(chest_measurement),
              get_mens_size(chest_measurement), sep='\n')


if __name__ == "__main__":
    main()
