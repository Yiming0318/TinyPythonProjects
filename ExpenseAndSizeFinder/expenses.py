'''
Yiming Ge
CS 5001, Fall 2021
HW03 -- Problem 2

This is a module that contains a set of functions for
helping user to calculate business trip driving expenses.
'''


def is_valid_start_end(start, end):
    '''
    Function -- is_valid_start_end
        determine whether the input start and end data are valid
    Parameters:
        start -- The odometer reading at the start of the trip. Expecting a
            number greater than 0.
        end -- The odometer reading at the end of the trip. Expecting a
            number greater than 0 and greater than the start value.
    Return:
        Return true if the input start and end are valid,
        otherwise return false, a boolean
    '''
    return end - start > 0 and start > 0 and end > 0


def is_vaild_mpg_fuel(mpg, fuel_price):
    '''
    Function -- is_valid_mpg_fuel
        determine whether the input mpg and fuel price are valid
    Parameters:
        mpg -- The car's miles per gallon (MPG), an integer greater than 0.
        fuel_price -- The fuel cost in dollars per gallon,
                      a non-negative float.
    Return:
        Return true if the input mpg and fuel price are valid,
        otherwise return false, a boolean
    '''
    return mpg > 0 and fuel_price >= 0


def calculate_mileage(start, end):
    '''
    Function -- calculate_mileage
        Calculates miles driven using the start and end odometer values.
    Parameters:
        start -- The odometer reading at the start of the trip. Expecting a
            number greater than 0.
        end -- The odometer reading at the end of the trip. Expecting a
            number greater than 0 and greater than the start value.
    Returns:
        The miles driven, a number. If either parameter is invalid (e.g.
        either parameter is negative or end is less than start), returns 0.
    '''
    if is_valid_start_end(start, end):
        miles_driven = end - start
        return miles_driven
    else:
        return 0


def get_reimbursement_amount(mileage):
    '''
    Function -- get_reimbursement_amount
        Calculates the amount in dollars that the employee should be
        reimbursed based on their mileage and the standard rate per mile.
        The standard rate for 2020 is 57.5 cents per mile.
    Parameters:
        mileage -- The number of miles driven.
    Returns:
        The amount the employee should be reimbursed in dollars, a float
        rounded to 2 decimal places.
    '''
    CENTS_TO_DOLLAR = 100
    STANDARD_RATE = 57.5
    if mileage >= 0:
        total_reimbursement_amount = round(mileage * STANDARD_RATE
                                           / CENTS_TO_DOLLAR, 2)
        return total_reimbursement_amount
    return 0.00


def get_actual_mileage_rate(mpg, fuel_price):
    '''
    Function -- get_actual_mileage_rate
        Calculates the actual trip cost per mile in dollars based on the
        car's MPG and the fuel price.
    Parameters:
        mpg -- The car's miles per gallon (MPG), an integer greater than 0.
        fuel_price -- The fuel cost in dollars per gallon,
                       a non-negative float.
    Returns:
        The actual cost per mile in dollars, a float rounded to 4 decimal
        places. If supplied arguments are invalid, returns 0.0
    '''
    if is_vaild_mpg_fuel(mpg, fuel_price):
        actual_cost_per_mile = round(fuel_price / mpg, 4)
        return actual_cost_per_mile
    else:
        return 0.0


def get_actual_trip_cost(start, end, mpg, fuel_price):
    '''
    Function -- get_actual_trip_cost
        Calculates the cost of a trip in dollars based on the miles driven,
        the MPG of the car, and the fuel price per gallon.
    Parameters:
        start -- The odometer reading at the start of the trip. Expecting a
            number greater than 0.
        end -- The odometer reading at the end of the trip. Expecting a
            number greater than 0 and greater than the start value.
        mpg -- The car's miles per gallon (MPG), an integer greater than 0.
        fuel_price -- The fuel price per gallon, a non-negative float.
    Returns:
        The cost of the drive in dollars, a float rounded to 2 decimal
        places. If any of the supplied arguments are invalid, returns 0.0
    '''
    if is_valid_start_end(start, end) and is_vaild_mpg_fuel(mpg, fuel_price):
        cost_of_the_drive = round(get_actual_mileage_rate(mpg, fuel_price)
                                  * calculate_mileage(start, end), 2)
        return cost_of_the_drive
    else:
        return 0.0


def main():
    print("MILEAGE REIMBURSEMENT CALCULATOR", "Options:", sep='\n')
    print("1 - Calculate reimbursement amount from odometer readings",
          "2 - Calculate reimbursement amount from miles traveled",
          "3 - Calculate the actual cost of your trip", sep='\n')
    choice = int(input("Enter your choice (1, 2, or 3): "))
    if choice > 3 or choice < 1:
        print("Not a valid choice")
    elif choice == 1:
        start = float(input("Enter your starting odometer reading: "))
        end = float(input("Enter your ending odometer reading: "))
        miles = calculate_mileage(start, end)
        print("You will be reimbursed ${:.2f}"
              .format(get_reimbursement_amount(miles)))
    elif choice == 2:
        miles = float(input("Enter the number of miles traveled: "))
        print("You will be reimbursed ${:.2f}"
              .format(get_reimbursement_amount(miles)))
    else:
        start = float(input("Enter your starting odometer reading: "))
        end = float(input("Enter your ending odometer reading: "))
        mpg = int(input("Enter your car's MPG: "))
        fuel_price = float(input("Enter the fuel price per gallon: "))
        print("Your trip cost ${:.2f}"
              .format(get_actual_trip_cost(start, end, mpg, fuel_price)))


if __name__ == "__main__":
    main()
