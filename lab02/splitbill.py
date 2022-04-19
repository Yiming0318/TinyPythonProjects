'''
Yiming Ge
CS 5001, Fall 2021
This is a program to
figure out how to split a restaurant bill.
'''


def main():
    # get three infomation: total amount of the bill, the tip percentage &
    # the number of total people
    total_amount = float(input("Enter the total amount of the bill: "))
    tip_percent = float(input("Enter the percentage everyone is willing to tip\
        (between 0 and 1): "))
    total_people = int(input("Enter the number of people: "))
    # get the money that each person should pay
    amount_per_person = total_amount * (1 + tip_percent) / total_people
    print("Each person should pay", amount_per_person, "dollars")


if __name__ == "__main__":
    main()
