'''
CS5001 2021 Fall
Problem 1 Recursive Binary Search
This is a Binary Search function using recursive
'''


def binary_search(lst, item):
    # find the mid-value
    mid = len(lst) // 2
    # If the value at the midpoint is equal to the search item, return True.
    if len(lst) == 1:
        return True if lst[mid] == item else False
    elif len(lst) == 0:
        return False
    elif lst[mid] == item:
        return True
    elif lst[mid] > item:
        return binary_search(lst[:mid], item)
    elif lst[mid] < item:
        return binary_search(lst[mid:], item)
    return False
