'''
Yiming Ge
CS 5001, Fall 2021
This is a program to
figure out how long until a user can buy a house with given factors
'''


def main():
    # get the information including cost of the house, annual salary, percent
    # that the user can save per month
    house_cost = float(input("How much is this house? "))
    annual_salary = float(input("What is your annual salary? "))
    save_percent = float(input("How much percent you can save from \
        your monthly salary? "))
    # get the down payment of the house
    downpayment = 0.25 * house_cost
    # get the saving amount per month of the user
    savings_per_month = annual_salary / 12 * save_percent
    # caculate months it will take to save enough for the down payment
    total_month = downpayment / savings_per_month
    if total_month >= 12:  # if larger than 1 year
        total_year = total_month // 12
        lefting_month = total_month % 12
        print("If you save", savings_per_month, "per month", "it will take",
              total_year, "years and", lefting_month, "months to save \
              enough for the down payment", downpayment, "dollars.")
    else:
        print("If you save", savings_per_month, "per month", "it will take",
              total_month, "months to save enough for the down payment",
              downpayment, "dollars.")


if __name__ == "__main__":
    main()
