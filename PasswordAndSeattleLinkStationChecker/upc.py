'''
Yiming Ge
CS 5001, Fall 2021
HW05 -- Problem 1
This a function called is_valid_upc that takes a stringas input and
returns True if the supplied string is a valid UPC or False if it’s not.
'''


def is_valid_upc(upc):
    '''
        Function -- is_valid_upc
            Check the given string whether is valid
        Parameter:
            upc -- a universal product code which user can find near the
                      barcode on most products. A string.
        Returns:
            Return True if the given upc is a valid UPC
            or False if it's not
    '''
    if upc.isdigit() is True:   # check whether the given ups is digit
        total = 0
        for index, number in enumerate(reversed(upc)):   # from right to left
            if index % 2 == 0:  # even index
                total += int(number)
            else:   # odd index
                total += int(number) * 3
        return total % 10 == 0
    else:
        return False


def main():
    print(is_valid_upc('9780128053904'))  # True
    print(is_valid_upc('0 a e'))   # False
    print(is_valid_upc('0 '))   # False


if __name__ == "__main__":
    main()
