'''
Yiming Ge
CS 5001, Fall 2021
HW06 -- Problem 1

This is a recursive function called contains_vowel that,
given a list of strings, returns True if every string
in the list contains a vowel, and False otherwise.
'''


def contains_vowel(string_list):
    '''
        Function -- contains_vowel
            Determine whether every string in the given list contain a vowel
        Parameters:
            string_list -- any list of strings including empty list
        Return:
            Returns True if every string in the list contains a vowel,
            and False otherwise.
    '''
    if len(string_list) == 0:
        return False
    if len(string_list) == 1:
        return word_contains_vowel(string_list[0])
    return word_contains_vowel(string_list[0]) and \
        contains_vowel(string_list[1:])


def word_contains_vowel(word):
    '''
        Function -- word_contains_vowel
            Determine whether every string in the given word contain a vowel.
        Parameters:
            word -- any strings including empty string "".
        Return:
            Returns True if any string in the word contains a vowel,
            and False otherwise.
    '''
    vowels = ["a", "e", "i", "o", "u"]
    word = word.lower()
    if len(word) == 0:
        return False
    else:
        return word[0] in vowels or word_contains_vowel(word[1:])
