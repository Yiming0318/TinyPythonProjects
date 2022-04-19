'''
Yiming Ge
CS 5001, Fall 2021
Lab04 -- Problem 3

This is a program that
will tell the user how many days there are until Friday.
'''


'''
    Function -- greeting
        Say hello to the user
    Parameters:
        name -- user's name, string
    Return:
        Return "Hello, <name>"
'''


def greeting(name):
    return "Hello, " + name


'''
    Function -- days_until_friday
        calculate the days until friday
    Parameters:
        day -- given day, string
    Return:
        number of days until friday, integer
'''


def days_until_friday(day):
    if day == "M":
        return 4
    elif day == "Tu":
        return 3
    elif day == "W" or day == "Su":
        return 2
    elif day == "F":
        return 0
    else:
        return 1


def main():
    name = input("What is your name? ")
    print(greeting(name))
    current_day = input("What day is today? ")
    print("{} days until Friday.".format(days_until_friday(current_day)))


if __name__ == "__main__":
    main()
