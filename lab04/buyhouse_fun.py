'''
Yiming Ge
CS 5001, Fall 2021
Lab04 -- Problem 1

This is a program that
figure out how long until a user can buy a house with given factors
'''

'''
    Function -- downpayment
        calculate the downpayment of the house
    Parameters:
        house_cost -- The float number house price
    Return:
        Return the downpayment the float
'''


def downpayment(house_cost):
    downpayment = 0.25 * house_cost
    return downpayment


'''
    Function -- saving
        calculate the saving amount per month of the user
    Parameters:
        save_percent -- The saving percenatge per month, float
        annual_salary -- The annual salary, float
    Return:
        Return the saving amount per month of the user, float
'''


def saving(save_percent, annual_salary):
    YEAR_TO_MONTH = 12
    savings_per_month = annual_salary / YEAR_TO_MONTH * save_percent
    return savings_per_month


'''
    Function -- total_month
        caculate months it will take to save enough for the down payment
    Parameters:
        house_cost -- The float number house price
        save_percent -- The saving percenatge per month, float
        annual_salary -- The annual salary, float
    Return:
        Return the months it will take to save enough for down payment, integer
'''


def total_month(house_cost, save_percent, annual_salary):
    total_month = downpayment(house_cost) / saving(save_percent, annual_salary)
    # if larger than 1 year
    if total_month >= 12:
        total_year = total_month // 12
        lefting_month = total_month % 12
        return "It will take {} years and {} months to save enough for the \
             down payment".format(total_year, lefting_month)
    else:
        return "It will take {} months to save enough for the down payment" \
                .format(total_month)


def main():
    house_cost = float(input("How much is this house? "))
    annual_salary = float(input("What is your annual salary? "))
    save_percent = float(input("How much percent you can save \
                                 from you monthly salary? "))
    print(total_month(downpayment(house_cost), saving(save_percent,
                                                      annual_salary)))


if __name__ == "__main__":
    main()
