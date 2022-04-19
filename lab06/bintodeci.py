'''
Yiming Ge
CS 5001, Fall 2021
Lab06 -- Problem 2
This is a function to compute the log base 2 of powers of 2.
'''


def binary_to_decimal(binary_number):
    right_to_left = binary_number[::-1]
    sum = 0
    for index, value in enumerate(right_to_left):
        sum += int(value) * (2 ** index)
    return sum


def main():
    input_number = input("enter a binary number: ")
    print(binary_to_decimal(input_number))


if __name__ == "__main__":
    main()
