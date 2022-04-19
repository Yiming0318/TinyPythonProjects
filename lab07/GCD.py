'''
Yiming Ge
CS 5001, Fall 2021
Lab07 -- Problem 2
This a a recursive function to determine the greatest common divisor (GCD)
of two non-zero positive integers.
'''


def gcd(A, B):
    '''
        Function  -- gcd
            a recursive function to determine the greatest common divisor (GCD)
            of two integers
        Parameter:
            A -- integer A
            B -- integer B
        Returns:
            The greatest common divisor of two integers
    '''
    if B == 0:
        return A
    return gcd(B, A % B)


def gcd_n_numbers(number_list):
    '''
        Function  -- gcd_n_numbers
            a recursive function to determine the greatest common divisor (GCD)
            of n integers
        Parameter:
            number_list -- a list of numbers (len(number_list) >= 1)
        Returns:
            The greatest common divisor of a list of numbers
    '''
    if len(number_list) == 0:
        return []
    if len(number_list) == 1:
        return number_list[0]
    if len(number_list) == 2:
        return gcd(number_list[0], number_list[1])
    return gcd(number_list[0], gcd_n_numbers(number_list[1:]))
