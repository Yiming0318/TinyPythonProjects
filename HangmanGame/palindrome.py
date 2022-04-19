'''
Yiming Ge
CS 5001, Fall 2021
HW04 -- Problem 1

This is a a function takes a string as input and
returns True if the supplied string is a palindrome or False if not.
'''


def is_palindrome(input_string):
    '''
        Function -- is_palindrome
            determine whether the input is a palindrome (reads the same
            backwards and forwards, ignoring letter case and spaces,
            and is at least 2 characters in length.)
        Parameters:
            input_string -- any strings including none-letters and spaces
        Return:
            Return true if the input sring is palindrome,
            otherwise return false, a boolean
    '''
    standard_string = input_string.lower().replace(" ", "")
    if len(standard_string) > 1:
        return standard_string == standard_string[::-1]
    else:
        return False


def main():
    print(is_palindrome("madam  Im adam"))
    print(is_palindrome("a"))
    print(is_palindrome("RADar"))


if __name__ == "__main__":
    main()
