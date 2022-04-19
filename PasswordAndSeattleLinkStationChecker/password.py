'''
Yiming Ge
CS 5001, Fall 2021
HW05 -- Problem 2
This a function called secure_password that takes a string and checks
if it is a secure password according to the following rules:
It is between 9 and 12 characters long (inclusive)
AND it meets at least 3 of these requirements:
At least one lowercase letter
At least one uppercase letter
At least one digit (0-9)
At least 1 of the following special characters: $, #, @, !
AND it does not contain any special characters other than $, #, @, or !
'''


def check_length(password, min_length, max_length):
    '''
        Function -- check_length
            Check whether the length of given password meets the
            length requirement: between 9 and 12 characters long (inclusive)
        Parameter:
            password -- the given password that user wants to use. A string.
            min_length -- the given minimum length.
            max_length -- the given maximum length.
        Returns:
            Return True if the given password meets the length requirement
            or False if it does not
    '''
    return len(password) <= max_length and len(password) >= min_length


def check_four_requirements(password, tolerance, special_characters):
    '''
    Function -- check_four_requirements
            Check whether the given password meets the bullet point two
            requirements with given tolerance. Here the requirement is to
            meet at least three out of four.
        Parameter:
            password -- the given password that user wants to use. A string.
            tolerance -- maximum false that function accepts for the given
                         four requirements. An integer.
            special_characters -- special characters that the algorithm accepts
        Returns:
            Return True if the given password meets the bullet point two
            requirement or False if it does not
    '''
    # create four requirements list (T or F list)
    lower_list = []
    upper_list = []
    digit_list = []
    special_list = []
    for letter in password:
        lower_list.append(True if letter.islower() else False)
        upper_list.append(True if letter.isupper() else False)
        digit_list.append(True if letter.isdigit() else False)
        special_list.append(True if letter in special_characters else False)
    # sum up the four requirements True False list separately
    # if one's sum equal to zero
    # which means the password does not meet its requirement
    sum_lower = sum(lower_list)
    sum_upper = sum(upper_list)
    sum_digit = sum(digit_list)
    sum_special = sum(special_list)
    four_requirements = [sum_lower, sum_upper, sum_digit, sum_special]
    # count how many 0 in the four_requirments
    # which means count how many Falses in these four requirments
    count = 0
    for number in four_requirements:
        if number == 0:
            count += 1
    # exceed the max tolerance
    if count > tolerance:
        return False
    return True


def check_special_characters(password, special_characters):
    '''
        Function -- check_special_characters
            Check whether the special characters in the given password
            contain any special characters other than
            those the algorithm accepts.
        Parameter:
            password -- the given password that user wants to use. A string.
            special_characters -- special characters that the algorithm accepts
        Returns:
            Return True if the given password meets the bullet point three
            requirement or False if it does not
    '''
    for letter in password:
        if letter.isalpha() is False and letter.isdigit() is False:
            if letter not in special_characters:
                return False
    return True


def secure_password(password):
    '''
        Function -- secure_word
            Check the given password whether is a secure password based on
            requirements
        Parameter:
            password -- the given password that user wants to use. A string.
        Returns:
            Return True if the given password is a secure password
            or False if it's not
    '''
    # min and max length that the function accepts
    MIN_LENGTH = 9
    MAX_LENGTH = 12
    # maximum false that function accepts for the given four requirements
    TOLERANCE = 1
    # special characters that function accepts
    SPECIAL_CHARACTERS = ['$', '#', '@', '!']
    # does not meet the length requirement (bullet point one)
    if check_length(password, MIN_LENGTH, MAX_LENGTH) is False:
        return False
    # does not meet the at least three requirements of four (bullet point two)
    if check_four_requirements(password, TOLERANCE, SPECIAL_CHARACTERS)\
            is False:
        return False
    # specail character is not in the given special list (bullet point three)
    if check_special_characters(password, SPECIAL_CHARACTERS) is False:
        return False
    return True
